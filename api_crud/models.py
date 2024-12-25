from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
# Create your models here.
class usuario(AbstractBaseUser):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nombre} - {self.apellido}'
