"""
Ejercicio 2: Jornada de partidos

Crea dos listas:
locales = ["Real Madrid", "Barcelona", "Atlético", "Sevilla", "Valencia"]
visitantes = ["Athletic", "Betis", "Cádiz", "Villarreal", "Osasuna"]
imprimir los partidos en formato:
Real Madrid vs Athletic
Barcelona vs Betis

Elimina un partido (por ejemplo, el de Sevilla vs Villarreal).
Añade un nuevo partido con un equipo inventado."""

locales = ['Real Madrid', 'Barcelona', 'Atletico','Sevilla','Valencia']
visitantes = ['Athletic', 'Betis','Cadiz','Villareal','Osasuna']

for local in range(0,len(locales)):
    print(locales[local]  + " vs " + visitantes[local])

locales.remove('Sevilla')
visitantes.remove('Villareal')

for local in range(0,len(locales)):
    print(locales[local] + " vs " + visitantes[local])

locales.append("Chelsea")
visitantes.append("Arsenal")

for local in range(0,len(locales)):
    print(locales[local] + " vs " + visitantes[local])
 