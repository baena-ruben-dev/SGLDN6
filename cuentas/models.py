from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El email es obligatorio")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('rol', 'SUPERADMIN')
        extra_fields.setdefault('debe_cambiar_password', False)
        return self.create_user(email, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    ROLES = [  # noqa: RUF012
        ('SUPERADMIN', 'Super Usuario / Admin'),
        ('RECTOR', 'Rector'),
        ('SECRETARIA', 'Secretaría'),
        ('PROSECRETARIO', 'Prosecretario'),
        ('ADMINISTRATIVO', 'Administrativo'),
    ]

    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rol = models.CharField(max_length=20, choices=ROLES, default='ADMINISTRATIVO')
    activo = models.BooleanField(default=True)
    debe_cambiar_password = models.BooleanField(default=True)
    ultimo_acceso = models.DateTimeField(null=True, blank=True)
    
    is_staff = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido']  # noqa: RUF012

    def __str__(self):
        return f"{self.apellido}, {self.nombre} ({self.get_rol_display()})"