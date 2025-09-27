import logging

def setup_logger():
    logging.basicConfig( #configuracion de como se va a hacer el registro
        level=logging.INFO, # solo registra mensajes de nivel INFO o superior
        format = '%(asctime)s - %(levelname)s -%(message)s', #como se va a mostrar el mensaje
        handlers=[ # manejadores donde se van a guardar los mensajes
            logging.FileHandler("logs/app.log"), #Guarda en un archivo
            logging.StreamHandler() #Tambien imprime en consola
        ]
    )
