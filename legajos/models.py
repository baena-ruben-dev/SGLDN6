#from django.db import models

from django.db import models


class Docente(models.Model):
    TIPO_DOCUMENTO_CHOICES = [  # noqa: RUF012
        ('DNI', 'DNI'),
        ('LC', 'Libreta Cívica'),
        ('LE', 'Libreta de Enrolamiento'),
        ('PAS', 'Pasaporte'),
    ]

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    tipo_documento = models.CharField(max_length=10, choices=TIPO_DOCUMENTO_CHOICES, default='DNI')
    numero_documento = models.CharField(max_length=20, unique=True)
    cuil = models.CharField(max_length=20, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    
    # Estado del legajo institucional
    ESTADO_CHOICES = [  # noqa: RUF012
        ('ACTIVO', 'Activo'),
        ('EN_REVISION', 'En revisión'),
        ('INACTIVO', 'Inactivo'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='ACTIVO')
    
    # Metadatos de control
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre} (DNI: {self.numero_documento})"

class Documento(models.Model):
    TIPO_DOC_LEGAJO = (
        ('DNI', 'Copia DNI'),
        ('CUIL', 'Constancia CUIL'),
        ('TITULO', 'Título Universitario / Terciario'),
        ('CV', 'Curriculum Vitae'),
        ('ANTECEDENTES', 'Certificado de Antecedentes'),
        ('OTRO', 'Otro Documento'),
    )

    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, related_name='documentos')
    titulo = models.CharField(max_length=150, verbose_name="Nombre / Descripción")
    tipo = models.CharField(max_length=20, choices=TIPO_DOC_LEGAJO, default='OTRO')
    archivo = models.FileField(upload_to='documentos_legajo/')
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.docente.apellido}"

class CargoDocente(models.Model):
    TIPO_CARGO_CHOICES = [  # noqa: RUF012
        ('TC', 'Tiempo Completo (36 hs)'),
        ('TP1', 'Tiempo Parcial 1 (30 hs)'),
        ('TP2', 'Tiempo Parcial 2 (24 hs)'),
        ('TP3', 'Tiempo Parcial 3 (18 hs)'),
        ('TP4', 'Tiempo Parcial 4 (12 hs)'),
        ('PRECEPTOR', 'Preceptor / Cargo Auxiliar'),
        ('OTRO', 'Otro Cargo / Conducción'),
    ]

    CONDICION_CHOICES = [  # noqa: RUF012
        ('TITULAR', 'Titular'),
        ('INTERINO', 'Interino'),
        ('SUPLENTE', 'Suplente'),
    ]

    TURNO_CHOICES = [  # noqa: RUF012
        ('MANANA', 'Mañana'),
        ('TARDE', 'Tarde'),
        ('VESPERTINO', 'Vespertino'),
        ('NOCHE', 'Noche'),
    ]

    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, related_name='cargos')
    tipo_cargo = models.CharField(max_length=20, choices=TIPO_CARGO_CHOICES, default='TP3')
    espacio_curricular = models.CharField(max_length=150, help_text="Ej: Matemática, Economía, o Función de Preceptoría")
    horas_catedra = models.PositiveIntegerField(help_text="Cantidad de horas semanales")
    condicion = models.CharField(max_length=20, choices=CONDICION_CHOICES, default='INTERINO')
    turno = models.CharField(max_length=20, choices=TURNO_CHOICES, default='VESPERTINO')
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.get_tipo_cargo_display()} - {self.espacio_curricular} ({self.docente})"