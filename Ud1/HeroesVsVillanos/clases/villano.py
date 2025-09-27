from .personaje import Personaje
import random

class Villano(Personaje):

    def __init__(self,nombre,apellidos,fecha_nacimiento):
        super().__init__(nombre,apellidos,fecha_nacimiento)
        self.chagepeteador = random.randint(0,100)
        self.entregador_tardio = random.randint(0,100)
        self.ausencias = random.randint(0,100)
        self.hablador = random.randint(0,100)
        self.calcular_puntuacion_total()


    def calcular_puntuacion_total(self):
        self.puntuacion_total = (
            self.chagepeteador +
            self.entregador_tardio +
            self.ausencias +
            self.ausencias
        ) / 4