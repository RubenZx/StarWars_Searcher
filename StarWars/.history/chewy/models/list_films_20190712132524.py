from django.db import models
from .my_datetime import DateTimeModel
from .film import Film


class films_list(DateTimeModel):
    film = models.ForeignKey(Film, related_name="film")

