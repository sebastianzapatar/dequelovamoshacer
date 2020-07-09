from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombres=models.CharField(
        max_length=40,
        help_text='Ingrese sus nombre',
    )
    apellidos=models.CharField(
        max_length=40,
        help_text='Ingrese sus apellidos',
    )
    cedula=models.IntegerField(

    )
    def __str__(self): #opcionales 
        return self.nombres + " " + self.apellidos
    def save(self): #opcional poner en todo en mayuscula, agregar cosas
        self.nombres=self.nombres.upper()
        self.apellidos=self.apellidos.upper()
        super(Estudiante,self).save()
    class Meta: #Obligatorio
        verbose_name_plural="Estudiantes"
