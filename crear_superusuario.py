import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

try:
    django.setup()
    from django.contrib.auth import get_user_model

    User = get_user_model()
    USERNAME = 'admin@escuela.com'
    EMAIL = 'admin@escuela.com'
    PASSWORD = 'adminpassword123'

    user, created = User.objects.get_or_create(username=USERNAME, defaults={'email': EMAIL})
    user.set_password(PASSWORD)
    user.is_superuser = True
    user.is_staff = True
    user.save()
    
    if created:
        print(f"Superusuario '{USERNAME}' creado con éxito.")
    else:
        print(f"Superusuario '{USERNAME}' ya existía, contraseña actualizada.")
        
except Exception as e:
    print(f"Aviso en script de superusuario: {e}")
    sys.exit(0)  # Evita que falle el build si ocurre un imprevisto