# Consulta el tiempo atmosférico con Python

Un programa de ordenador recibe datos de entrada, procesa de forma automáticamente estos datos y genera unos datos de salida, nos devuelve una información.

Los datos de entrada, normalmente son introducidos por el usuario. En otras ocasiones los datos con los que trabaja el programa están guardados en ficheros o en bases de datos. Pero, ¿y si pudiéramos utilizar los datos que tenemos disponible en internet para realizar nuestros programas?

Actualmente, una de las fuentes de información más importante que tenemos son las páginas web disponibles en internet. Los usuarios podemos consultar distintas páginas web y la información se nos muestra con una estructura determinada: el lenguaje HTML, que está pensado para representar la información de manera sencilla.

Sin embargo, ¿podríamos crear programas que tomaran como datos de entrada la información ofrecida por alguna página web?. La respuesta es sí, pero no vamos a utilizar directamente una página web, vamos a usar lo que conocemos como **Servicio web**. Hay distintos tipos de Servicios web, nosotros vamos a utilizar los servicios web REST (RESTful web API) que son un mecanismo de comunicación que nos permite que un programa se comunique con otro. En este caso la información que se comparte tiene que estar estructurada para que sea fácil gestionarla con un programa. En este recurso el lenguaje que estructura la información que vamos a utilizar será JSON.

## ¿Qué debo saber para empezar a trabajar con este recurso?

### Niveles a los que va dirigido

Bachillerato y formación Profesional

### Asignatura/s

### ¿Se requieren conocimientos previos?¿cuáles son?

### ¿Qué objetivos se persigue con el recurso?


### ¿En qué consiste el recurso?

Vamos a desarrollar un programa en Python que nos posibilite consultar el tiempo atmosférico que tenemos en nuestra ciudad. Para ello el programa, se comunicara con el servicio web RESTful API de `openwheather`.

## Y ahora que sé para que sirve, ¿cómo lo pongo en práctica?

### Paso 1: Entendiendo la diferencia entre aplicación web y servicio web

Como ya hemos presentado en la introducción del recurso, las páginas web o aplicaciones web están pensada para que las personas consulten información. De esta manera si quiero saber los datos atmosféricos de mi ciudad puedo a acceder a la página [openweathermap.org](https://openweathermap.org) y hacer una búsqueda de mi ciudad:

![openwhetaher](img/openwheather1.png)

Los datos son recibidos utilizando el lenguaje HTML y utilizando Hojas de Estílo (CSS) para darle formato. De esta manera la persona recibe está información de manera muy clara.

Pero, ¿y si queremos desarrollar un programa que haga la misma consulta y que pueda procesar esa información de forma automática? En este caso necesitaríamos consulat el servicio web RESTful de openwhether: [https://openweathermap.org/api](https://openweathermap.org/api) y la información recibida vendría estructurada con otro lenguaje de marcado, en nuestro caso utilizaremos JSON. Lo vemos en el siguiente punto.

### Paso 2: Usando el servicio web RESTful de OpenWheather

Aunque algunos servicios web RESTful se pueden usar sin ninguna restricción, otros, como el de OpenWheather, es necesario que nos identifiquemos para su utilización. En este caso el proceso de autentficación se hace mediante una clave personal (**API key**). Lo primero que vamos a hacer es obtener nuestra clave personal, para ello:

1. Nos registramos en la página de OpenWheather
2. Accedemos con el usuario y contraseña que hemos indicado.
3. Accedemos al apartado *API Keys* y generamos una nueva key.

    ![openwhetaher](img/openwheather2.png)

Ya podemos ver la clave que se nos asignado. Tenemos que tener en cuenta que esta clave es como nuestra contraseña, nos identifica en el servicio web, por lo que es importante que la protejamos de forma adecuada.

![openwhetaher](img/openwheather3.png)


## ¿Qué habilidades de los alumnos desarrollo que no se pueden obtener de manera más tradicional?


## ¿Qué ventaja obtengo de utilizar este recurso en el aula?


## ¿Qué materiales necesito para ponerlo en práctica en el aula?

