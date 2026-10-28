from django.core.management.base import BaseCommand
from cuentas.models import Usuario

class Command(BaseCommand):
    help = 'Crea usuarios de demostración para cada rol institucional'

    def handle(self, *args, **options):
        self.stdout.write("Creando usuarios de prueba...")

        usuarios_data = [
            {'email': 'superadmin@institucion.edu.ar', 'nombre': 'Ana', 'apellido': 'Admin', 'rol': 'SUPERADMIN'},
            {'email': 'rector@institucion.edu.ar', 'nombre': 'Carlos', 'apellido': 'Rector', 'rol': 'RECTOR'},
            {'email': 'secretaria@institucion.edu.ar', 'nombre': 'María', 'apellido': 'Secretaria', 'rol': 'SECRETARIA'},
            {'email': 'prosecretario@institucion.edu.ar', 'nombre': 'Jorge', 'apellido': 'Prosecretario', 'rol': 'PROSECRETARIO'},
            {'email': 'administrativo@institucion.edu.ar', 'nombre': 'Lucía', 'apellido': 'Administrativa', 'rol': 'ADMINISTRATIVO'},
        ]

        for data in usuarios_data:
            user, created = Usuario.objects.get_or_create(
                email=data['email'],
                defaults={
                    'nombre': data['nombre'],
                    'apellido': data['apellido'],
                    'rol': data['rol'],
                    'debe_cambiar_password': True,
                    'is_staff': data['rol'] == 'SUPERADMIN'
                }
            )
            if created:
                user.set_password('Demo12345!')
                user.save()
                self.stdout.write(self.style.SUCCESS(f"Usuario creado: {data['email']} ({data['rol']})"))
            else:
                self.stdout.write(f"El usuario {data['email']} ya existía.")

        self.stdout.write(self.style.SUCCESS("¡Seed de usuarios completado con éxito!"))