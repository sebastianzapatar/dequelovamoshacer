# Generated by Django 3.0.5 on 2020-07-08 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(help_text='Ingrese sus nombre', max_length=40)),
                ('apellidos', models.CharField(help_text='Ingrese sus apellidos', max_length=40)),
                ('cedula', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Estudiantes',
            },
        ),
    ]
