from django.shortcuts import render
from http.client import HTTPResponse
from django.http import HttpResponse

# Create your views here.

def ingresar(request):
#    if request.method == 'POST':
#        nombreUsuario = request.POST.get('nombreUsuario')
#        passwordUsuario = request.POST.get('passwordUsuario')
#        #validación de información
#        #Fin validación
#        print(request)
#        print(request.POST)
#        print(nombreUsuario)
#        print(passwordUsuario)
    return render(request,'gestion_tareas/ingresar.html')

def dashboard(request):
    
    #filtrar pichangas de nuestro equipo

    #filtrar finalizado
    return render(request,'gestion_tareas/dashboard.html')

def detalle_tarea(request):
    return render(request,'gestion_tareas/detalle_tarea.html')
