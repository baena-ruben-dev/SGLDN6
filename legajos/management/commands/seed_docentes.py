from django.core.management.base import BaseCommand
from legajos.models import Docente

class Command(BaseCommand):
    help = 'Crea docentes de demostración para el sistema SGLD'

    def handle(self, *args, **options):
        self.stdout.write("Creando docentes de prueba...")

        docentes_data = [
            {
                'nombre': 'Ruben Orlando',
                'apellido': 'Baena',
                'tipo_documento': 'DNI',
                'numero_documento': '28456789',
                'cuil': '20-28456789-3',
                'email': 'ruben.baena@institucion.edu.ar',
                'telefono': '1145678910',
                'fecha_nacimiento': '1989-12-21',
                'estado': 'ACTIVO'
            },
            {
                'nombre': 'Christian',
                'apellido': 'Cardenas',
                'tipo_documento': 'DNI',
                'numero_documento': '32123456',
                'cuil': '27-32123456-4',
                'email': 'chris.cardenas@institucion.edu.ar',
                'telefono': '1198765432',
                'fecha_nacimiento': '1985-09-20',
                'estado': 'ACTIVO'
            },
            {
                'nombre': 'Daniel',
                'apellido': 'Cori',
                'tipo_documento': 'DNI',
                'numero_documento': '25987456',
                'cuil': '20-25987456-1',
                'email': 'daniel.cori@institucion.edu.ar',
                'telefono': '1155443322',
                'fecha_nacimiento': '1975-02-15',
                'estado': 'EN_REVISION'
            },
        ]

        for data in docentes_data:
            docente, created = Docente.objects.get_or_create(
                numero_documento=data['numero_documento'],
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Docente creado: {docente.apellido}, {docente.nombre}"))
            else:
                self.stdout.write(f"El docente con DNI {data['numero_documento']} ya existía.")

        self.stdout.write(self.style.SUCCESS("¡Seed de docentes completado con éxito!"))