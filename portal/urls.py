from django.urls import path
from . import views

app_name ="portal"
urlpatterns = [
    path('', views.home, name="home"),
    path('articulos', views.articulos, name="articulos"),
    path('<int:articulo_id>', views.articulo, name="articulo"),
    path('articulo_nuevo', views.articulo_nuevo, name="articulo_nuevo"),
    path('filtro_secciones/<int:seccion_id>', views.filtro_secciones, name="filtro_secciones"),
    path('busqueda', views.busqueda, name="busqueda"),
]