# Crea una lista llamada numeros con los valores [10, 20, 30, 40, 50].
# 1. Imprime el primer y el último elemento de la lista.
# 2. Agrega el número 60 al final de la lista.
# 3. Inserta el número 23 en la segunda posición.
# 4. Cambia el valor del tercer elemento por 35.


def imprime_primer_y_ultimo_elemento_de_lista(numeros):
    print("Imprimiendo el primer y ultimo elemento: ")
    print(numeros[0])
    print(numeros[len(numeros) - 1])


def agregar_numero_a_lista(numeros, numero):
    print("Lista original:\n", numeros)
    print("Añadiendo el numero", numero, "a la lista...")
    numeros.append(numero)
    print("Lista actualizada:\n", numeros)


def agregar_numero_por_indice_especifico(numeros, numero):
    print("Lista original:\n", numeros)
    print("Añadiendo el numero", numero, "a la lista en la posicion 2...")
    numeros.insert(2, numero)
    print("Lista actualizada:\n", numeros)


def cambiar_numero_en_indice(numeros, numero, indice):
    print("Lista original:\n", numeros)
    print("cambiando el numero ", numeros[indice], "por ", numero, "...")
    numeros[indice] = numero
    print("Lista actualizada:\n", numeros)


if __name__ == '__main__':
    numeros = [10, 20, 30, 40, 50]
    imprime_primer_y_ultimo_elemento_de_lista(numeros)
    agregar_numero_a_lista(numeros, 60)
    agregar_numero_por_indice_especifico(numeros, 23)
    cambiar_numero_en_indice(numeros, 35, 2)
