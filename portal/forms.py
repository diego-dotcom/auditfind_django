from django import forms
from .models import Articulo


class FormArticulo(forms.ModelForm):
    #campos del modelo
    class Meta:
        model = Articulo
        fields = ('autor', 'seccion', 'titulo', 'copete', 'texto', 'imagen', 'fecha_publicacion')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'prod_titulo'}),
            'copete': forms.Textarea(attrs={'class': 'prod_copete'}),
            'texto': forms.Textarea(attrs={'class': 'prod_texto'}),
            'imagen': forms.FileInput(attrs={'name':'imagen_adjunta', 'class': 'articulo_imagen'}),
            'fecha_publicacion': forms.SelectDateWidget(attrs={'class': 'prod_fecha_publicacion'}),     
        }