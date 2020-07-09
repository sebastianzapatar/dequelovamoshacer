from django.contrib import admin
from django.urls import include, path
from Estudiante.views import ListEstudiantes, InsertarEstudiante
from Estudiante.views import EditarEstudiante, BorrarEstudiante
urlpatterns=[
    path('estudiantes',ListEstudiantes.as_view(),name='listar_estudiantes'),
    path('estudiantes/new',InsertarEstudiante.as_view(),name='insertar_estudiante'),
    path('estudiantes/edit/<int:pk>',EditarEstudiante.as_view(),name='editar_estudiante'),
    path('estudiantes/delete/<int:pk>',BorrarEstudiante.as_view(),name='eliminar_estudiante'),
]