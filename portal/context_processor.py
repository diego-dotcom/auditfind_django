from .models import Seccion  

def secciones(request):
    lista_secciones = Seccion.objects.all()
    return {'lista_secciones': lista_secciones}


