import random
from random import choice

from clases.heroe import Heroe
from clases.villano import Villano

class Fabrica:
    @staticmethod
    def crear_heroe(nombre,apellidos,fecha_nacimiento):
        return Heroe(nombre,apellidos,fecha_nacimiento)
    @staticmethod
    def crear_villano(nombre,apellidos,fecha_nacimiento):
        return Villano(nombre,apellidos,fecha_nacimiento)
    @staticmethod
    def crear_heroe_aleatorio():
        nombres = [
            "Thibaut", "Dani", "Éder", "David", "Jesús", "Federico", "Aurélien", "Luka", "Toni", "Vinicius",
            "Rodrygo", "Kylian", "Arda", "Endrick", "Fran",  "Lunin", "Rudiger",

        ]

        apellidos = [
            "Courtois", "Carvajal", "Militão", "Alaba", "Mendy", "Tchouaméni", "Camavinga", "Modrić", "Kroos",
            "Bellingham", "Valverde", "Ceballos", "Rudiger", "Militão", "Éder", "Vinicius", "Rodrygo",

        ]
        fechas = [
            "2000-01-01", "2001-05-10", "1999-11-22", "2002-03-15", "1998-07-30", "1995-04-07", "2003-09-21",
            "1990-09-07", "1985-04-26", "1992-02-12", "1996-06-20", "1994-08-14", "1997-12-10", "1993-11-05",
            "1991-03-23", "1988-05-16", "1987-10-02", "1989-01-28", "1986-08-09", "1995-09-03"
        ]

        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        fecha = random.choice(fechas)

        return Heroe(nombre,apellido,fecha)

    @staticmethod
    def crear_villano_aleatorio():
        nombres = [
            "Robert", "Gavi", "Pedri", "Frenkie", "João", "Lamine", "Raphinha", "Ferran", "Iñaki", "Pau",
            "Eric", "Jules", "Ronald", "Thomas", "Marcos", "Ilias", "Ansu", "Alejandro", "Sergio", "Arnau"
        ]

        apellidos = [
            "Lewandowski", "Gavi", "Pedri", "de Jong", "Félix", "Yamal", "Raphinha", "Torres", "Pérez",
            "García", "Araujo", "Fati", "Balde", "Roberto", "Martínez"
        ]

        fechas = [
            "2000-01-01", "2001-05-10", "1999-11-22", "2002-03-15", "1998-07-30", "1995-04-07", "2003-09-21",
            "1990-09-07", "1985-04-26", "1992-02-12", "1996-06-20", "1994-08-14", "1997-12-10", "1993-11-05",
            "1991-03-23", "1988-05-16", "1987-10-02", "1989-01-28", "1986-08-09", "1995-09-03"
        ]

        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        fecha = random.choice(fechas)

        return  Villano(nombre,apellido,fecha)
