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

    def __str__(self):
        return (f"Heroe: {self.nombre} {self.apellidos} "
                f"(ID: {self.identificador}, Edad: {self.calcular_edad()})\n"
                f"  Código Limpio: {self.codigo_limpio}\n"
                f"  Bien Documentado: {self.bien_documentado}\n"
                f"  GITGod: {self.git_god}\n"
                f"  Arquitecto: {self.arquitecto}\n"
                f"  Detallista: {self.detallista}\n"
                f"  Puntuación Total: {self.puntuacion_total:.2f}")