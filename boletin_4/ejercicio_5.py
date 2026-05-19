# Crea una nueva lista llamada pendientes. Recorre la lista tareas original y añade a pendientes
# solo aquellas tareas que tengan "completada": False. Al final, imprime la lista de pendientes.

tareas = []

tarea1 = {"id": 1, "Tarea": "Hacer la cama", "completado": True}
tarea2 = {"id": 2, "Tarea": "Sacar la basura", "completado": True}
tarea3 = {"id": 3, "Tarea": "Hacer la comida", "completado": False}

tareas.append(tarea1)
tareas.append(tarea2)
tareas.append(tarea3)

pendientes = []

for t in tareas:
    if t["completado"] == False:
        pendientes.append(t)

print("tareas por terminar:\n", pendientes)
