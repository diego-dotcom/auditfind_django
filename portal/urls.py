from django.urls import path
from . import views

app_name ="portal"
urlpatterns = [
    path('', views.home, name="home"),
    path('articulos', views.articulos, name="articulos"),
    path('<int:articulo_id>', views.articulo, name="articulo"),
    path('nosotros', views.nosotros, name="nosotros"),
    path('contacto', views.contacto, name="contacto"),
    path('articulo_nuevo', views.articulo_nuevo, name="articulo_nuevo"),
    path('articulo_editar/<int:articulo_id>', views.articulo_editar, name="articulo_editar"),
    path('articulo_eliminar/<int:articulo_id>', views.articulo_eliminar, name="articulo_eliminar"),
    path('autor_editar', views.autor_editar, name="autor_editar"),
    path('filtro_secciones/<int:seccion_id>', views.filtro_secciones, name="filtro_secciones"),
    path('busqueda', views.busqueda, name="busqueda"),
]