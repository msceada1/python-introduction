import random

class MiEntradaSalida:
    """Clase para gestionar la entrada y salida de datos de forma robusta."""

    @staticmethod
    def leer_entero(mensaje):
        while True:
            try:
                return int(input(mensaje + "\n"))
            except ValueError:
                print("Ha introducido un dato incorrecto.")

    @staticmethod
    def leer_entero_positivo(mensaje):
        while True:
            try:
                numero = int(input(mensaje + "\n"))
                if numero >= 0:
                    return numero
            except ValueError:
                print("Ha introducido un dato incorrecto.")

    @staticmethod
    def leer_entero_en_rango(mensaje, limite_inferior, limite_superior):
        while True:
            try:
                numero = int(input(mensaje + "\n"))
                if limite_inferior <= numero <= limite_superior:
                    return numero
            except ValueError:
                print("Ha introducido un dato incorrecto.")

    @staticmethod
    def leer_caracter(mensaje):
        while True:
            entrada = input(mensaje + "\n")
            if len(entrada) > 0:
                return entrada[0]
            print("Ha introducido un dato incorrecto.")

    @staticmethod
    def leer_caracter_sn(mensaje):
        while True:
            entrada = input(mensaje + "\n").upper()
            if len(entrada) == 1 and entrada in ('S', 'N'):
                return entrada

    @staticmethod
    def leer_cadena(mensaje):
        while True:
            entrada = input(mensaje + "\n")
            if len(entrada) > 0:
                return entrada

    @staticmethod
    def leer_opcion(mensaje, opciones):
        for i, opcion in enumerate(opciones, start=1):
            print(f"{i}: {opcion}")
        return MiEntradaSalida.leer_entero_en_rango(mensaje, 1, len(opciones))

    @staticmethod
    def leer_double(mensaje):
        while True:
            try:
                return float(input(mensaje + "\n"))
            except ValueError:
                print("ERROR: Ha introducido un dato incorrecto.")

    @staticmethod
    def genera_aleatorio(max_val):
        # En Python random.randint(a, b) incluye ambos extremos
        return random.randint(1, max_val)

    @staticmethod
    def genera_aleatorio_entre(min_val, max_val, se_acepta_el_maximo):
        if not se_acepta_el_maximo:
            max_val -= 1
        return random.randint(min_val, max_val)

    @staticmethod
    def imprimir_matriz(matriz):
        for fila in matriz:
            print(*(fila)) # El asterisco expande la lista para imprimirla bonita