# Generated by Django 4.1.3 on 2022-11-05 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Descripcion', models.TextField(max_length=400)),
                ('Rating', models.CharField(max_length=2)),
                ('FechaPublicacion', models.DateField(max_length=50)),
            ],
        ),
    ]
