from django.db import models
from django.urls import reverse

# Create your models here.

class Pelicula(models.Model):
    Nombre = models.CharField(max_length=50)
    Descripcion = models.TextField(max_length=400)
    Rating = models.CharField(max_length=2)
    FechaPublicacion = models.DateField()
    Poster = models.ImageField(upload_to='poster/', blank=True)
    Precio = models.IntegerField(blank=True)

    def __str__(self):
        return self.Nombre[:25]

    def get_absolute_url(self):
        #return reverse('peliculas_detalle', args=[str(self.id)])
        return reverse('peliculas')

    class Meta:
        permissions = [
            ('Admin_generico', 'Puede: Editar y Crear Peliculas'),
            ('Membresia', 'Visualizar el detalle de las peliculas')
        ]

class Cine(models.Model):
    Nombre = models.CharField(max_length=50)
    Ubicacion = models.CharField(max_length=50)
    Pelicula = models.ForeignKey(Pelicula, on_delete = models.CASCADE)
    
    Epson = 'Epson'
    Canon = 'Canon'
    Generic = 'Generic'

    TipoDeProyector = [
        (Epson, 'Epson'),
        (Canon, 'Canon'),
        (Generic, 'Generic'),
    ]
    Proyector = models.CharField(max_length=10, choices=TipoDeProyector, default = 'Epson')
