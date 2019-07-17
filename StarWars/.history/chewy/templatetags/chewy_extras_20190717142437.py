import os
from django import template


register = template.Library()


def image_exists(value):
    # value = model/id.jpg
    return os.path.isfile(
        "chewy/static/media/images/" + value
    )  # True default_storage.exists("chewy/static/media/images/" + value)
