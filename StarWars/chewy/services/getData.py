import requests
import re

from chewy.models.people import People
from chewy.models.planet import Planet
from chewy.models.film import Film
from chewy.models.species import Species
from chewy.models.transport import Vehicle, Starship


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


# Function to save a page in the database
def save_page(model, act_page):
    DB_objects = model.objects.all()  # take the objects of the actual model
    act_object = model  # create an object of this model

    fields = act_page[0].keys()
    for elem in act_page:  # take the elements of the actual page
        for field in fields:  # take each field of the actual model
            if is_an_url(elem[field]):
                if isinstance(elem[field], list):
                    for e in elem[field]:
                        act_object.field.append(e.split("/")[-2])
                else:
                    act_object.field = elem[field].split("/")[-2]
            else:
                act_object.field = elem[field]

        if not DB_objects.filter(name=act_object.name).exists():
            act_object.save()
            # If the object is not in the database then save it
        act_object = model


my_models = {
    "people": People,
    "planets": Planet,
    "films": Film,
    "species": Species,
    "vehicles": Vehicle,
    "starships": Starship,
}
# Take all the objects saved in our database

response = secure_request("https://swapi.co/api/")
# API connection

urls = []
dic = response.json()
for key in dic:
    urls.append(dic[key])
# We take all the urls on the API that we are going to manage


for elem in urls:  # every url on the api
    model = elem.split("/")[-2]  # take the string of the model e.g(people)
    actual_model = my_models[model]  # take the actual model to manage e.g(People)
    resp = secure_request(elem).json()  # make a request to the page of the model
    next_page = resp["next"]  # take the next page of the actual model
    # First of all I've to save the first page, bc it couldn't have more than 1 page
    save_page(model=actual_model, act_page=resp["results"])
    while next_page != "null":
        # Now I have to iterate the rest of the pages
        r = secure_request(next_page).json()
        save_page(model=actual_model, act_page=next_page)
        next_page = r["next"]
