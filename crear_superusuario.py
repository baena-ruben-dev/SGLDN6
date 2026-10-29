import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

USERNAME = 'admin'
EMAIL = 'admin@escuela.com'
PASSWORD = 'adminpassword123'

try:
    user, created = User.objects.get_or_create(username=USERNAME, defaults={'email': EMAIL})
    user.set_password(PASSWORD)
    user.is_superuser = True
    user.is_staff = True
    user.save()
    if created:
        print(f"Superusuario '{USERNAME}' creado con éxito.")
    else:
        print(f"Superusuario '{USERNAME}' ya existía, contraseña actualizada correctamente.")
except Exception as e:
    print(f"Aviso al configurar superusuario: {e}")