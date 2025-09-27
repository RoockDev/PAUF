from clases.heroe import Heroe
from clases.villano import Villano

# Crear un héroe
h1 = Heroe("Ana", "García", "2001-05-10")
print(h1)  # Debería mostrar: Ana García (ID: 1)

# Crear un villano
v1 = Villano("Luis", "Fernández", "2000-11-22")
print(v1)  # Debería mostrar: Luis Fernández (ID: 2)

# Mostrar puntuaciones
print(f"Puntuación de {h1.nombre}: {h1.puntuacion_total}")
print(f"Puntuación de {v1.nombre}: {v1.puntuacion_total}")