from django.shortcuts import render
from http.client import HTTPResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import tarea, usuarios_app

# Create your views here.

def ingresar(request):
    if request.method == 'POST':
        emailUsuario = request.POST.get('emailUsuario')
        passwordUsuario = request.POST.get('passwordUsuario')
        
        #validación de información
        usuario_registrado = 0
        usuarios_totales = usuarios_app.objects.all()

        for usuario in usuarios_totales:
            if usuario.nombre_usuario == emailUsuario and usuario.contrasena == passwordUsuario:
                usuario_registrado = 1
        #Fin validación

        lista_tareas = tarea.objects.all()

        if usuario_registrado == 1:
#            return HttpResponseRedirect(reverse('gestion_tareas:dashboard', kwargs={'lista_tareas' : lista_tareas}))
#            return HttpResponseRedirect(reverse('gestion_tareas:dashboard'))
            return render(request,'gestion_tareas/dashboard.html',{
                'lista_tareas':lista_tareas
            })
        else:
            return render(request,'gestion_tareas/ingresar.html',{
                'mensaje_error':'Los datos ingresados son incorrectos',
            })         
    return render(request,'gestion_tareas/ingresar.html')

#        print(request)
#        print(request.POST)
#        print(nombreUsuario)
#        print(passwordUsuario)
    #return render(request,'gestion_tareas/ingresar.html')

def dashboard(request):
    
    #filtrar pichangas de nuestro equipo

    #filtrar finalizado
    return render(request,'gestion_tareas/dashboard.html')

def detalle_tarea(request,ind):
    tarea_editar = tarea.objects.get(id=ind)
    return render(request,'gestion_tareas/detalle_tarea.html',{
        'tarea':tarea_editar
    })

def editar_tarea(request,ind):
    tarea_editar = tarea.objects.get(id=ind)
    return render(request,'gestion_tareas/editar_tarea.html',{
        'tarea':tarea_editar
    })