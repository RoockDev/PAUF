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

    def __str__(self):
        return (f"Villano: {self.nombre} {self.apellidos} "
                f"(ID: {self.identificador}, Edad: {self.calcular_edad()})\n"
                f"  Chagepeteador: {self.chagepeteador}\n"
                f"  Entregador Tardío: {self.entregador_tardio}\n"
                f"  Ausencias: {self.ausencias}\n"
                f"  Hablador: {self.hablador}\n"
                f"  Puntuación Total: {self.puntuacion_total:.2f}")