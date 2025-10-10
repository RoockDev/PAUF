from django.core.management import BaseCommand

from ...models import Tarea, Programador


class Command(BaseCommand):

    def handle(self, *args, **options):
        tarea = Tarea(nombreTarea='tarea tchouaméni')
        tarea.usuario = Programador.objects.get(pk=1)
        tarea.usuario = Programador.objects.get(pk=2)