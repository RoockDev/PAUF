from django.core.management.base import  BaseCommand
from ...models import *

class Command(BaseCommand):


    def handle(self, *args, **options):
        self.stdout.write(self.style.ERROR('VAS A BORRAR TODOS LOS DATOS'))
        respuesta = input('estas seguro de que quieres continuar? (s/n): ')

        if respuesta == 's':
            self.stdout.write(self.style.WARNING('Iniciando borrado de datos masivo'))
            modelos = [Reproduccion, Direccion, Cancion, Podcast, Usuario, Autor]

            for modelo in modelos:
                modelo.objects.all().delete()

            self.stdout.write(self.style.SUCCESS('Borrado completado con exito'))
        else:
            self.stdout.write(self.style.SUCCESS('Borrado cancelado, no se han modificado los datos'))
