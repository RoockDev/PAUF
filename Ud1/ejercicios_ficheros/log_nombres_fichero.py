from datetime import datetime

ahora = datetime.now()
fecha = ahora.strftime("%d%m%Y")
nombre_archivo_log = f"{fecha}_Personas.log"

print(f"El archivo de log se llamara: {nombre_archivo_log}")

with open("Libro2.txt", "r") as fichero_entrada:
    with open(nombre_archivo_log, "w") as fichero_salida:
        for linea in fichero_entrada:
            datos = linea.split(' ')

            nombre = datos[0]
            apellidos = datos[1]
            fecha_nacimiento = datos[2]
            calle = datos[3]
            codigo_postal = datos[4]
            numero = datos[5]
            movil = datos[6]

            # sentencia insert
            insert_sql = f'Insert into Personas (id,nombre,apellidos,fecha_nacimiento,calle,codigo_postal,numero,movil) values (seq_personas.nextval, "{nombre}", "{apellidos}", "{fecha_nacimiento}". "{calle}", "{codigo_postal}", "{numero}", "{movil}")'

            fichero_salida.write(insert_sql + "\n")
