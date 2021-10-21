from django.contrib import admin
from .models import Articulo, Seccion, Autor

# Register your models here.

admin.site.register(Articulo)
admin.site.register(Seccion)
admin.site.register(Autor)