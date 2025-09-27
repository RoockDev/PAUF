from .personaje import Personaje
import random

class Heroe(Personaje):
    def __init__(self,nombre,apellidos,fecha_nacimiento):
        super().__init__(nombre,apellidos,fecha_nacimiento)
        self.codigo_limpio = random.randint(0,100)
        self.bien_documentado = random.randint(0,100)
        self.git_god = random.randint(0,100)
        self.arquitecto = random.randint(0,100)
        self.detallista = random.randint(0,100)
        self.calcular_puntuacion_total()

    def calcular_puntuacion_total(self):
        self.puntuacion_total = (
            self.codigo_limpio +
            self.bien_documentado +
            self.git_god +
            self.arquitecto +
            self.detallista
        ) / 5