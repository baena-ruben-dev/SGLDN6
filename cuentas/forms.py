from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Cambiamos la etiqueta del campo username para que pida el email institucional
        self.fields['username'].label = 'Email institucional'
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'correo@institucion.edu.ar'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Contraseña'
        })