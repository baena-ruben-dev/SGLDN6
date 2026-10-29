from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class CustomUserAdmin(UserAdmin):
    model = Usuario
    list_display = ('email', 'apellido', 'nombre', 'rol', 'activo', 'is_staff')
    list_filter = ('rol', 'activo', 'is_staff')
    search_fields = ('email', 'nombre', 'apellido')
    ordering = ('email',)
    
    readonly_fields = ('last_login',)
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Información Personal', {'fields': ('nombre', 'apellido', 'rol')}),
        ('Permisos y Estados', {'fields': ('activo', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nombre', 'apellido', 'rol', 'password1', 'password2', 'activo', 'is_staff')}
        ),
    )

admin.site.register(Usuario, CustomUserAdmin)