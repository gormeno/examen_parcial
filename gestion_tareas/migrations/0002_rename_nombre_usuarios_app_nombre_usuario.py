# Generated by Django 4.1 on 2022-09-06 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_tareas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuarios_app',
            old_name='nombre',
            new_name='nombre_usuario',
        ),
    ]
