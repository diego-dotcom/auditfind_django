from django import forms
from .models import Articulo, Autor
from django.forms.widgets import Textarea
from django.contrib.auth.models import User


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
        fields = ('nombre', 'bio', 'foto', 'link_linkedin', 'link_twitter')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'autor_nombre'}),
            'bio': forms.Textarea(attrs={'class': 'autor_bio'}),
            'foto': forms.FileInput(attrs={'name':'imagen_adjunta', 'class': 'autor_imagen'}), 
            'link_linkedin': forms.TextInput(attrs={'class': 'autor_linkedin'}),
            'link_twitter': forms.TextInput(attrs={'class': 'autor_twitter'}),
        }


class FormContacto(forms.Form):
    nombre=forms.CharField(label="Nombre",required=True)
    email=forms.CharField(label="Email",required=True)
    consulta=forms.CharField(label="Consulta",required=True, widget=forms.Textarea)


class RegisterForm(forms.Form):
    username = forms.CharField(required=True, min_length=4, max_length=50, 
                                widget=forms.TextInput(attrs={
                                'class': 'form-control',
                                'id': 'username',
                                }))
    email = forms.EmailField(required=True,
                                widget=forms.EmailInput(attrs={
                                    'class': 'form-control',
                                    'id': 'email',
                                    'placeholder': 'example@mail.com'
                                }))
    password = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                }))
    password2 = forms.CharField(required=True, label= 'Confirmar password',
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',    
                                }))

    def clean_username(self): # siempre este nombre
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El username ya se encuentra en uso')

        return username

    def clean_email(self): # siempre este nombre
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya se encuentra en uso')

        return email

    def clean(self): # Sobreescribimos este método si y solo si necesitamos validar campor que dependan unos de otros

        cleaned_data = super().clean()

        if cleaned_data.get('password') != cleaned_data.get('password2'):
            self.add_error('password2', 'El password no coindice')

    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password'),
            )