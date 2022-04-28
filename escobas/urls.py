from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto', views.contacto, name='contacto'),
    path('logueo', views.logueo, name='logueo'),
    path('panel', views.panel, name='panel'),
    path('cerrar_sesion', views.cerrar_sesion, name='cerrar_sesion'),
    path('contacto/mensaje_enviado', views.creando_mensaje, name="creando_mensaje"),
    path('panel/borrando_mensaje/<int:id_mensaje>', views.borrando_mensaje, name="borrando_mensaje"),
]
