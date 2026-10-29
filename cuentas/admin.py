from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class CustomUserAdmin(UserAdmin):
    model = Usuario
    # Definimos qué columnas se ven en la lista
    list_display = ('email', 'apellido', 'nombre', 'rol', 'is_active', 'is_staff')
    list_filter = ('rol', 'activo', 'is_staff')
    search_fields = ('email', 'nombre', 'apellido')
    ordering = ('email',)
    
    # Mapeo de campos para el formulario de edición en el admin
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Información Personal', {'fields': ('nombre', 'apellido', 'rol')}),
        ('Permisos y Estados', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nombre', 'apellido', 'rol', 'password1', 'password2', 'activo', 'is_staff')}
        ),
    )

# Registramos el modelo con su admin personalizado
admin.site.register(Usuario, CustomUserAdmin)