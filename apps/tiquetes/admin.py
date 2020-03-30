from django.contrib import admin
from apps.tiquetes.models import Multiplex,Pelicula,Horario,Sala,Proyeccion

# Register your models here.
admin.site.register(Multiplex)
admin.site.register(Pelicula)
admin.site.register(Horario)
admin.site.register(Sala)
admin.site.register(Proyeccion)