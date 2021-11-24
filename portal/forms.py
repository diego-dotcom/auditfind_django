from django import forms
from .models import Articulo, Autor
from django.forms.widgets import Textarea


class FormArticulo(forms.ModelForm):
    #campos del modelo
    class Meta:
        model = Articulo
        fields = ('seccion', 'titulo', 'copete', 'texto', 'imagen', 'fecha_publicacion')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'prod_titulo'}),
            'copete': forms.Textarea(attrs={'class': 'prod_copete'}),
            'texto': forms.Textarea(attrs={'class': 'prod_texto'}),
            'imagen': forms.FileInput(attrs={'name':'imagen_adjunta', 'class': 'articulo_imagen'}),
            'fecha_publicacion': forms.SelectDateWidget(attrs={'class': 'prod_fecha_publicacion'}),     
        }

class FormAutor(forms.ModelForm):
    #campos del modelo
    class Meta:
        model = Autor
        fields = ('usuario', 'nombre', 'bio', 'foto', 'link_linkedin', 'link_twitter')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'autor_nombre'}),
            'bio': forms.Textarea(attrs={'class': 'autor_bio'}),
            'foto': forms.FileInput(attrs={'name':'imagen_adjunta', 'class': 'autor_imagen'}), 
            'link_linkedin': forms.TextInput(attrs={'class': 'autor_linkedin'}),
            'link_twitter': forms.TextInput(attrs={'class': 'autor_twitter'}),
        }


class FormContacto(forms.Form):
    nombre=forms.CharField(label="Nombre",required=True)
    mail=forms.CharField(label="Email",required=True)
    consulta=forms.CharField(label="Consulta",required=True, widget=forms.Textarea)