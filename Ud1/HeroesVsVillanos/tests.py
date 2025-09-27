import logging

from clases.heroe import Heroe
from clases.villano import Villano
from gestor import Gestor
from log import setup_logger
from fabrica import Fabrica

# configuracion logging
logging.basicConfig(  # configuracion de como se va a hacer el registro
    level=logging.INFO,  # solo registra mensajes de nivel INFO o superior
    format='%(asctime)s - %(levelname)s -%(message)s',  # como se va a mostrar el mensaje
    handlers=[  # manejadores donde se van a guardar los mensajes
        logging.FileHandler("logs/tests.log"),  # Guarda en un archivo
        logging.StreamHandler()  # Tambien imprime en consola
    ]
)


def menu():
    print("--Gestion Juego Heroes y Villanos")
    print("Elige un opcion:")
    print("[1] Crear Heroe")
    print("[2] Crear Villano")
    print("[3] Crear Heroe Aleatorio")
    print("[4] Crear villano Aleatorio")
    print("[5] Buscar hereo o villano por nombre")
    print("[6] Buscar heroe o villano por atributo y nivel")
    print("[7] Emparejar heroe u villano")
    print("[8] Listar todos los personajes")
    print("[9] Salir")


def gestion_simulacion(opcion, gestor):
    salir = True
    try:
        match opcion:
            case 1:
                print("Crear Heroe")
                nombre = input("nombre del heroe:\n")
                apellidos = input("apellidos del heroe:\n")
                fecha = input("Introduce la fecha de nacimiento (YYYY-MM-DD)\n")
                heroe = Fabrica.crear_heroe(nombre, apellidos, fecha)
                gestor.agregar_personajes(heroe)
                logging.info(f"Heroe creado: {heroe.nombre} {heroe.apellidos}")
            case 2:
                print("Crear villano")
                nombre = input("nombre del villano:\n")
                apellidos = input("apellidos del villano\n")
                fecha = input("Fecha de nacimiento(YYYY-MM-DD)\n")
                villano = Fabrica.crear_villano(nombre, apellidos, fecha)
                gestor.agregar_personajes(villano)
                logging.info(f"Villano creado: {villano.nombre} {villano.apellidos}")
            case 3:
                print("Crear heroe aleatorio")
                heroe = Fabrica.crear_heroe_aleatorio()
                gestor.agregar_personajes(heroe)
                logging.info(f"Heroe creado: {heroe.nombre} {heroe.apellidos}")
            case 4:
                print("Crear villano alatorio")
                villano = Fabrica.crear_villano_aleatorio()
                gestor.agregar_personajes(villano)
                logging.info(f"Villano creado: {villano.nombre} {villano.apellidos}")
            case 5:
                print("Buscar heroe o villano por nombre")
                nombre = input("Nombre a buscar\n")
                resultado = gestor.buscar_por_nombre(nombre)
                if resultado:
                    print("resultados encontrados")
                    for r in resultado:
                        print(f"{r.nombre} , {r.apellidos}")
                else:
                    print("No se encontraron resultados")
            case 6:
                print("Buscar heroe o villano por atributo y nivel")
                atributo = input("nombre de atributo\n")
                valor_min = int(input("Introduce el valor minimo\n"))
                valor_max = int(input("Introduce el valor maximo\n"))
                resultado = gestor.buscar_por_atributo(atributo, valor_min, valor_max)
                if resultado:
                    print("Resultados encontrados")
                    for r in resultado:
                        print(f"{r.nombre} {r.apellidos} {atributo}")
            case 7:
                print("Emparejar heroe y villano")
                heroe, villano, resultado = gestor.emparejamiento_heroes_villanos()
                if heroe and villano:
                    print(f"Emparejamiento: {heroe.nombre} vs {villano.nombre}")
                    print(f"resultado: {resultado}")
                else:
                    print("no hay suficientes heroes o villanos para emparejar")

            case 8:
                print("Listar todos los heroes")
                gestor.listar_personajes()
            case 9:
                print("saliendo del programa")
                salir = False

            case _:
                print("opcion no valida, elige una opcion correcta")


    except Exception as e:
        logging.error(f"Error al gestionar la opcion de la simulacion {e}")
        print("Error")

    return salir


def main():
    gestor = Gestor()

    while True:
        menu()
        try:
            opcion = int(input("Elige una opcion \n"))
            if not gestion_simulacion(opcion, gestor):
                break
        except Exception as e:
            logging.error(f"Error en el menú: {e}")
            print(f"Ha ocurrido un error")


if __name__ == "__main__":
    main()
