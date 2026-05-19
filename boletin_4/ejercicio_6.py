# 1. Pide al usuario que introduzca un título por teclado.
# 2. Recorre la lista tareas. Si encuentras una tarea cuyo título coincida con el input del
# usuario, imprime "¡Tarea encontrada!" y su ID.
# 3. Si termina el bucle y no la has encontrado, imprime "No existe".

tareas = []

tarea1 = {"id": 1, "Tarea": "hacer la cama", "completado": True}
tarea2 = {"id": 2, "Tarea": "sacar la basura", "completado": True}
tarea3 = {"id": 3, "Tarea": "hacer la comida", "completado": False}

tareas.append(tarea1)
tareas.append(tarea2)
tareas.append(tarea3)

nombre = input("Introduce el titulo de una tarea:\n")

encontradas = []

for t in tareas:
    if t["Tarea"] == nombre:
        encontradas.append(t)
        break

if len(encontradas) == 0:
    print("No se ha encotrado la tarea")
else:
    print("Tarea encontrada.\n id de la tarea = ", encontradas["id"])
