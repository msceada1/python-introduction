# Crea una lista vacía llamada tareas.
# 1. Define tres diccionarios representando tareas diferentes (usa datos inventados).
# 2. Añade las tres tareas a la lista tareas usando .append().
# 3. Imprime la longitud de la lista (len()).

tareas = []

tarea1 = {"id": 1, "Tarea": "Hacer la cama", "completado": True}
tarea2 = {"id": 2, "Tarea": "Sacar la basura", "completado": True}
tarea3 = {"id": 3, "Tarea": "Hacer la comida", "completado": False}

tareas.append(tarea1)
tareas.append(tarea2)
tareas.append(tarea3)

print("Tareas:\n", tareas)
