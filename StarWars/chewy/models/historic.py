from django.db import models
from chewy.models.film import Film


class Historic(models.Model):
    film = models.ForeignKey(Film, related_name="film", on_delete=models.PROTECT)
    search_date = models.DateTimeField(auto_now_add=True)
