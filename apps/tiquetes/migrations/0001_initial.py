# Generated by Django 3.0.4 on 2020-03-29 05:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Multiplex',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('numero_salas', models.IntegerField()),
            ],
        ),
    ]
