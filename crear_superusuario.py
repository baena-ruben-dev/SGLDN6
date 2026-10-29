import os
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

USERNAME = 'admin'
EMAIL = 'admin@escuela.com'
PASSWORD = 'adminpassword123'

try:
    if not User.objects.filter(username=USERNAME).exists():
        User.objects.create_superuser(username=USERNAME, email=EMAIL, password=PASSWORD)
        print(f"Superusuario '{USERNAME}' creado con éxito.")
    else:
        print(f"El usuario '{USERNAME}' ya existe en la base de datos.")
except Exception as e:
    print(f"Aviso al crear superusuario: {e}")