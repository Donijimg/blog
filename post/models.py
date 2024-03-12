from django.db import models
from datetime import date

# Create your models here.
class Autor(models.Model):
  nombre = models.CharField(max_length=200)
  correo = models.CharField(max_length=200)

  def __str__(self):
    return self.nombre

class Post(models.Model):
  id_author = models.ForeignKey(Autor, on_delete=models.CASCADE, null=True, blank=True)
  titulo = models.CharField(max_length=200)
  cuerpo = models.TextField()
  fecha = models.DateField(default= date.today)
  
  def __str__(self):
    return self.titulo
