from django.db import models
from chewy.models.film import Film
from .my_datetime import DateTimeModel


class Historic(DateTimeModel):
    film = models.ForeignKey(Film, related_name="film", on_delete=models.SET_NULL)
    search_date = models.DateTimeField(auto_now_add=True)
