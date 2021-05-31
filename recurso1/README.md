# Aprendiendo las tablas de multiplicar con Python

En la actualidad la educación debe preparar al alumnado para vivir en el mundo digital, en el que ya se están desarrollando. Esa formación no se límita a enseñar la utilización de determinadas herramientas informáticas (a ser consumidores digitales), sino que debe capacitar a la persona para conocer el lenguaje digital que le posibilite adquirir las destrezas necesarias para relacionarse con el mundo digital de forma completa (ser creadores digitales). Para conseguir esta segunda vertiente es necesario desarrollar en los jóvenes el pensamiento computacional, como metodología de trabajo y la programación, como herramienta para resolver problemas.

Existen muchos lenguajes de programación, que nos dan la posibilidad de resolver problemas por medio de programas de ordenador. El lenguaje Python puede ser un candidato muy adecuado para introducir a los jóvenes de las distintas etapas educativas en la programación, por distintos motivos: aunque es un lenguaje muy completo y potente, su sintaxis es sencilla y facilita el aprendizaje de la programación, además al ser un lenguaje interpretado, la ejecución de los programas es sencilla, sin necesidad de ningún proceso complicado. Python, es mutltiplataforma, por lo que es fácil de trabajar con los distintos sistemas operativos que tenemos a nuestra disposición.

## ¿Qué debo saber para empezar a trabajar con este recurso?

### Niveles a los que va dirigido

Secundaria y Bachillerato

### Asignatura/s

El presente recurso se puede desarrollar en cualquier asignatura de Secundaria o Bachillerato, donde se esté haciendo una introducción a la programación. Asignaturas, com Tecnología, TIC o incluso matemáticas. 

### ¿Se requieren conocimientos previos?¿cuáles son?

El recurso tiene una dificultad sencilla, estaría pensado para desarrollar cuando ya se han estudiado algunos conceptos sobre programación y con el trabajo con el lenguaje Python: instalación de python en el sistema operativo, estructura de un programa, ejecución de un programa, trabajo con datos, tipos de datos y variables, estructuras de programación: secuencial, alternativas y repetitivas.

Puede ser un recurso muy acertado para repasar los conceptos básicos sobre la introducción a la programación con Python.

### ¿Qué objetivos se persigue con el recurso?

El principal objetivo es aprender como solucionar por medio de un programa de ordenador un problema. En este caso es un problema matemático. 
Vamos a realizar distintas aproximaciones a la solución del problema que nos permitan repasar distintos conceptos sobre la resolución de problemas con ordenadores:

* Analizar el problema
* Diseñar una posible solución al problema.
* Codificar un programa python que resuelva el problema.
* Verificar y comprobar que realmente el programa resuelve el problema

Concretamente al desarrollar el programa en Python vamos a repasar distintos conceptos:

* Estructura de un programa python
* Trabajar con datos, tipso de datos y variables
* Trabajar con funciones 
* Utilizar los distintos estructuras de programación: secuencial, alternativa y repetitiva para desarrollar el algoritmo que resuelve el problema.

### ¿En qué consiste el recurso?

El problema que queremos resolver es el siguiente:

Uno de los objetivos fundamentales de los alumnos de primaria es aprender muy bien las tablas de multiplicar en su etapa de primaria. Vamos a crear un programa que ayude a los alumnos de primaria a repasar las tablas de multiplicar. Para ello, nuestro programa irá generando distintas multiplicaciones y nos irá pidiendo la solución. El programa nos pedirá, al principio, el número de multiplicaciones que se van a generar. Y al finalizar nos dará la puntuación que hemos obtenido, y sacamos más de un 9, el programa nos felicitará.

## Y ahora que sé para que sirve, ¿cómo lo pongo en práctica?

Una de la técnicas para analizar un programa y diseñar un programa que resuelve el programa, es simplificar el problema, en problemas más sencillos que seamos capaces de solucionar de una manera sencilla y en sucesivas iteraciones ir introducción un nivel mayor de complejidad y solucionarlo a partir de lo que teníamos construido. 

En este caso vamos a realizar tres aproximaciones para resolver el problema completo:

### Generar una multiplicación

En esta primera aproximación el problema sería muy sencillo: Vamos a generar una multiplicación con números aleatorios (entre 1 y 10), le pedimos al usuario la solución y el programa nos dice si la solución es correcta o incorrecta.

¿Cómo generamos números aleatorios en Python?, en realidad en un ordenador generamos números [pseudoaleatorios](https://es.wikipedia.org/wiki/N%C3%BAmero_pseudoaleatorio), para generar números enteros pseudoaleatorio podemos usar la función `randint` del módulo `ramdom`. Veamos un ejemplo:

Si queremos generar números pseudoaleatorio entre el 2 y el 10, podemos hacer el siguiente programa (que podemos guardar en un fichero `programa1.py`):

```python
from random import randint
numero = randint(2, 10)
print(numero)
```

En la variable `numero` se guarda un número aleatorio entre 2 y 10 en cada una de las ejecuciones:

```bash
$ python3 programa1.py
7
```
Ya que sabemos generar números enteros aleatorios, para resolver nuestro primer programa tendríamos que hacer los siguientes pasos:

1. Generar dos números aleatorios entre 2 y 10 que serán los factores de la multiplicación.
2. Calcular la multiplicación de los números internamente.
3. Imprimir la multiplicación y pedir al usuario la solución.
4. Si la solución dad por el usuario coincide por la solución calculada, el usuario habrá realizado de forma correcta la multiplicación, en caso contrario habrá cometido un error.

Veamos una posible solución al problema, haráimos un programa python que guardaríamos en el fichero `multiplicacion1.py`:

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
# Si la solución dad por el usuario coincide por la solución calculada, el usuario habrá realizado de forma correcta la multiplicación, 
# en caso contrario habrá cometido un error.
if solucion_de_usuario == solucion:
    print("¡Respuesta correcta!")
else:
    print("¡Respuesta incorrecta!")
```




## ¿Qué habilidades de los alumnos desarrollo que no se pueden obtener de manera más tradicional?

## ¿Qué ventaja obtengo de utilizar este recurso en el aula?

## ¿Qué materiales necesito para ponerlo en práctica en el aula?