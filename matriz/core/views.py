from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from django.views.generic.list import ListView, MultipleObjectMixin
from django.views.generic.detail import DetailView
from .forms import  GuardiaEspecialistaForm
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse



now = timezone.now()
# Create your views here.


# Vista para la pagina Home y ordenar productos en la portada

class HomePageView(TemplateView):
    template_name = "core/base.html"


class CategoriaListView(ListView):
    template_name = "core/index.html"
    model = Categoria

    def get_queryset(self):
        object_list = Categoria.objects.all()
        queryset = self.request.GET.get('search')
        if queryset:
            object_list = Categoria.objects.filter(
                Q(name__icontains=queryset)
            ).distinct()
        return object_list


class CategoriaDetail(DetailView, MultipleObjectMixin):
    template_name = "core/empresa.html"
    model = Categoria

    def get_context_data(self, **kwargs):
        object_list = Empresa.objects.filter(categoria_id=self.object.id)
        context = super(CategoriaDetail, self).get_context_data(object_list=object_list, **kwargs)
        queryset = self.request.GET.get('search')
        if queryset:
            object_list = Empresa.objects.filter(categoria_id=self.object.id).filter(
                Q(name__icontains=queryset)
            ).distinct()
            context = super(CategoriaDetail, self).get_context_data(object_list=object_list, **kwargs)

        return context




class TablaDetail(DetailView):
    template_name = "core/tabla.html"
    model = Empresa


    def get_context_data(self, **kwargs):
        object_list = TablaEscalacion.objects.filter(empresa_id=self.object.id)
        context = super(TablaDetail, self).get_context_data(object_list=object_list, **kwargs)
        return context



class GuardiaListView(ListView):
    template_name = "core/guardia_list.html"
    model = Guardia

    def get_queryset(self):
        object_list = Guardia.objects.all()
        queryset = self.request.GET.get('search')
        if queryset:
            object_list = Guardia.objects.filter(
                Q(name__icontains=queryset)
            ).distinct()
        return object_list


class GuardiaDetail(DetailView):
    template_name = "core/guardia_detail.html"
    model = Guardia

    def get_context_data(self, **kwargs):
        object_list = GuardiaEspecialista.objects.filter(guardia_id=self.object.id).filter(fecha_inicio__lte=now).filter(fecha_fin__gte=now)
        context = super(GuardiaDetail, self).get_context_data(object_list=object_list, **kwargs)

        queryset = self.request.GET.get('search')
        if queryset:
            object_list =GuardiaEspecialista.objects.filter(guardia__id=self.object.id).filter(fecha_inicio__lte=now).filter(fecha_fin__gte=now).filter(
                Q(name__name__icontains=queryset)
            ).distinct()
            context = super(GuardiaDetail, self).get_context_data(object_list=object_list, **kwargs)

        return context


class GuardiaSemanalCreate(CreateView):
    model = GuardiaEspecialista
    form_class = GuardiaEspecialistaForm
    template_name = "core/guardia_Semanal.html"

    def get_success_url(self):
        return reverse_lazy('core:guardiaSemanal_create') + "?ok"



class GuardiasEspecialistasListView(ListView):
    template_name = "core/guardias_especialidades_list.html"
    model = GuardiaEspecialista
    paginate_by = 4

    def get_context_data(self, **kwargs):
        object_list = GuardiaEspecialista.objects.filter(id=self.request.user.get_user.id)
        context = super(GuardiasEspecialistasListView, self).get_context_data(object_list=object_list, **kwargs)
        return context



class GuardiasEspecialistasUpdateView(UpdateView):
    template_name = "core/guardias_especialidades_update.html"
    model = GuardiaEspecialista
    #fields = ['imagen','fecha_inicio','fecha_fin','guardia']
    form_class = GuardiaEspecialistaForm


    def get_success_url(self):
        return reverse_lazy('core:guardias_especialistas_update', args=[self.object.id]) + "?ok"






class GuardiasEspecialistasDeleteView(DeleteView):
    template_name = "core/guardias_especialidades_delete.html"
    model = GuardiaEspecialista
    success_url = reverse_lazy('core:guardias_especialistas_list')







