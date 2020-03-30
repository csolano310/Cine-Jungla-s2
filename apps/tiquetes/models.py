from django.db import models
import uuid
from datetime import date
# Create your models here.

class Multiplex(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    nombre = models.CharField(max_length=50)
    numero_salas = models.IntegerField()

    def __str__(self):
        
        return '{0}{1}{2}'.format(self.id, self.nombre, self.numero_salas)


class Pelicula(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    nom_pelicula = models.CharField(max_length = 30)
    duracion_pelicula = models.CharField(max_length=30)
    CLASIFICACION = (
        ('AA','PUBLICO INFANTIL'),
        ('A','TODO PUBLICO'),
        ('B','ADOLESCENTES DE 12'),
        ('B15','ADOLESCENTES DE 15'),
        ('C', 'ADULTOS 18 AÑOS'),
        ('D', 'ADULTOS')
    )
    clasificacion = models.CharField(max_length=3, choices= CLASIFICACION)
    imagen_pelicula = models.ImageField()

    def __str__(self):

        return '{0}{1}{2}{3}{4}'.format(self.id,self.nom_pelicula,self.duracion_pelicula,self.clasificacion,self.imagen_pelicula)


class Sala(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    cant_sillas = models.IntegerField()
    cod_multi = models.ForeignKey('Multiplex',on_delete = models.CASCADE)
    num_sala = models.IntegerField()

    def __str__(self):

        return '{0}{1}{2}{3}'.format(self.id,self.cant_sillas,self.cod_multi,self.num_sala)

class Horario(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    hora = models.TimeField()
    fecha = models.DateField()

    def __str__(self):
        return '{0}{1}{2}'.format(self.id,self.hora,self.fecha)

class Proyeccion(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    cod_sala = models.ForeignKey('Sala', on_delete = models.SET_NULL, null=True)
    cod_horario = models.ForeignKey('Horario',on_delete = models.SET_NULL, null=True)
    cod_pelicula = models.ForeignKey('Pelicula',on_delete = models.SET_NULL,null=True)

    def __str__(self):

        return '{0}{1}{2}{3}'.format(self.id,self.cod_sala,self.cod_horario,self.cod_pelicula)
        
