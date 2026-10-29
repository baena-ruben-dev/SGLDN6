import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

try:
    django.setup()
    from django.contrib.auth import get_user_model

    User = get_user_model()
    EMAIL = 'admin@escuela.com'
    PASSWORD = 'adminpassword123'

    # Buscamos por email y pasamos nombre y apellido que son obligatorios en tu modelo
    user, created = User.objects.get_or_create(
        email=EMAIL,
        defaults={
            'nombre': 'Administrador',
            'apellido': 'Sistema',
            'rol': 'SUPERADMIN',
            'is_staff': True,
            'is_superuser': True,
            'debe_cambiar_password': False,
            'activo': True
        }
    )
    
    # Aseguramos la contraseña cifrada correctamente y privilegios de admin
    user.set_password(PASSWORD)
    user.is_staff = True
    user.is_superuser = True
    user.activo = True
    user.save()

    if created:
        print(f"Superusuario '{EMAIL}' creado con éxito.")
    else:
        print(f"Superusuario '{EMAIL}' ya existía, contraseña actualizada.")
        
except Exception as e:
    print(f"Error al configurar superusuario: {e}")