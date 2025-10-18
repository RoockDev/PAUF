from multiprocessing.connection import deliver_challenge

from django.core.management.base import BaseCommand
from ...models import *

class Command(BaseCommand):
    def handle(self, *args, **options):
        help = "comando parabuscar reproducciones entre edades"
        personas = Usuario.objects.filter(fecha_nacimiento__year__gte=1992, fecha_nacimiento__year__lte=1994)
        reproducciones = Reproduccion.objects.filter(usuario__in=personas)
        for persona in personas:
            self.stdout.write(self.style.SUCCESS(f'Usuario: {persona}'))
            reproducciones_personas = reproducciones.filter(usuario=persona)
            if reproducciones_personas.exists():
                for reproduccion in reproducciones_personas:
                    self.stdout.write(f'  Reproduccion: {reproduccion}')
            else:
                self.stdout.write('  - No tiene reproducciones')

                #esto no es muy eficiente por que tienes que recorrer mucho bucle para buscar
    #
    # def handle(self, *args, **options):
    #     personas = Usuario.objects.filter(fecha_nacimiento__year__gte=1992, fecha_nacimiento__year__lte=1994).prefetch_related('reproducciones')
    #     for persona in personas:
    #         self.stdout.write(self.style.SUCCESS(f'Usuario: {persona}'))
    #         reproducciones_personas = persona.reproducciones.all()
    #         if reproducciones_personas.exists():
    #             for reproduccion in reproducciones_personas:
    #                 self.stdout.write(f'  Reproduccion: {reproduccion}')
    #         else:
    #             self.stdout.write('   No tiene reproducciones')