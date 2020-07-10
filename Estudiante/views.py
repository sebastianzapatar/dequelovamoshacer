from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from Estudiante.models import Estudiante, Profesor
from .forms import EstudianteForm, ProfesorForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
class ListEstudiantes(LoginRequiredMixin,generic.ListView):#ListView nos hace el select * from Estudiante
    model=Estudiante
    template_name="listar_estudiantes.html"
    context_object_name="obj"
    login_url="home:login"
class InsertarEstudiante(LoginRequiredMixin,generic.CreateView):#CreateView hace el insert into estu..
    model=Estudiante
    template_name="estudiante_form.html"
    form_class=EstudianteForm
    success_url=reverse_lazy("estudiantes:listar_estudiantes")
    login_url="home:login"
class EditarEstudiante(LoginRequiredMixin,generic.UpdateView):#UpdateView hace el update into estu..
    model=Estudiante
    template_name="estudiante_form.html"
    form_class=EstudianteForm
    success_url=reverse_lazy("estudiantes:listar_estudiantes")
    login_url="home:login"
class BorrarEstudiante(LoginRequiredMixin,generic.DeleteView):#Delete from Estudiante where...
    model=Estudiante
    template_name="borrar_estudiante.html"
    context_object_name="obj"
    success_url=reverse_lazy("estudiantes:listar_estudiantes")
    login_url="home:login"


# Las vistas de los profesores

class InsertarProfesor(LoginRequiredMixin,generic.CreateView):#CreateView hace el insert into estu..
    model=Profesor
    template_name="insertar_profesor.html"
    form_class=ProfesorForm
    success_url=reverse_lazy("estudiantes:listar_profesores")#Cambiar a listar profesores
    login_url="home:login"
class ListProfesores(LoginRequiredMixin,generic.ListView):#ListView nos hace el select * from Estudiante
    model=Profesor
    template_name="listar_profesores.html"
    context_object_name="profe"
    login_url="home:login"
class EditarProfesor(LoginRequiredMixin,generic.UpdateView):#UpdateView hace el update into estu..
    model=Profesor
    template_name="insertar_profesor.html"
    form_class=ProfesorForm
    success_url=reverse_lazy("estudiantes:listar_profesores")
    login_url="home:login"
class BorrarProfesor(LoginRequiredMixin,generic.DeleteView):#Delete from Estudiante where...
    model=Profesor
    template_name="borrar_profesor.html"
    context_object_name="profe"
    success_url=reverse_lazy("estudiantes:listar_profesores")
    login_url="home:login"
def profesor_print(self, pk=None):
    import io
    from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import Table

    response = HttpResponse(content_type='application/pdf')
    buff = io.BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
    profesores = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado de Profesores", styles['Heading1'])
    profesores.append(header)
    headings = ('Id',  'nombres', 'Apellidos','cedulas')
    if not pk:
        todosprofesores = [(p.id, p.nombres, p.apellidos,p.cedula)
                           for p in Profesor.objects.all().order_by('pk')]
    else:
        todosprofesores = [(p.id, p.nombres, p.apellidos,p.cedula)
                           for p in Profesor.objects.filter(id=pk)]
    
    t = Table([headings] + todosprofesores)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
    ))

    profesores.append(t)
    doc.build(profesores)
    response.write(buff.getvalue())
    buff.close()
    return response