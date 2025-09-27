import logging

from clases.heroe import Heroe
from clases.villano import Villano
from gestor import Gestor
from log import setup_logger

#configuracion logging
setup_logger()

#gestor
gestor = Gestor()

h1 = Heroe("Sergio","Zarcero","1998-10-31")

#prueba de registro en el log
logging.info(f"personaje Creado: {h1.nombre}")