import json
from getpass import fallback_getpass
from idlelib.pyshell import usage_msg

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import *
from django.http import JsonResponse
# Create your views here.
#CRUD CANCION
##get obtener una cancion por id
def get_cancion(request,id):
    try:
        cancion = Cancion.objects.values().get(id=id)
        return JsonResponse(cancion)
    except:
        return JsonResponse({"error" : "cancion no encontrada"})

##post crear una cancion
@csrf_exempt
def add_cancion(request):
    if request.method == "POST":
        jsonCancion = json.loads(request.body)
        cancion = Cancion.objects.create(**jsonCancion)
        return JsonResponse({"Muy bien": "Cancion insertada correctamente"})

##get obtener todas las canciones
def get_canciones(request):
    canciones = list(Cancion.objects.all().values())
    return JsonResponse(canciones,safe=False)

#delete borrar una cancion
def delete_cancion(request, id):
    try:
        cancion = Cancion.objects.get(pk=id)
        cancion.delete()
        return JsonResponse({"mensaje": "cancion eliminada correctamente"})
    except Cancion.DoesNotExist:
        return JsonResponse({"error": "Cancion no encontrada"}, status=404)

#update updatear una cancion
@csrf_exempt
def update_cancion(request,id):
    try:

        cancion = Cancion.objects.get(pk=id)
        nuevos_datos = json.loads(request.body) #cogemos los datos del body

        #se usa .get() para que si no se envia un campo que no cambie
        cancion.nombre = nuevos_datos.get('nombre',cancion.nombre)
        cancion.ano_lanzamiento = nuevos_datos.get('ano_lanzamiento',cancion.ano_lanzamiento)
        cancion.duracion = nuevos_datos.get('duracion',cancion.duracion)
        cancion.save()
        return JsonResponse({"mensaje": "cancion actualizada correctamente"})

    except Cancion.DoesNotExist:
        return JsonResponse({"error": "cancion no encontrada"},status=404)


#----------CRUD USUARIO----------
#get obtener todos los usuarios
def get_usuarios(request):
    usuarios = list(Usuario.objects.all().values())
    return JsonResponse(usuarios,safe=False)

#get obtener un usuario por id
def get_usuario(request,id):
    try:
        usuario = Usuario.objects.values().get(pk=id)
        return JsonResponse(usuario)
    except Usuario.DoesNotExist:
        return JsonResponse({"error":" usuario no encontrado"},status=404)

#post crear un usuario
@csrf_exempt
def add_usuario(request):
    if request.method == 'POST':
        try:
            jsonUsuario = json.loads(request.body)
            usuario = Usuario.objects.create(**jsonUsuario)
            return JsonResponse({"Succes":"Usuario creado correctamente"},status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)},status=400)

#delete borrar un usuario
@csrf_exempt
def delete_usuario(request,id):
    if request.method == 'DELETE':
        try:
            usuario = Usuario.objects.get(pk=id)
            usuario.delete()
            return  JsonResponse({"succes": "Usuario borrado correctamente"})
        except Usuario.DoesNotExist:
            return  JsonResponse({"Succes": "Usuario no encontrado"})
#update updatear un usuario
@csrf_exempt
def update_usuario(request,id):
    if request.method == 'PUT':
        try:
            usuario = Usuario.objects.get(pk=id)
            nuevos_datos = json.loads(request.body)

            usuario.nombre = nuevos_datos.get('nombre',usuario.nombre)
            usuario.apellido = nuevos_datos.get('apellido',usuario.apellido)
            usuario.nick = nuevos_datos.get('nick',usuario.nick)
            usuario.fecha_nacimiento = nuevos_datos.get('fecha_nacimiento', usuario.fecha_nacimiento)
            usuario.telefono = nuevos_datos.get('telefono',usuario.telefono)
            usuario.email = nuevos_datos.get('email',usuario.email)
            usuario.activo = nuevos_datos.get('activo',usuario.activo)
            return JsonResponse({"mensaje":"usuario actualizado correctamente"})
        except Usuario.DoesNotExist:
            return JsonResponse({"error":"usuario no encontrado"})


























