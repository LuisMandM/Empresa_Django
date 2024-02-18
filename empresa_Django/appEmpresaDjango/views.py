from django.views.generic import ListView, DetailView, CreateView, View
from django.shortcuts import render, redirect, get_object_or_404
from appEmpresaDjango.forms import DepartamentoForm, EmpleadoForm
from appEmpresaDjango.models import *


# Create your views here.
class DepartamentoListView(ListView):
    model = Departamento


class DepartamentoDetailView(DetailView):
    model = Departamento


class DepartamentoCreateView(View):

    def get(self, request):
        formulario = DepartamentoForm()
        context = {
            'formulario': formulario
        }
        return render(request, 'appEmpresaDjango/departamento_create.html',
                      context)

    def post(self, request):
        formulario = DepartamentoForm(request.POST)
        if formulario.is_valid():
            # Opcion 1
            departamento = Departamento()
            departamento.nombre = formulario.cleaned_data['nombre']
            departamento.telefono = formulario.cleaned_data['telefono']
            departamento.save()

            # Opcion 2 Cuando no es necesario hacer ninguna transformación antes de ir a base de datos
            # (Usar datos genericos).
            # formulario.save()

            return redirect('index')
        return render(request, 'appEmpresaDjango/departamento_create.html', context={'formulario': formulario})
        # EL FORMULARIO GUARDA LOS ERRORES DE VALIDACION


class EmpleadoListView(ListView):
    model = Empleado
    context_object_name = 'empleados'

    def get_queryset(self):
        self.departamento = get_object_or_404(Departamento, pk=self.kwargs['departamento_id'])
        return Empleado.objects.filter(departamento=self.departamento)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        departamento = get_object_or_404(Departamento, pk=self.kwargs['departamento_id'])
        context['departamento'] = departamento
        return context


class EmpleadoCreateView(View):

    def get(self, request):
        formulario = EmpleadoForm()
        context = {
            'formulario': formulario
        }
        return render(request, 'appEmpresaDjango/empleado_create.html',
                      context)

    def post(self, request):
        formulario = EmpleadoForm(request.POST)
        if formulario.is_valid():
            # Opcion 1

            empleado = Empleado()
            empleado.nombre = formulario.cleaned_data['nombre']
            empleado.fecha_nacimiento = formulario.cleaned_data['fecha_nacimiento']
            empleado.apellido = formulario.cleaned_data['antiguedad']
            empleado.departamento = formulario.cleaned_data['departamento']
            empleado.hijos = formulario.cleaned_data['habilidad']
            empleado.save()

            # Opcion 2 Cuando no es necesario hacer ninguna transformación antes de ir a base de datos
            # (Usar datos genericos).
            # formulario.save()

            return redirect('index')
        return render(request, 'appEmpresaDjango/departamento_create.html', context={'formulario': formulario})
        # EL FORMULARIO GUARDA LOS ERRORES DE VALIDACION


class EmpleadoDetailView(DetailView):
    model = Empleado
