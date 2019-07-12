from .my_datetime import DateTimeModel
from .film import Film


class Historic(DateTimeModel):
    film = models.ForeignKey(Film, related_name="film")
    search_date = models.DateTimeField(auto_now_add=True)
