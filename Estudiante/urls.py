from django.contrib import admin
from django.urls import include, path
from Estudiante.views import ListEstudiantes, InsertarEstudiante
from Estudiante.views import EditarEstudiante, BorrarEstudiante, InsertarProfesor
from .views import ListProfesores,EditarProfesor, BorrarProfesor,profesor_print
urlpatterns=[
    #Acá van las operaciones de los estudiantes
    path('estudiantes',ListEstudiantes.as_view(),name='listar_estudiantes'),
    path('estudiantes/new',InsertarEstudiante.as_view(),name='insertar_estudiante'),
    path('estudiantes/edit/<int:pk>',EditarEstudiante.as_view(),name='editar_estudiante'),
    path('estudiantes/delete/<int:pk>',BorrarEstudiante.as_view(),name='eliminar_estudiante'),


    #Acá van las operaciones de los profesores
    path('profesores',ListProfesores.as_view(),name='listar_profesores'),
    path('profesores/new',InsertarProfesor.as_view(),name='insertar_profesor'),
    path('profesores/edit/<int:pk>',EditarProfesor.as_view(),name='editar_profesor'),
    path('profesores/delete/<int:pk>',BorrarProfesor.as_view(),name='eliminar_profesor'),
    path('profesores/print/<int:pk>',profesor_print,name='print_one'),
     path('profesores/print',profesor_print,name='print_all'),
]