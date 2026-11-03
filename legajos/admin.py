from django.contrib import admin

from .models import CargoDocente, Docente


@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'numero_documento', 'email', 'estado', 'created_at')
    list_filter = ('estado', 'tipo_documento')
    search_fields = ('nombre', 'apellido', 'numero_documento', 'email', 'cuil')
    ordering = ('apellido', 'nombre')

@admin.register(CargoDocente)
class CargoDocenteAdmin(admin.ModelAdmin):
    list_display = ('docente', 'tipo_cargo', 'espacio_curricular', 'horas_catedra', 'condicion', 'turno')
    search_fields = ('docente__apellido', 'docente__nombre', 'espacio_curricular')
    list_filter = ('tipo_cargo', 'condicion', 'turno')