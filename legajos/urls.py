from django.urls import path

from .views import (
    CargoCreateView,
    CargoDeleteView,
    CargoUpdateView,
    DocenteCreateView,
    DocenteDetailView,
    DocenteListView,
    DocenteUpdateView,
    DocumentoCreateView,
    DocumentoDeleteView,
    exportar_legajo_pdf,
)

#app_name = 'legajos'

urlpatterns = [
    path('', DocenteListView.as_view(), name='docente_list'),
    path('nuevo/', DocenteCreateView.as_view(), name='docente_create'),
    path('<int:pk>/', DocenteDetailView.as_view(), name='docente_detail'),
    path('<int:pk>/editar/', DocenteUpdateView.as_view(), name='docente_update'),
    path('<int:pk>/documento/nuevo/', DocumentoCreateView.as_view(), name='documento_create'),
    path('documento/<int:pk>/eliminar/', DocumentoDeleteView.as_view(), name='documento_delete'),
    path('<int:pk>/cargo/nuevo/', CargoCreateView.as_view(), name='cargo_create'),
    path('cargos/<int:pk>/editar/', CargoUpdateView.as_view(), name='cargo_update'),
    path('cargos/<int:pk>/eliminar/', CargoDeleteView.as_view(), name='cargo_delete'),
    path('<int:pk>/pdf/', exportar_legajo_pdf, name='exportar_legajo_pdf'),
]