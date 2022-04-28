from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from .models import Mensaje

def index(request):
    return render(request, 'index.html')

def contacto(request):
    return render(request, 'contacto.html')

@csrf_exempt
def logueo(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('panel'))
    else:
        if request.method == 'POST':
            usuario = request.POST["usuario"]
            clave = request.POST["clave"]
            persona = authenticate(username=usuario, password=clave)
            if persona is not None:
                login(request, persona)
                return HttpResponseRedirect(reverse('panel'))
            else:
                contexto = {
                    'equivocado': True,
                }
                return render(request, 'logueo.html', contexto)
        return render(request, 'logueo.html')

def panel(request):
    if request.user.is_authenticated:
        mensajes = Mensaje.objects.filter(archivado=False).order_by('-pk')
        contexto = {
            'mensajes': mensajes,
        }
        return render(request, 'panel.html', contexto)
    else:
        return HttpResponseRedirect(reverse('logueo'))

def cerrar_sesion(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@csrf_exempt
def creando_mensaje(request):
    if request.method == 'POST':
        nuevo_nombre = request.POST["nombre"]
        nuevo_telefono = request.POST["telefono"]
        nueva_explicacion = request.POST["explicacion"]
        nuevo_mensaje = Mensaje(nombre=nuevo_nombre, telefono=nuevo_telefono, explicacion=nueva_explicacion)
        nuevo_mensaje.save()
        return render(request, 'mensaje_enviado.html')
    else:
        return HttpResponseRedirect(reverse('index'))

def borrando_mensaje(request, id_mensaje):
    mensaje = Mensaje.objects.get(pk=id_mensaje)
    mensaje.delete()
    return HttpResponseRedirect(reverse('panel'))
