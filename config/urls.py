from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.conf.urls.static import static
from legajos.models import Docente, Documento

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Estadísticas clave para el SGLD
        context['total_docentes'] = Docente.objects.count()
        context['docentes_activos'] = Docente.objects.filter(estado='ACTIVO').count()
        context['docentes_revision'] = Docente.objects.filter(estado='EN_REVISION').count()
        context['docentes_inactivos'] = Docente.objects.filter(estado='INACTIVO').count()
        context['total_documentos'] = Documento.objects.count()
        return context

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cuentas/', include('cuentas.urls')),  # Agregamos el prefijo 'cuentas/' aquí
    path('legajos/', include('legajos.urls')),
    path('', DashboardView.as_view(), name='dashboard'),  # La raíz queda para el Dashboard
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # Agregamos esta línea para que los archivos estáticos se sirvan correctamente también
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)