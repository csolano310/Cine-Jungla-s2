# Generated by Django 3.0.4 on 2020-03-29 06:22

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tiquetes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('hora', models.TimeField()),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('nom_pelicula', models.CharField(max_length=30)),
                ('duracion_pelicula', models.CharField(max_length=30)),
                ('clasificacion', models.CharField(choices=[('AA', 'PUBLICO INFANTIL'), ('A', 'TODO PUBLICO'), ('B', 'ADOLESCENTES DE 12'), ('B15', 'ADOLESCENTES DE 15'), ('C', 'ADULTOS 18 AÑOS'), ('D', 'ADULTOS')], max_length=3)),
                ('imagen_pelicula', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('cant_sillas', models.IntegerField()),
                ('num_sala', models.IntegerField()),
                ('cod_multi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiquetes.Multiplex')),
            ],
        ),
        migrations.CreateModel(
            name='Proyeccion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('cod_horario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tiquetes.Horario')),
                ('cod_pelicula', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tiquetes.Pelicula')),
                ('cod_sala', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tiquetes.Sala')),
            ],
        ),
    ]
