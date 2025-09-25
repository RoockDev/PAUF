# Gestión de Héroes y Villanos en Python 🦸‍♂️🦹‍♀️

## 📌 Descripción
Este proyecto consiste en el desarrollo de un programa en **Python** para gestionar **héroes y villanos** dentro de un entorno de aula.  

El objetivo es aplicar conceptos de:
- **Programación Orientada a Objetos (POO)**
- **Manejo de estructuras de datos**
- **Búsquedas y filtrados**
- **Aleatoriedad**
- **Logging para registro de eventos y errores**

---

## 🏷️ Atributos comunes
Todos los personajes (héroes y villanos) tienen:
- Nombre  
- Apellidos  
- Fecha de nacimiento  
- Identificador  
- Puntuación total  

---

## 🦹‍♂️ Villanos
Cada villano cuenta con las siguientes cualidades (valores aleatorios entre 0 y 100):
- **Chagepeteador**  
- **EntregadorTardío**  
- **Ausencias**  
- **Hablador**  

La **puntuación total** se calcula en base a un algoritmo definido (ejemplo: promedio ponderado tipo FIFA).

---

## 🦸‍♂️ Héroes
Cada héroe cuenta con las siguientes cualidades (valores aleatorios entre 0 y 100):
- **Código Limpio**  
- **Bien Documentado**  
- **GITGod**  
- **Arquitecto**  
- **Detallista**  

La **puntuación total** se calcula con el mismo criterio que en los villanos.

---

## ⚙️ Funcionalidades principales

1. **Gestión de personajes**  
   - Crear héroes y villanos dinámicamente.  
   - Almacenarlos en una estructura de datos (lista, diccionario, etc.).  

2. **Búsquedas y filtrados**  
   - Permite buscar por cualquier **atributo o cualidad**.  
   - Ejemplo:  
     - `Buscar villanos con nombre = Fernando`  
     - `Buscar héroes con GITGod > 50`  

3. **Edad**  
   - El sistema puede calcular la edad de héroes y villanos a partir de su fecha de nacimiento.  

4. **Enfrentamientos**  
   - Empareja un héroe y un villano **al azar**.  
   - Evalúa el enfrentamiento:  
     - **Equilibrado** → Puntuaciones similares.  
     - **Alta desviación** → Diferencia notable entre héroe y villano.  

5. **Logging**  
   - Todas las acciones importantes se registran en un archivo de log.  
   - Se incluyen también errores y excepciones.  

---

## 🎯 Objetivos del proyecto
- Crear héroes y villanos con cualidades aleatorias.  
- Calcular y almacenar sus puntuaciones totales.  
- Gestionarlos en estructuras de datos.  
- Realizar búsquedas avanzadas por atributos y cualidades.  
- Simular enfrentamientos equilibrados o desbalanceados.  
- Mantener un **registro detallado** de todas las acciones y errores.  

---

## 🚀 Tecnologías utilizadas
- **Python 3.x**
- **Módulos estándar**:  
  - `random` (para asignar valores aleatorios)  
  - `datetime` (cálculo de edad)  
  - `logging` (registro de acciones y errores)  

---

## 📂 Estructura recomendada del proyecto
