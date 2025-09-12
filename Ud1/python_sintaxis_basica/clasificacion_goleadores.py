"""
Ejercicio 3: Clasificación de goleadores
Crea una lista con los goles de 6 jugadores:
Muestra cuántos jugadores hay
Ordena la lista de goles de menor a mayor y luego de mayor a menor.
Muestra el máximo y el mínimo de la lista (max() y min()).
Inserta un nuevo jugador con 8 goles en la posición correcta para mantener el orden.
"""

goles = [23,40,16,35,55]
goles.sort()
print(goles)
goles.sort(reverse=True)
print(goles)
print(min(goles))
print(max(goles))
goles.insert(5,8)
print(goles)