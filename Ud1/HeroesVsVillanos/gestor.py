

from clases.heroe import Heroe
from clases .villano import Villano

class Gestor:

    def __init__(self):
        self.personajes = [] # Lista para guardar a todos los personajes

    def agregar_personajes(self,personaje):
        self.personajes.append(personaje)

    def listar_personajes(self):
        for personaje in self.personajes:
            print(personaje)


    def buscar_por_nombre(self,nombre):
        resultados = []
        for personaje in self.personajes:
            if nombre.lower() in personaje.nombre.lower():
                resultados.append(personaje)
        return resultados

    def buscar_por_atributo(self,atributo,valor_min,valor_max):
        """
        Buscamos personajes que tenguna una atributo dentro de un rango
        """

        resultados = []

        try:
            for personaje in self.personajes:
                if hasattr(personaje,atributo):  # verificamos si el personaje tiene ese atributo
                    valor = getattr(personaje,atributo) #obtenemos el valor del atributo
                    if valor_min <= valor <= valor_max:
                        resultados.append(personaje)

        except Exception as e:
            raise ValueError("Error al obtener personajes por atributo y valor")

        return resultados

