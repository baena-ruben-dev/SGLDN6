from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('email', 'apellido', 'nombre', 'rol', 'activo', 'is_staff')
    list_filter = ('rol', 'activo', 'is_staff')
    search_fields = ('email', 'nombre', 'apellido')
    ordering = ('apellido', 'nombre')