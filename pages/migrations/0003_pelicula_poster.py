# Generated by Django 4.1.3 on 2022-11-24 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_pelicula_fechapublicacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='Poster',
            field=models.ImageField(blank=True, upload_to='poster/'),
        ),
    ]