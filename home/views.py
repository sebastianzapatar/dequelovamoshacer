from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
# Create your views here.
class Home1(generic.View):
    def get(self,request,*args,**kwargs):
        return HttpResponse('Seguimos en el fin del mundo y con trabajo gratis pobre Carlos :P')
class Home(LoginRequiredMixin,generic.TemplateView):
    template_name="base/home.html"
    login_url="home:login"
class RegistroUsuario(generic.CreateView):
    model=User
    template_name="base/registrar.html"
    form_class=UserCreationForm
    success_url=reverse_lazy("estudiantes:listar_estudiantes")