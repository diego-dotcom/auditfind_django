from .models import Seccion  
from datetime import datetime

def secciones(request):
    lista_secciones = Seccion.objects.all()
    return {'lista_secciones': lista_secciones}

def fecha(request):
    hoy = datetime.today()
    meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    dias_de_la_semana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")
    dia_de_la_semana = dias_de_la_semana[hoy.weekday()]
    dia = hoy.day
    mes = meses[hoy.month - 1]
    anio = hoy.year
    fecha = f"{dia_de_la_semana}, {dia} de {mes} de {anio}"
    return {'fecha': fecha}

