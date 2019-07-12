from django.db import models
from .my_datetime import DateTimeModel


class films_list(DateTimeModel):
    film = models.ForeignKey(Film, related_name="film")

