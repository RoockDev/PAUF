from django.core.management.base import BaseCommand
from faker import Faker
from ...models import *
import random

fake = Faker('es_Es')

class Command(BaseCommand):

    def handle(self, *args, **options):
 # Ejercicio 4: Para buscar a una persona que su nombre contenga ‘an’
        # y que tenga una edad comprendida entre los 20 y 40 años.
        # Si nos da resultado coger el primer elemento y añadirle una dirección preferida
        #  a true y ponerle las demás a false.

        #para bucar un texto que contenga una cadena usamos icontains
        # para buscar por años usamos __year y para acotar usamos __gte (greater than or equal) y __lte (less than or equal)

        usuario = Usuario.objects.filter(nombre__icontains='an', fecha_nacimiento__year__gte=1984, fecha_nacimiento__year__lte=2004).first()
        if usuario:
            self.stdout.write(self.style.SUCCESS(f'Se ha encontrado el usuario: {usuario}'))
            # creamos una nueva direccion y se la ponemos como preferida

            nueva_direccion = Direccion.objects.create(
                calle=fake.street_name(),
                numero = fake.building_number(),
                ciudad=random.choice([c[0] for c in Direccion.CIUDADES]),
                usuario=usuario
            )
            usuario.preferida = nueva_direccion
            usuario.save()
        else:
            self.stdout.write(self.style.ERROR('No se encuentra ningun usuario'))

