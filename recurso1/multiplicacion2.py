from random import randint
# Pedir la cantidad de multiplicaciones que se van a generar
cuantas_multiplicaciones = int(input("Número de multiplicaciones:"))
# Bucle que repite la generación de multiplicaciones 
for numero in range(0,cuantas_multiplicaciones):
    factor1 = randint(2, 10)
    factor2 = randint(2, 10)
    # Calculamos la multiplicación de los números generados.
    solucion = factor1 * factor2
    # Imprimimos la multiplicación y pedimos al usuario la solución.
    print(factor1, "x", factor2, "= ", end="")
    solucion_de_usuario = int(input())
    # Si la solución dada por el usuario coincide por la solución calculada, el usuario habrá realizado de forma correcta la multiplicación, 
    # en caso contrario habrá cometido un error.
    if solucion_de_usuario == solucion:
        print("¡Respuesta correcta!")
    else:
        print("¡Respuesta incorrecta!")