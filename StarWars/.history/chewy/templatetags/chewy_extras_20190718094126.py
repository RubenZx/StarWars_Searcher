import os
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@stringfilter
def image_exists(value):
    # value = model/id.jpg
    return os.path.isfile("chewy/static/media/images/" + value)
