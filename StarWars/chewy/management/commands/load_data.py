from django.core.management.base import BaseCommand
import requests
import re

from chewy.models.people import People
from chewy.models.planet import Planet
from chewy.models.film import Film
from chewy.models.species import Species
from chewy.models.transport import Vehicle, Starship

# ------------------------------------------------------------------------------
# Gobal variables
# ------------------------------------------------------------------------------
dict_planets = {}


# ------------------------------------------------------------------------------
# Functions of load_data
# ------------------------------------------------------------------------------
# API connection, and check if it is a succesful connection
def secure_request(url):
    response = requests.get(url)
    while response.status_code != 200:
        response = requests.get(url)
    return response


# Regex to check if a string is an url or not
def is_an_url(string):
    return (
        re.findall(
            "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
            string,
        )
        != []
    )


def switch(opt):
    switcher = {
        "planets": str(1) + opt[1],
        "people": str(2) + opt[1],
        "films": str(3) + opt[1],
        "species": str(4) + opt[1],
        "vehicles": str(5) + opt[1],
        "starships": str(6) + opt[1],
    }
    # pk_model = X-ID of url, X belongs to integers
    return switcher[opt[0]]


def get_id(string):
    id_ = []
    if isinstance(string, list):
        for s in string:
            id_.append(switch(opt=[s.split("/")[-3], s.split("/")[-2]]))
    else:
        id_ = switch(opt=[string.split("/")[-3], string.split("/")[-2]])
    return id_


# Function to save a page in the database
def save_page(model, act_page):
    DB_objects = model.objects.all()  # take the objects of the actual model
    act_object = model()  # create an object of this model
    qs_fields = model._meta.get_fields()  # fields of the actual queryset

    if model == Planet:
        for elem in act_page:
            act_id = get_id(elem["url"])
            dict_planets.update(
                {
                    act_id: Planet(
                        pk=act_id,
                        name=elem["name"],
                        rotation_period=elem["rotation_period"],
                        orbital_period=elem["orbital_period"],
                        diameter=elem["diameter"],
                        climate=elem["climate"],
                        gravity=elem["gravity"],
                        terrain=elem["terrain"],
                        surface_water=elem["surface_water"],
                        population=elem["population"],
                    )
                }
            )
            if not DB_objects.filter(pk=act_object.pk).exists():
                dict_planets[act_id].save(force_insert=True)
        # First of all save all the planets, that doesnt have any relations
    else:
        for elem in act_page:  # take the elements of the actual page
            for field in qs_fields:  # take each field of the actual model
                if (
                    # not field.many_to_many
                    not field.is_relation
                    and field.name != "created"
                    and field.name != "edited"
                ):
                    if field.name == "id":
                        setattr(act_object, "pk", get_id(elem["url"]))
                        # pk = id de la url del objeto
                    else:
                        setattr(act_object, field.name, elem[field.name])
                else:
                    if field.name == "homeworld":
                        setattr(
                            act_object,
                            "homeworld",
                            dict_planets[get_id(elem[field.name])],
                        )
                        # Set a planet as a foreign key of a model
                    if field.name == "pilots" or field.name == "people":
                        pk_ = get_id(elem[field.name])
                        for ppl in pk_:
                            people = People.objects.get(pk=ppl)
                            if not DB_objects.filter(pk=act_object.pk).exists():
                                act_object.save(force_insert=True)
                            getattr(act_object, field.name).add(people)
                            # Set the relation m2m of pilots in transport and people of species

            if not DB_objects.filter(pk=act_object.pk).exists():
                act_object.save(force_insert=True)
                # If the object is not in the database then save it
            act_object = model()


# ------------------------------------------------------------------------------
# load_data function
# ------------------------------------------------------------------------------
class Command(BaseCommand):
    help = "Command to load/update the data from the API to the app"

    def handle(self, *args, **options):
        urls = [
            "https://swapi.co/api/planets/",
            "https://swapi.co/api/people/",
            "https://swapi.co/api/starships/",
            "https://swapi.co/api/vehicles/",
            "https://swapi.co/api/species/",
            "https://swapi.co/api/films/",
        ]
        # Take all the urls on the API to manage

        my_models = {
            "people": People,
            "planets": Planet,
            "films": Film,
            "species": Species,
            "vehicles": Vehicle,
            "starships": Starship,
        }
        # Take all the models that I have

        for m in my_models:
            my_models[m].objects.all().delete()
        # Drop all the tables of the database

        for elem in urls:  # every url on the api
            model = elem.split("/")[-2]  # take the string of the model e.g(people)
            actual_model = my_models[model]  # take the act model to manage e.g(People)
            resp = secure_request(elem).json()  # make a reqst to the page of the model
            next_page = resp["next"]  # take the next page of the actual model

            # First of all I've to save the first page, bc it couldn't have more than 1 page
            save_page(model=actual_model, act_page=resp["results"])
            while next_page is not None:
                # Now I have to iterate the rest of the pages
                r = secure_request(next_page).json()
                save_page(model=actual_model, act_page=r["results"])
                next_page = r["next"]

        self.stdout.write(self.style.SUCCESS("Successfully data charge"))
