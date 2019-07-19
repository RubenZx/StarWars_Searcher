import os
from django import template
from django.template.defaultfilters import stringfilter
from chewy.models.film import Film
from chewy.models.people import People
from chewy.models.planet import Planet
from chewy.models.species import Species
from chewy.models.transport import Starship, Vehicle

register = template.Library()

MODELS = {
    "planets": Planet,
    "characters": People,
    "starships": Starship,
    "vehicles": Vehicle,
    "species": Species,
    "films": Film,
}


@register.filter
@stringfilter
def image_exists(image, value):
    # value = model/id.jpg
    return os.path.isfile("chewy/static/media/images/" + value + image + ".jpg")


@register.filter
def get_name(path):
    p_split = path.split("/")
    if p_split[0] == "" and p_split[1] == "":
        name = "Home"  # home page option
    elif len(p_split) == 2:
        name = p_split[-1].capitalize()  # model_name
    elif len(p_split) == 3:
        if p_split[-1][3:] == "":
            name = "Result doesn't found"  # empty search
        else:
            name = p_split[-1][3:]  # search_bar option
    else:
        model = None
        if p_split[1] in MODELS:
            model = MODELS[p_split[1]]
            id_ = p_split[2]
        if model == Film:
            name = model.objects.get(id=id_).title
        elif model != None:
            name = model.objects.get(id=id_).name
        else:
            name = "Error"
    return name
