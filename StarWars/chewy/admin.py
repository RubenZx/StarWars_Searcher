from django.contrib import admin

# Register your models here.
from .models import People, Film, Planet, Starship, Vehicle, Species

admin.site.register(People)
admin.site.register(Film)
admin.site.register(Planet)
admin.site.register(Starship)
admin.site.register(Vehicle)
admin.site.register(Species)
