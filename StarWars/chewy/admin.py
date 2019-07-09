from django.contrib import admin
from .models.people import People
from .models.film import Film
from .models.planet import Planet
from .models.transport import Starship, Vehicle
from .models.species import Species


admin.site.register(People)
admin.site.register(Film)
admin.site.register(Planet)
admin.site.register(Starship)
admin.site.register(Vehicle)
admin.site.register(Species)
