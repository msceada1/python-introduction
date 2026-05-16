# Realizar un programa que solicite un carácter por teclado e informe por
# pantalla si el carácter es una vocal o no lo es. Si es una vocal mostrará el mensaje
# “Es la primera vocal (A)” o “Es la segunda vocal (E)”, etc.
from utils.mi_entrada_salida import MiEntradaSalida


def es_consonante(caracater):
    if caracater != 'a' and caracater != 'e' and caracater != 'i' and caracater != 'o' and caracater != 'u':
        return True


def comprueba_vocal(caracter):
    if caracter == 'a':
        return "es la primera vocal a"
    elif caracter == 'e':
        return "es la segunda vocal e"
    elif caracter == 'i':
        return "es la tercera vocal i"
    elif caracter == 'o':
        return "es la cuarta vocal o"
    else:
        return "es la quinta vocal u"


def programa():
    caracter = MiEntradaSalida.leer_caracter("Introduce un caracter")

    if es_consonante(caracter):
        print("El caracter intoducido no es una vocal")
        return
    else:
        print(comprueba_vocal(caracter))

if __name__ == '__main__':
    programa()
