import json

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

























