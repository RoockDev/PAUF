
"""
Ejercicio 1: Lista de equipos

Crea una lista con los 5 primeros equipos de la clasificación (puedes inventar el orden).

Muestra en pantalla el primer y último equipo.

Añade un equipo nuevo al final de la lista.

Inserta a mano un equipo en la primera posición.

Elimina un equipo que ya no quieras que esté en la lista.
"""
lista = ['Madrid', 'Barcelona', 'Atletico', 'Valencia', 'Betis']
print(lista[0])
print(lista[-1])

lista.append('Puertollano')
print(lista)
lista.insert(0,'Sevilla')
lista.remove('Atletico')
print(lista)