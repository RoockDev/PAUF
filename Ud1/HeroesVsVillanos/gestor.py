import logging
import random

from clases.heroe import Heroe
from clases .villano import Villano

class Gestor:


    """
    No se si todo esto deberia ir en el main y si esta clase deberia de hacerse
    pero asi me parece mucho mas limpio
    """
    def __init__(self):
        self.personajes = [] # Lista para guardar a todos los personajes

    def agregar_personajes(self,personaje):
        try:
            self.personajes.append(personaje)
            logging.info(f"personaje añadido: {personaje.nombre} {personaje.apellidos} (ID: {personaje.identificador})")
        except Exception as e:
            logging.error(f"Error al añadir personaje: {e}")

    def listar_personajes(self):
        try:
            for personaje in self.personajes:
                print(personaje)
            logging.info("Personajes listados")
        except Exception as e:
            logging.error(f"Error al listar personajes: {e}")

    def buscar_por_nombre(self, nombre):
        resultados = []

        try:
            logging.info(f"Buscando personajes por nombre: '{nombre}'")
            for personaje in self.personajes:
                if nombre.lower() in personaje.nombre.lower():
                    resultados.append(personaje)
                    logging.info(f"Se han encontrado {len(resultados)} personajes con nombre '{nombre}'")

        except Exception as e:
            logging.error(f"Error al buscar por nombre: {e}")

        return resultados
           

    def buscar_por_atributo(self,atributo,valor_min,valor_max):
        """
        Buscamos personajes que tenguna una atributo dentro de un rango
        """

        resultados = []

        try:
            logging.info(f"Buscando personajes con el atributo {atributo} entre {valor_min} y {valor_max}")
            for personaje in self.personajes:
                if hasattr(personaje,atributo):  # verificamos si el personaje tiene ese atributo
                    valor = getattr(personaje,atributo) #obtenemos el valor del atributo
                    if valor_min <= valor and  valor <= valor_max:
                        resultados.append(personaje)
                        logging.info(f"personaje encontrado {personaje.nombre} atributo : {atributo} con valor {valor}")

        except Exception as e:
            logging.error(f"error al buscar el atributo {atributo}")

        return resultados


    def emparejamiento_heroes_villanos(self):
        try:
            heroes = []
            for personaje in self.personajes:
                if isinstance(personaje,Heroe):  #como el is/as en kotlin/java si no me equivoco
                    heroes.append(personaje)

            villanos = []
            for villano in self.personajes:
                if isinstance(villano,Villano):
                    villanos.append(villano)

            if not heroes or not villanos:
                logging.warning("No hay heroes o villanos para emparejar")

            heroe = random.choice(heroes)
            villano = random.choice(villanos)

            diferencia_poder = abs(heroe.puntuacion_total - villano.puntuacion_total)

            if diferencia_poder <= 10:
                resultado = "tienen mas o menos el mismo poder"
            elif diferencia_poder >= 30:
                resultado = "esta desequilibrado"
            else:
                resultado = "muy descompensado"

            logging.info(f"emparejamiento: Heroe: {heroe.nombre} con poder: {heroe.puntuacion_total}"
                         f"vs Villano: {villano.nombre} con poder: {villano.puntuacion_total}"
                         f"resultado: {resultado}")

            """
            He visto que en python se puede retornar varias variables, en este caso esto
            seria buena practica y estaria bien?
            o mejor devolverlo en un array?
            """
            return heroe,villano,resultado

        except Exception as e:
            logging.error(f"Error al emparejar pelea de heroe vs villano: {e}")