
from django.core.management.base import BaseCommand
from faker import Faker
from ...models import *


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Cargando datos iniciales..."))
        fake =Faker('es_ES')
        Usuario.objects.create(nombre=fake.first_name(), apellido=fake.last_name(), nick=fake.user_name(),
                               fecha_nacimiento=fake.date_of_birth(minimum_age=18, maximum_age=18),
                               telefono=fake.phone_number(), email=fake.email())
        self.stdout.write(self.style.SUCCESS("PERSONA INSERTADA"))
