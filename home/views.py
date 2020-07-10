from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# Create your views here.
class Home1(generic.View):
    def get(self,request,*args,**kwargs):
        return HttpResponse('Seguimos en el fin del mundo y con trabajo gratis pobre Carlos :P')
class Home(LoginRequiredMixin,generic.TemplateView):
    template_name="base/home.html"
    login_url="home:login"
