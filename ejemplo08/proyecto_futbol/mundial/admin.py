from django.contrib import admin

# Register your models here.
from mundial.models import Equipo, Estadio

admin.site.register(Equipo)
admin.site.register(Estadio)
