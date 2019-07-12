from django.db import models
from chewy.models.my_datetime import DateTimeModel
from chewy.models.people import People
from chewy.models.planet import Planet
from chewy.models.transport import Vehicle, Starship
from chewy.models.species import Species


class Film(DateTimeModel):
    """ A film """

    title = models.CharField(max_length=100)
    episode_id = models.IntegerField()
    opening_crawl = models.TextField(max_length=1000)
    director = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    release_date = models.DateField()
    characters = models.ManyToManyField(People, related_name="films", blank=True)
    planets = models.ManyToManyField(Planet, related_name="films", blank=True)
    starships = models.ManyToManyField(Starship, related_name="films", blank=True)
    vehicles = models.ManyToManyField(Vehicle, related_name="films", blank=True)
    species = models.ManyToManyField(Species, related_name="films", blank=True)

    def __unicode__(self):
        return self.title
