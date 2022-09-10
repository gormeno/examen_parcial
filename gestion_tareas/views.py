from asyncio import as_completed
from datetime import datetime
from xmlrpc.client import DateTime
from django.shortcuts import render
from http.client import HTTPResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import tarea, usuarios_app
from dateutil.parser import parse

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

        if usuario_registrado == 1:
            #Actualización de estados de tareas
            tareas_actualizar = tarea.objects.filter(responsable=emailUsuario) #extraer las tareas en progreso
            for cadaTarea in tareas_actualizar:
                #fecha_f = datetime.strptime(cadaTarea.fecha_entrega,'%Y-%m-%d').date()
                fecha_f = cadaTarea.fecha_entrega
                fecha_i = datetime.today().date()
                delta = (fecha_f - fecha_i).days
                #delta = abs(cadaTarea.fecha_entrega - datetime.date.today).days
                if delta < 2:
                    cadaTarea.estado = "FINALIZANDO"
                    cadaTarea.save()
            
            tareas_finalizando = tarea.objects.filter(responsable=emailUsuario,estado="FINALIZANDO") #extraer todas las tareas del usuarios finalizando
            for cadaTarea in tareas_finalizando:
                fecha_ent = cadaTarea.fecha_entrega
                fecha_hoy = datetime.today().date()
                delta = (fecha_hoy - fecha_ent).days
                if delta >= 1:
                    cadaTarea.estado = "PENDIENTE"
            #FIn de actualización de estados

            return HttpResponseRedirect(reverse('gestion_tareas:dashboard', kwargs={'responsable' : emailUsuario}))
        else:
            return render(request,'gestion_tareas/ingresar.html',{
                'mensaje_error':'Los datos ingresados son incorrectos',
            })         
    return render(request,'gestion_tareas/ingresar.html')

def dashboard(request,responsable):
    #filtrar tareas del usuario logueado
    lista_tareas = tarea.objects.filter(responsable=responsable)
    lista_tareas = lista_tareas.exclude(estado='ELIMINADO')
    if request.method == 'POST':        
        # filtro de fechas
        fecha_inicio = request.POST.get("fecha_inicio")
        fecha_fin = request.POST.get("fecha_fin")
        if fecha_inicio != "" and fecha_fin != "":
            lista_tareas = tarea.objects.filter(fecha_cracion__range=[fecha_inicio,fecha_fin],responsable=responsable)
            lista_tareas = lista_tareas.exclude(estado='ELIMINADO')
        return render(request,'gestion_tareas/dashboard.html',{
            'lista_tareas':lista_tareas,
            'responsable':responsable 
        })
    #filtrar finalizado
    return render(request,'gestion_tareas/dashboard.html',{
        'lista_tareas':lista_tareas,
        'responsable':responsable 
    })

def detalle_tarea(request,ind):
    tarea_editar = tarea.objects.get(id=ind)
    return render(request,'gestion_tareas/detalle_tarea.html',{
        'tarea':tarea_editar
    })

def editar_tarea(request,ind):
    tarea_editar = tarea.objects.get(id=ind)
    fecha_defecto = str(tarea_editar.fecha_entrega)
    fecha_minima = str(datetime.today().date())

    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        fecha_entrega = request.POST.get('fecha_entrega')
        fecha_entrega = parse(fecha_entrega)
        tarea_editar.descripcion = descripcion
        tarea_editar.fecha_entrega = fecha_entrega
        tarea_editar.save()
        lista_tareas = tarea.objects.filter(responsable=tarea_editar.responsable)
        lista_tareas = lista_tareas.exclude(estado='ELIMINADO')
        return render(request,'gestion_tareas/dashboard.html',{
            'lista_tareas':lista_tareas,
            'responsable':tarea_editar.responsable  
    })
    return render(request,'gestion_tareas/editar_tarea.html',{
        'tarea':tarea_editar,
        'fecha_defecto':fecha_defecto,
        'fecha_minima':fecha_minima
#        'lista_tareas':tarea.objects.all() 
    })

def crear_tarea(request,responsable):
    fecha_minima = str(datetime.today().date())
    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        fecha_entrega = request.POST.get('fecha_entrega')
        fecha_entrega = parse(fecha_entrega)
        tarea(descripcion=descripcion,fecha_entrega=fecha_entrega,responsable=responsable).save()
        lista_tareas = tarea.objects.filter(responsable=responsable)
        lista_tareas = lista_tareas.exclude(estado='ELIMINADO')
        return render(request,'gestion_tareas/dashboard.html',{
            'lista_tareas':lista_tareas,
            'responsable':responsable
    })
    return render(request,'gestion_tareas/crear_tarea.html',{
        'responsable':responsable,
        'fecha_minima':fecha_minima 
    })      

def eliminar_tarea(request,ind): #solo eliminación lógica
    tarea_eliminar = tarea.objects.get(id=ind)
    tarea_eliminar.estado = "ELIMINADO"
    tarea_eliminar.save()
    lista_tareas = tarea.objects.filter(responsable=tarea_eliminar.responsable)
    lista_tareas = lista_tareas.exclude(estado='ELIMINADO')
    return render(request,'gestion_tareas/dashboard.html',{
        'lista_tareas':lista_tareas,
        'responsable':tarea_eliminar.responsable    
    })      

def finalizar_tarea(request,ind):
    tarea_eliminar = tarea.objects.get(id=ind)
    tarea_eliminar.estado = "FINALIZADO"
    tarea_eliminar.save()
    lista_tareas = tarea.objects.filter(responsable=tarea_eliminar.responsable)
    lista_tareas = lista_tareas.exclude(estado='ELIMINADO')
    return render(request,'gestion_tareas/dashboard.html',{
        'lista_tareas':lista_tareas,
        'responsable':tarea_eliminar.responsable    
    })          