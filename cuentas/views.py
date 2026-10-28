#from django.shortcuts import render

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import CustomAuthenticationForm

class CustomLoginView(LoginView):
    template_name = 'cuentas/login.html'
    authentication_form = CustomAuthenticationForm
    redirect_authenticated_user = True

    def get_success_url(self):
        # Por ahora lo mandamos al home o dashboard general
        return reverse_lazy('dashboard')

class CustomLogoutView(LogoutView):
    next_page = 'login'

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def dashboard(request):
    return HttpResponse(f"¡Bienvenido al sistema SGLD! Estás logueado como: {request.user.email}")