from . import views
from django.urls import path

app_name = 'gestion_tareas'

urlpatterns = [
    path('ingresar',views.ingresar,name='ingresar'),
    path('dashboard/<str:responsable>',views.dashboard,name='dashboard'),
    path('detalle_tarea/<str:ind>',views.detalle_tarea,name='detalle_tarea'),
    path('editar_tarea/<str:ind>',views.editar_tarea,name='editar_tarea'),
    path('crear_tarea/<str:responsable>',views.crear_tarea,name='crear_tarea'),
    path('eliminar_tarea/<str:ind>',views.eliminar_tarea,name='eliminar_tarea'),
    path('finalizar_tarea/<str:ind>',views.finalizar_tarea,name='finalizar_tarea')
]