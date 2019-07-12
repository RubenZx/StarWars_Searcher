from django.db import models
from .film import Film


class Historic(models.Model):
    film = models.ForeignKey(Film, related_name="film")
    search_date = models.DateTimeField(auto_now_add=True)
