# Realizar un programa que lea un número entero por teclado e informe de si
# el número es par o impar (el cero se considera par).

DIVISOR_COMPRUEBA_PAR = 2
RESULTADO_COMPRUEBA_QUE_SEA_PAR = 0

while True:
    try:
        numero = int(input("Introduce un número:\n"))
        if numero % DIVISOR_COMPRUEBA_PAR == RESULTADO_COMPRUEBA_QUE_SEA_PAR:
            print("El numero ", numero, " es par")
            break
        else:
            print("El numero ", numero, " no es par")
            break
    except ValueError:
        print("ERROR: debes introducir un numero entero")

