# Usando el diccionario del ejercicio anterior:
# 1. Cambia el valor de la clave "completada" a True.
# 2. Añade una nueva clave "fecha_limite" con valor "20-10-2023".
# 3. Imprime el diccionario completo para ver los cambios.

tarea_demo = {"id": 1, "titulo": "Comprar pan", "completada": False}

print("Diccionario original:\n", tarea_demo)

tarea_demo["Fecha limite"] = "20-10-2023"
tarea_demo["completada"] = True
print("Diccionario actualizado:\n", tarea_demo)