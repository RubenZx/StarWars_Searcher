from django import template


register = template.Library()


def image_exists(value):
    return default_storage.exists("chewy/static/media/images/" + value)

