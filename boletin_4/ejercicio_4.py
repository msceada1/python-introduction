# Usa un bucle for para recorrer la lista tareas. Por cada tarea, imprime una frase con este
# for#mato exacto:
# "[X] Título de la tarea" (Si está completada)
# "[ ] Título de la tarea" (Si no está completada)

tareas = []

tarea1 = {"id": 1, "Tarea": "Hacer la cama", "completado": True}
tarea2 = {"id": 2, "Tarea": "Sacar la basura", "completado": True}
tarea3 = {"id": 3, "Tarea": "Hacer la comida", "completado": False}

tareas.append(tarea1)
tareas.append(tarea2)
tareas.append(tarea3)

for t in tareas:
    if t["completado"] == True:
        print("[X]", t["Tarea"])
    else:
        print("[]", t["Tarea"])
