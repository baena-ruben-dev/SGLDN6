import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

USERNAME = 'admin@escuela.com'
EMAIL = 'admin@escuela.com'
PASSWORD = 'adminpassword123'

# Si el usuario ya existe, lo eliminamos para crearlo limpio y con la contraseña bien encriptada
if User.objects.filter(username=USERNAME).exists():
    User.objects.filter(username=USERNAME).delete()

# Creamos el superusuario oficial de Django
User.objects.create_superuser(username=USERNAME, email=EMAIL, password=PASSWORD)
print(f"Superusuario '{USERNAME}' creado y blanqueado con éxito.")