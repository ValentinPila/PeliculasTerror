from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CostumUser(AbstractUser):
    Nombre = models.CharField(max_length=30)