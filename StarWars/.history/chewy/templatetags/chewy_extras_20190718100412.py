import os
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def image_exists(image, value):
    # value = model/id.jpg
    return os.path.isfile("chewy/static/media/images/" + value + image + ".jpg")
