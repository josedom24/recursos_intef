from random import randint
# Pedir la cantidad de multiplicaciones que se van a generar
cuantas_multiplicaciones = int(input("Número de multiplicaciones:"))
# Incializamos el contador
contador_multiplicaciones_correctas = 0
# Bucle que repite la generación de multiplicaciones 
for numero in range(0,cuantas_multiplicaciones):
    factor1 = randint(2, 10)
    factor2 = randint(2, 10)
    # Calculamos la multiplicación de los números generados.
    solucion = factor1 * factor2
    # Imprimimos la multiplicación y pedimos al usuario la solución.
    print(factor1, "x", factor2, "= ", end="")
    solucion_de_usuario = int(input())
    # Si la solución dada por el usuario coincide con la solución calculada, 
    # el usuario habrá realizado de forma correcta la multiplicación, 
    # en caso contrario habrá cometido un error.
    if solucion_de_usuario == solucion:
        print("¡Respuesta correcta!")
        # Incrementamos el contador de multiplicaciones correctas
        contador_multiplicaciones_correctas = contador_multiplicaciones_correctas + 1
    else:
        print("¡Respuesta incorrecta!")
# Calculamos la nota
nota = contador_multiplicaciones_correctas / cuantas_multiplicaciones * 10
print("Tu nota ha sido", nota)
# Si la nota es mayor o igual que 9, felicitamos al usuario
if nota >=9:
    print("Felicidades, has sacado más de un 9.")