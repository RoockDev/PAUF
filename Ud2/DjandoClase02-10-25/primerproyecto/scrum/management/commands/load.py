from django.core.management import BaseCommand

from ...models import (Programador)


class Command(BaseCommand):
    def handle(self, *args, **options):
        programadores = Programador.objects.filter(nombre='sergio')
        for prog in programadores:
            prog.nombre = 'thouameninga'
            prog.save()
