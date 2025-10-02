import pandas as pd

datos = [
    {"ID": 1, "Nombre": "Ana",    "Edad": 20, "Curso": "DAW2", "Grupo": "A", "Ciudad": "Puertollano", "Nota": 7.5, "Becado": True,  "Creditos": 60, "FechaMatricula": "2024-09-10"},
    {"ID": 2, "Nombre": "Luis",   "Edad": 35, "Curso": "DAW2", "Grupo": "B", "Ciudad": "Ciudad Real", "Nota": 4.0, "Becado": False, "Creditos": 55, "FechaMatricula": "2024-09-12"},
    {"ID": 3, "Nombre": "María",  "Edad": 60, "Curso": "DAW1", "Grupo": "A", "Ciudad": "Toledo",       "Nota": 9.2, "Becado": True,  "Creditos": 65, "FechaMatricula": "2024-09-09"},
    {"ID": 4, "Nombre": "Pedro",  "Edad": 15, "Curso": "DAW1", "Grupo": "C", "Ciudad": "Albacete",     "Nota": 5.5, "Becado": False, "Creditos": 58, "FechaMatricula": "2024-09-15"},
    {"ID": 5, "Nombre": "Lucía",  "Edad": 22, "Curso": "DAW2", "Grupo": "A", "Ciudad": "Puertollano", "Nota": 8.8, "Becado": False, "Creditos": 61, "FechaMatricula": "2024-09-11"},
    {"ID": 6, "Nombre": "Diego",  "Edad": 44, "Curso": "DAW1", "Grupo": "B", "Ciudad": "Toledo",       "Nota": 6.2, "Becado": True,  "Creditos": 59, "FechaMatricula": "2024-09-13"},
    {"ID": 7, "Nombre": "Elena",  "Edad": 28, "Curso": "DAW2", "Grupo": "C", "Ciudad": "Ciudad Real", "Nota": 3.2, "Becado": False, "Creditos": 40, "FechaMatricula": "2024-09-10"},
    {"ID": 8, "Nombre": "Sergio", "Edad": 41, "Curso": "DAW1", "Grupo": "A", "Ciudad": "Albacete",     "Nota": 9.8, "Becado": True,  "Creditos": 66, "FechaMatricula": "2024-09-08"},
    {"ID": 9, "Nombre": "Nuria",  "Edad": 19, "Curso": "DAW2", "Grupo": "B", "Ciudad": "Puertollano", "Nota": 7.9, "Becado": True,  "Creditos": 62, "FechaMatricula": "2024-09-16"},
    {"ID":10, "Nombre": "Javier", "Edad": 52, "Curso": "DAW1", "Grupo": "C", "Ciudad": "Toledo",       "Nota": 4.9, "Becado": False, "Creditos": 48, "FechaMatricula": "2024-09-14"},
]





"""
datos = [
    {"ID": 1, "Nombre": "Ana",    "Edad": 20, "Curso": "DAW2", "Grupo": "A", "Ciudad": "Puertollano", "Nota": 7.5, "Becado": True,  "Creditos": 60, "FechaMatricula": "2024-09-10"},
    {"ID": 2, "Nombre": "Luis",   "Edad": 35, "Curso": "DAW2", "Grupo": "B", "Ciudad": "Ciudad Real", "Nota": 4.0, "Becado": False, "Creditos": 55, "FechaMatricula": "2024-09-12"},
    {"ID": 3, "Nombre": "María",  "Edad": 60, "Curso": "DAW1", "Grupo": "A", "Ciudad": "Toledo",       "Nota": 9.2, "Becado": True,  "Creditos": 65, "FechaMatricula": "2024-09-09"},
    {"ID": 4, "Nombre": "Pedro",  "Edad": 15, "Curso": "DAW1", "Grupo": "C", "Ciudad": "Albacete",     "Nota": 5.5, "Becado": False, "Creditos": 58, "FechaMatricula": "2024-09-15"},
    {"ID": 5, "Nombre": "Lucía",  "Edad": 22, "Curso": "DAW2", "Grupo": "A", "Ciudad": "Puertollano", "Nota": 8.8, "Becado": False, "Creditos": 61, "FechaMatricula": "2024-09-11"},
    {"ID": 6, "Nombre": "Diego",  "Edad": 44, "Curso": "DAW1", "Grupo": "B", "Ciudad": "Toledo",       "Nota": 6.2, "Becado": True,  "Creditos": 59, "FechaMatricula": "2024-09-13"},
    {"ID": 7, "Nombre": "Elena",  "Edad": 28, "Curso": "DAW2", "Grupo": "C", "Ciudad": "Ciudad Real", "Nota": 3.2, "Becado": False, "Creditos": 40, "FechaMatricula": "2024-09-10"},
    {"ID": 8, "Nombre": "Sergio", "Edad": 41, "Curso": "DAW1", "Grupo": "A", "Ciudad": "Albacete",     "Nota": 9.8, "Becado": True,  "Creditos": 66, "FechaMatricula": "2024-09-08"},
    {"ID": 9, "Nombre": "Nuria",  "Edad": 19, "Curso": "DAW2", "Grupo": "B", "Ciudad": "Puertollano", "Nota": 7.9, "Becado": True,  "Creditos": 62, "FechaMatricula": "2024-09-16"},
    {"ID":10, "Nombre": "Javier", "Edad": 52, "Curso": "DAW1", "Grupo": "C", "Ciudad": "Toledo",       "Nota": 4.9, "Becado": False, "Creditos": 48, "FechaMatricula": "2024-09-14"},
]
1)Muestra todos los alumnos que han aprobado (Nota ≥ 5).

2)Obtén los nombres de los alumnos becados.

3)Filtra los alumnos que sean de la ciudad de Puertollano y muestra solo su Nombre y Nota.

4)Selecciona los alumnos cuya Edad esté entre 20 y 40 años, ambos incluidos.

5)Muestra el Top 3 de alumnos con mejor nota, mostrando Nombre, Curso y Nota.

6)Filtra los alumnos de DAW2 que además tengan Nota superior a 8.

7)Muestra todos los alumnos que NO están becados.

8)Selecciona los alumnos cuya Fecha de matrícula sea posterior al 12 de septiembre de 2024.
"""
df = pd.DataFrame(datos)
print(df[df['Nota']>=5])

print(df[df['Becado'] ==True])
print(df[df['Edad'].between(20,40)])




