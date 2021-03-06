from django.contrib import admin
from django.urls import include, path
from home.views import Home,RegistroUsuario
from django.contrib.auth import views as authviews #vistas para autorizar al usuario
urlpatterns=[
    path('',Home.as_view(),name='home'),
    
    path('login/', authviews.LoginView.as_view(template_name="base/login.html"),name="login"),#Sin decorador
    path('accounts/login/', authviews.LoginView.as_view(template_name="base/login.html"),name="login"),#Con decorador
    path('logout/',authviews.LogoutView.as_view(template_name='base/login.html'),name='logout'),
    
]