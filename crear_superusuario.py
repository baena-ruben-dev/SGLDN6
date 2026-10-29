import os
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Definir los datos del usuario que querés usar en la nube
USERNAME = 'admin'
EMAIL = 'admin@escuela.com'
PASSWORD = 'demo123'  # Cambiala por la contraseña que prefieras

if not User.objects.filter(username=USERNAME).exists():
    User.objects.create_superuser(username=USERNAME, email=EMAIL, password=PASSWORD)
    print(f" Superusuario '{USERNAME}' creado con éxito.")
else:
    print(f" El usuario '{USERNAME}' ya existe.")