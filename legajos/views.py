from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from .models import Docente, Documento, CargoDocente
from .forms import DocenteForm, DocumentoForm, CargoForm

class DocenteListView(LoginRequiredMixin, ListView):
    model = Docente
    template_name = 'legajos/docente_list.html'
    context_object_name = 'docentes'

    def get_queryset(self):
        queryset = super().get_queryset()
        estado = self.request.GET.get('estado')
        if estado:
            # Manejo flexible por si el estado tiene espacio o guion bajo en la BD
            if estado == 'EN_REVISION':
                queryset = queryset.filter(estado__in=['EN_REVISION', 'EN REVISION'])
            else:
                queryset = queryset.filter(estado=estado)
        return queryset

class DocenteDetailView(LoginRequiredMixin, DetailView):
    model = Docente
    template_name = 'legajos/docente_detail.html'
    context_object_name = 'docente'

class DocenteCreateView(LoginRequiredMixin, CreateView):
    model = Docente
    form_class = DocenteForm
    template_name = 'legajos/docente_form.html'
    success_url = reverse_lazy('docente_list')

class DocenteUpdateView(LoginRequiredMixin, UpdateView):
    model = Docente
    form_class = DocenteForm
    template_name = 'legajos/docente_form.html'

    def get_success_url(self):
        return reverse('docente_detail', kwargs={'pk': self.object.pk})

class DocumentoCreateView(LoginRequiredMixin, CreateView):
    model = Documento
    form_class = DocumentoForm
    template_name = 'legajos/documento_form.html'

    def form_valid(self, form):
        docente = get_object_or_404(Docente, pk=self.kwargs['docente_id'])
        form.instance.docente = docente
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['docente'] = get_object_or_404(Docente, pk=self.kwargs['docente_id'])
        return context

    def get_success_url(self):
        return reverse('docente_detail', kwargs={'pk': self.kwargs['docente_id']})

class DocumentoDeleteView(LoginRequiredMixin, DeleteView):
    model = Documento
    template_name = 'legajos/documento_confirm_delete.html'

    def get_success_url(self):
        return reverse('docente_detail', kwargs={'pk': self.object.docente.pk})

class CargoCreateView(LoginRequiredMixin, CreateView):
    model = CargoDocente
    form_class = CargoForm
    template_name = 'legajos/cargo_form.html'

    def form_valid(self, form):
        docente = get_object_or_404(Docente, pk=self.kwargs['docente_id'])
        form.instance.docente = docente
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['docente'] = get_object_or_404(Docente, pk=self.kwargs['docente_id'])
        return context

    def get_success_url(self):
        return reverse('docente_detail', kwargs={'pk': self.kwargs['docente_id']})

class CargoUpdateView(LoginRequiredMixin, UpdateView):
    model = CargoDocente
    form_class = CargoForm
    template_name = 'legajos/cargo_form.html'

    def get_success_url(self):
        return reverse('docente_detail', kwargs={'pk': self.object.docente.pk})

class CargoDeleteView(LoginRequiredMixin, DeleteView):
    model = CargoDocente
    template_name = 'legajos/cargo_confirm_delete.html'

    def get_success_url(self):
        return reverse('docente_detail', kwargs={'pk': self.object.docente.pk})

def exportar_legajo_pdf(request, pk):
    docente = get_object_or_404(Docente, pk=pk)
    documentos = docente.documentos.all() if hasattr(docente, 'documentos') else []
    
    context = {
        'docente': docente,
        'documentos': documentos,
    }
    return render(request, 'legajos/docente_pdf.html', context)