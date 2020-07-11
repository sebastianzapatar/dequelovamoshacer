from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombres=models.CharField(
        max_length=40,
   
    )
    apellidos=models.CharField(
        max_length=40,
  
    )
    nombrepadre=models.CharField(
        blank=True,
        null=True,
    )
    cedula=models.IntegerField(

    )
    martriculado=models.DateField(auto_now=True)#Cada vez que cambie cambia la fecha
    creado=models.DateField(auto_now_add=True)#Solo se cambia cuando se inserta
    activo=models.BooleanField(default=True) 
    def __str__(self): #opcionales 
        return self.nombres + " " + self.apellidos
    def save(self): #opcional poner en todo en mayuscula, agregar cosas
        self.nombres=self.nombres.upper()
        self.apellidos=self.apellidos.upper()
        super(Estudiante,self).save()
    class Meta: #Obligatorio
        verbose_name_plural="Estudiantes"
class Profesor(models.Model):
    nombres=models.CharField(
        max_length=40,
 
    )
    apellidos=models.CharField(
        max_length=40,
  
    )
    cedula=models.IntegerField(

    )
    estudiante=models.ForeignKey(
        Estudiante,
        on_delete=models.CASCADE
    )
    def __str__(self): #opcionales 
        return '{}:{}'.format(Profesor, self.nombres,self.apellidos)
    def save(self): #opcional poner en todo en mayuscula, agregar cosas
        self.nombres=self.nombres.upper()
        self.apellidos=self.apellidos.upper()
        super(Profesor,self).save()
    class Meta: #Obligatorio
        verbose_name_plural="Profesores"
class EstudianteXProfesor(models.Model):
    profesor=models.ForeignKey(
       Profesor,
       on_delete=models.CASCADE 
    )
    estudiante=models.ForeignKey(
       Estudiante,
       on_delete=models.CASCADE 
    )