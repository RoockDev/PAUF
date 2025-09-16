from datetime import datetime

fecha = datetime.now().strftime("%d%m%Y")
nombre_archivo_log = f"{fecha}_Personas.log"

print(f"El archivo de log se llamara: {nombre_archivo_log}")

with open("Libro2.txt", "r") as fichero_entrada:
    with open(nombre_archivo_log, "w") as fichero_salida:
        contador_id = 1
        for linea in fichero_entrada:
            datos = linea.split(' ')

            datosUnidos = ', '.join(datos)

            # sentencia insert
            insert_sql = f'Insert into Personas (id,nombre,apellidos,fecha_nacimiento,calle,codigo_postal,numero,movil) values (id{contador_id}, {datosUnidos});\n'
            contador_id += 1
            fichero_salida.write(insert_sql)

    

# ahora = datetime.now().strftime("%d%m%Y") o como si lo haces todo en la linea 5. no me crees dos variables para hacer una cosa que puedes hacer una.
'''
nombre = datos[0]
apellidos = datos[1]
fecha_nacimiento = datos[2]
calle = datos[3]
codigo_postal = datos[4]
numero = datos[5]
movil = datos[6]
'''
# Seguro que se te ocurre un metodo que haga algo mejor que eso por si te cambio el txt no puedes hacer uno general? y con el f en la línea 23 si pones comillas dobles no tienes que poner comillas cada vez que pongas {x}
