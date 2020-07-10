from django import forms
from .models import Estudiante, Profesor
class EstudianteForm(forms.ModelForm):#Hereda del ModelForm
    class Meta:
        model=Estudiante
        fields=['nombres','apellidos','cedula'] #Ponemos los campos que queremos insertar
        labels={'nombres':'Ingrese su nombre','apellidos':'Ingrese sus apellidos',
        'cedula':'Ingrese su cédula'}
        widget={
            'nombres':forms.TextInput(),
            'apellidos':forms.TextInput(),
            'cedula':forms.NumberInput(),
        }
        def __init__(self,*args,**kgwards):
            super().__init__(*args,**kgwards)#Recorremos los campos
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'form-control'
                })
class ProfesorForm(forms.ModelForm):
    estudiante=forms.ModelChoiceField(
        queryset=Estudiante.objects.order_by('apellidos')
    )
    class Meta:
        model=Profesor
        fields=['nombres','apellidos','cedula','estudiante']
        labels={'nombres':'Ingrese su nombre','apellidos':'Ingrese sus apellidos',
        'cedula':'Ingrese su cédula','estudiante':'seleccione al estudiante'}
        widget={
            'nombres':forms.TextInput(),
            'apellidos':forms.TextInput(),
            'cedula':forms.NumberInput(),
        }
        def __init__(self,*args,**kgwards):
            super().__init__(*args,**kgwards)#Recorremos los campos
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'form-control'
                })
           