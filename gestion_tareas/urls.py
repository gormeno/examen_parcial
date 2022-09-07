from . import views
from django.urls import path

app_name = 'gestion_tareas'

urlpatterns = [
    path('ingresar',views.ingresar,name='ingresar'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('detalle_tarea/<str:ind>',views.detalle_tarea,name='detalle_tarea'),
    path('editar_tarea/<str:ind>',views.editar_tarea,name='editar_tarea')
]