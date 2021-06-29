# Aprendiendo las tablas de multiplicar con Python

En la actualidad la educación debe preparar al alumnado para vivir en el mundo digital, en el que ya se está desarrollando. Esa formación no se límita a enseñar la utilización de determinadas herramientas informáticas (a ser consumidores digitales), sino que debe capacitar a la persona para conocer el lenguaje digital que le posibilite adquirir las destrezas necesarias para relacionarse con el mundo digital de forma completa (ser creadores digitales). Para conseguir esta segunda vertiente es necesario desarrollar en los jóvenes el pensamiento computacional, como metodología de trabajo y la programación, como herramienta para resolver problemas.

Existen muchos lenguajes de programación, que nos dan la posibilidad de resolver problemas por medio de programas de ordenador. El lenguaje Python puede ser un candidato muy adecuado para introducir a los jóvenes, de las distintas etapas educativas, en la programación. 

Podemos elegir Python, como lenguaje para introducirnos en la programación, por distintos motivos: aunque es un lenguaje muy completo y potente, su sintaxis es sencilla y facilita el aprendizaje de la programación, además al ser un lenguaje interpretado, la ejecución de los programas es sencilla, sin necesidad de ningún proceso complicado. Python, es mutltiplataforma, por lo que es fácil de trabajar con los distintos sistemas operativos que tenemos a nuestra disposición.

## ¿Qué debo saber para empezar a trabajar con este recurso?

### Niveles a los que va dirigido

Secundaria y Bachillerato

### Asignatura/s

El presente recurso se puede desarrollar en cualquier asignatura de Secundaria o Bachillerato, donde se esté haciendo una introducción a la programación. Asignaturas como Tecnología, TIC o incluso, Matemáticas. 

### ¿Se requieren conocimientos previos?¿cuáles son?

Para realizar este recurso es necesario tener un conocimiento básico de Python, en concreto se debe estar familiarizado con algunos conceptos: instalación de python en el sistema operativo, estructura de un programa, ejecución de un programa, trabajo con datos, tipos de datos y variables, estructuras de programación: secuencial, alternativas y repetitivas.

Puede ser un recurso muy acertado para repasar los conceptos básicos sobre la introducción a la programación con Python.

### ¿Qué objetivos se persigue con el recurso?

El principal objetivo es introducir una metodología de trabajo para facilitar al alumno la resolución de problemas, por medio de programas de ordenador. En este recurso vamos a resolver un problema matemático. 

La metodología que vamos a utilizar consiste en realizar distintas aproximaciones a la solución del problema que nos permitan repasar distintos conceptos sobre el ciclo de vida del desarrollo de programas:

* Análisis del problema.
* Diseño de una posible solución al problema.
* Codificación de un programa python que resuelva el problema.
* Verificación y comprobación de que realmente el programa resuelve el problema.

Concretamente al desarrollar el programa en Python vamos a repasar distintos conceptos:

* Estructura de un programa python.
* Trabajar con datos, tipos de datos y variables.
* Trabajar con funciones.
* Utilizar los distintos estructuras de programación: secuencial, alternativa y repetitiva para desarrollar el algoritmo que resuelve el problema.

### ¿En qué consiste el recurso?

El problema que queremos resolver es el siguiente:

Uno de los objetivos fundamentales de los alumnos de primaria es aprender muy bien las tablas de multiplicar. Vamos a crear un programa que ayude a los alumnos a repasar las tablas de multiplicar. Para ello, nuestro programa irá generando distintas multiplicaciones y nos irá pidiendo la solución. El programa nos pedirá, al principio, el número de multiplicaciones que se van a generar. Y al finalizar nos dará la puntuación que hemos obtenido, y si sacamos más de un 9, el programa nos felicitará.

## Y ahora que sé para que sirve, ¿cómo lo pongo en práctica?

Una de las técnicas para analizar un problema y diseñar un programa que lo resuelva, consiste en simplificar el problema en otros más sencillos que seamos capaces de solucionar de una manera simple y en sucesivas iteraciones, ir introduciendo un nivel mayor de complejidad y solucionarlo a partir de lo que teníamos construido. 

En este caso vamos a realizar tres aproximaciones para resolver el problema completo:

### Primera aproximación: Generar una multiplicación

En esta primera aproximación el problema sería muy sencillo: Vamos a generar una multiplicación con números aleatorios (entre 1 y 10), le pedimos al usuario la solución y el programa nos dice si la solución es correcta o incorrecta.

¿Cómo generamos números aleatorios en Python?, en realidad en un ordenador generamos números [pseudoaleatorios](https://es.wikipedia.org/wiki/N%C3%BAmero_pseudoaleatorio), y para ello podemos usar la función `randint` del módulo `random`. Veamos un ejemplo:

Si queremos generar números pseudoaleatorio entre el 2 y el 10, podemos hacer el siguiente programa (que podemos guardar en un fichero `programa1.py`):

```python
from random import randint
numero = randint(2, 10)
print(numero)
```

En la variable `numero` se guarda un número entero aleatorio entre 2 y 10 en cada una de las ejecuciones:

```bash
$ python3 programa1.py
7

$ python3 programa1.py
5
```
Ya que sabemos generar números enteros aleatorios, para resolver nuestro primer programa tendríamos que hacer los siguientes pasos:

1. Generar dos números aleatorios entre 2 y 10 que serán los factores de la multiplicación.
2. Calcular la multiplicación de los números internamente.
3. Imprimir la multiplicación y pedir al usuario la solución.
4. Si la solución dada por el usuario coincide con la solución calculada, el usuario habrá realizado de forma correcta la multiplicación, en caso contrario habrá cometido un error.

Veamos una posible solución al problema, haríamos un programa python que guardaríamos en el fichero [`multiplicacion1.py`](multiplicacion1.py):

```python
from random import randint
# Generamos dos números aleatorios entre 2 y 10 que serán los factores de la multiplicación.
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
else:
    print("¡Respuesta incorrecta!")
```

Veamos cómo funciona:

```bash
$ python3 multiplicacion1.py 
3 x 6 = 18
¡Respuesta correcta!

$ python3 multiplicacion1.py 
6 x 6 = 37
¡Respuesta incorrecta!
```

Veamos algunos aspectos del programa:

1. `factor1` y `factor2` son dos variables enteras generadas con la función `randint`.
2. La variable `solucion` también será de tipo entero, ya que al multiplicar dos valores enteros el resultado también es entero.
3. La función `print` nos permite imprimir en pantalla: imprimimos el valor de la variable `factor1`, el carácter "x", el valor de la variable `factor2` y el carácter `=`. El parámetro `end=""` lo utilizamos para que no haga un salto de línea y la siguiente instrucción se ejecute en la misma línea.
4. La función `input` lee una cadena de caracteres por teclado, en este caso usamos la función `int` para convertir esa cadena de caracteres en un número entero, que guardaremos en la variable `solucion_de_usuario`.
5. La instrucción `if` nos permite ejecutar un bloque de código u otro según el resultado de una condición lógica. En este caso esa condición será la comprobación de si la solución calculada (variable `solucion`) y la solución dada por el usuario (variable `solucion_de_usuario`) son iguales. Para comprobar si dos valores son iguales usamos el operador `==`. Si los dos valores son iguales, se ejecutará la primera instrucción `print`, en caso contrario, se ejecutará la segunda. En python es muy importante el sangrado de código, es decir los bloques de instrucciones que se ejecutan en el `if` deben estar tabulados.

### Segunda aproximación: Generar varias multiplicaciones

A continuación vamos a complicar un poco el problema: ahora queremos que el programa nos pida la cantidad de multiplicaciones que va a generar y cuya solución va a pedir al usuario. En este caso vamos a introducir un bucle (estructura repetitiva) que nos va a permitir repetir un número de veces un conjunto de instrucciones.

¿Cómo podemos repetir un bloque de instrucciones en python? Para ello vamos a usar un bucle construido con la instrucción `for`, por ejemplo si queremos escribir 10 veces un mensaje podemos ejecutar el siguiente programa:

```python
for numero in range(0,10):
    print("Hola")
```

En esta caso creamos un rango de valores (`range`) que nos permite repetir la instrucción `print` 10 veces. El rango de valores que hemos definido va desde el 0 al 9, y la variable `numero` va tomando cada uno de esos valores en cada iteración, aunque en este caso no hemos usado esa variable.

Por lo tanto para resolver nuestro segundo problema deberemos:

1. Pedir la cantidad de multiplicaciones que se van a generar.
2. Crear un bucle que repita las instrucciones del programa anterior (primera aproximación) tantas veces como hayamos indicado.

Para ello creamos el siguiente programa, que guardamos en el fichero [`multiplicacion2.py`](multiplicacion2.py):

```python
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
    # Si la solución dada por el usuario coincide con la solución calculada, 
    # el usuario habrá realizado de forma correcta la multiplicación, 
    # en caso contrario habrá cometido un error.
    if solucion_de_usuario == solucion:
        print("¡Respuesta correcta!")
    else:
        print("¡Respuesta incorrecta!")
```

Veamos el funcionamiento:

```bash
$ python3 multiplicacion2.py 
Número de multiplicaciones:3
2 x 4 = 8
¡Respuesta correcta!
8 x 8 = 64
¡Respuesta correcta!
2 x 7 = 15
¡Respuesta incorrecta!
```

Estudiemos algunos aspectos del programa:

1. Vamos a pedir la cantidad de multiplicaciones que vamos a generar al usuario, usando una instrucción `input`. En este caso la instrucción `input` tiene como parámetro el mensaje que vamos a mostrar al usuario. Además la cadena de caracteres que vamos a leer la convertimos a entero, para posteriormente usarla en la función `range`.
2. La instrucción `for` nos permite hacer un bucle que repite el bloque de instrucciones, tantas veces como hemos indicado en la variable `cuantas_multiplicaciones`.

### Tercera aproximación: Generación de multiplicaciones y puntuación obtenida

Finalmente vamos a introducir el último elemento a nuestro problema: queremos saber las respuestas correctas, para que al finalizar el programa nos de una nota (de 0 a 10) y que nos felicite si hemos sacado más de un 9. Para calcular la nota podemos usar la formula: `multiplicaciones_correctas/total_multiplicaciones * 10`.

En este caso necesitamos contar las respuestas correctas, para ello vamos a usar un contador. Un contador es una variable entera que nos permite contar un suceso. El contador se inicializa a un valor inicial, y se va incrementando cada vez que ocurre el suceso que queremos contar.

La solución del problema quedaría de la siguiente forma:

1. Pedir la cantidad de multiplicaciones que se van a generar.
2. Inicializamos el contador.
3. Crear un bucle que repita las instrucciones del programa anterior tantas veces como hayamos indicado:
    * Generar dos números aleatorios entre 2 y 10 que serán los factores de la multiplicación.
    * Calcular la multiplicación de los números internamente.
    * Imprimir la multiplicación y pedir al usuario la solución.
    * Si la solución dada por el usuario coincide con la solución calculada, el usuario habrá realizado de forma correcta la multiplicación, en caso contrario habrá cometido un error. 
    * Si la solución dada por el usuario coincide con la solución calculada, incrementamos el contador.
4. Calculamos la nota: `contador_preguntas_correctas / cantidad_multiplicaciones * 10`
5. Imprimimos la nota
6. Si la nota es mayor o igual que 9 mostramos un mensaje de felicitación.

El programa quedaría de la siguiente manera ([`multiplicacion3.py`](multiplicacion3.py)):

```python
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
```

Y Podemos hacer una prueba:

```bash
$ python3 multiplicacion3.py 
Número de multiplicaciones:3
5 x 2 = 10
¡Respuesta correcta!
5 x 4 = 20
¡Respuesta correcta!
9 x 2 = 17
¡Respuesta incorrecta!
Tu nota ha sido 6.666666666666666
```

## ¿Qué habilidades de los alumnos desarrollo que no se pueden obtener de manera más tradicional?

Esta actividad puede ayudar al alumno a afianzar conceptos ya estudiados sobre programación, profundizando en la metodología de análisis del problema y en la realización de programas en Python. Además el hecho de trabajar con ordenadores es muy motivador para el alumnado, que puede ir comprobando si el programa realiza las operaciones que le hemos programado.

## ¿Qué ventaja obtengo de utilizar este recurso en el aula?

Aunque tradicionalmente la enseñanza de la programación es muy práctica y se realizan muchos ejercicios, en muchas ocasiones, sobre todo cuando el alumno se está iniciando en el desarrollo de programas, no se pone mucha atención en las distintas metodologías que nos facilitan el análisis del problema y el diseño de una posible solución.

Con este recurso se introduce una metodología que puede ayudar al alumno a enfrentarse con problemas un poco más complejos: se analiza el problema completo, pero se van dando soluciones parciales más simples, y se va añadiendo elementos del problema en sucesivas aproximaciones, hasta realizar un programa que resuelve el problema completo.

## ¿Qué materiales necesito para ponerlo en práctica en el aula?

Necesitamos un ordenador con Python 3 instalado. Para codificar el programa podemos usar cualquier editor de texto.