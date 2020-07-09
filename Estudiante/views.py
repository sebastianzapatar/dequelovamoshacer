from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from Estudiante.models import Estudiante
from .forms import EstudianteForm
# Create your views here.
class ListEstudiantes(generic.ListView):#ListView nos hace el select * from Estudiante
    model=Estudiante
    template_name="listar_estudiantes.html"
    context_object_name="obj"
class InsertarEstudiante(generic.CreateView):#CreateView hace el insert into estu..
    model=Estudiante
    template_name="estudiante_form.html"
    form_class=EstudianteForm
    success_url=reverse_lazy("estudiantes:listar_estudiantes")
class EditarEstudiante(generic.UpdateView):#UpdateView hace el update into estu..
    model=Estudiante
    template_name="estudiante_form.html"
    form_class=EstudianteForm
    success_url=reverse_lazy("estudiantes:listar_estudiantes")
class BorrarEstudiante(generic.DeleteView):#Delete from Estudiante where...
    model=Estudiante
    template_name="borrar_estudiante.html"
    context_object_name="obj"
    success_url=reverse_lazy("estudiantes:listar_estudiantes")

