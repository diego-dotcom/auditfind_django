from django.db import models
from django.utils import timezone

# Create your models here.

class Seccion(models.Model):
    descripcion = models.CharField(max_length=64)

    def __str__(self):
        return self.descripcion

class Articulo(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE, related_name="seccion")
    titulo = models.CharField(max_length=100)
    copete = models.TextField()
    texto = models.TextField()
    imagen = models.FileField(upload_to='img_articulos/', blank= True)
    fecha_publicacion = models.DateField(null=False)

    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo




