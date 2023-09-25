Muy bien, para evitar llenar el código con un montón de comentarios utilizaremos los archivos con extensión .md para explicarte el programa.
Si quieres hacer el programa con la explicación antes de continuar y copiar el código, termina de leer este documento y comienza a programar después, continuemos.

Un concepto muy importante en el mundo de la programación son las variables.
Una variable es un lugar con nombre en la memoria donde puede almacenar datos para su uso futuro.
Puedes tratar las variables como cajas especiales para datos.
Cada caja tiene un nombre y puedes ingresar fácilmente datos dentro de dichas cajas para referirse a ellos en otro lugar.

En Python podemos crear fácilmente nuestras propias variables o cajas para datos. Cada variable tiene un nombre y un valor.

Vamos a crear una variable llamada ‘saludo’.
Al mismo tiempo, también necesitamos poner un valor inicial en la variable.
Para ello, utilizamos el operador de asignación, que es un signo de igualdad.

`saludo = 'Hola! Amigo, soy una variable'`

La línea anterior crea una variable llamada saludo y le otorga el valor de la cadena ‘Hola! Amigo, soy una variable’ 
Sabemos que el valor es una cadena porque está rodeado de apóstrofes, podemos hacer varias cosas con las variables.
Por ejemplo, podemos imprimir el contenido de la variable, usaremos la función print() y dentro pondremos saludo.

`print(saludo)`

Y podras ver que se imprime el valor de la variable.
* Nota que no pusimos apóstrofes alrededor de la palabra saludo porque de otra forma sólo veríamos la palabra palabra saludo impresa en la salida.
En su lugar, hemos utilizado el nombre de la variable saludo sin apóstrofes.
Así que esta vez le indicamos a Python que imprima el valor de lo que está almacenado dentro de la variable llamada saludo.

También podemos utilizar el mismo signo igual para asignar un nuevo valor a nuestra variable.
Así que esta vez le escribiremos nueva información

`saludo = 'Hola! Amigo, estoy rescribiendo una variable'`

Y aquí volvemos a usar el print.

Veremos una salida diferente.
Observa que la variable empieza a existir cuando le asignas un valor por primera vez, antes de eso, la variable no existe.

Tus variables pueden tener casi cualquier nombre que desees, sólo recuerda algunas reglas de oro.

1. En primer lugar, los nombres de las variables deben comenzar con una letra o el signo de subrayado.
2. En segundo lugar, las letras mayúsculas y minúsculas se tratan de forma diferente.
3. Por último, Python también tiene un par de palabras clave que no se pueden utilizar como nombres de variables.

Algunas de ellas son `from` y `global`.

Si intentas asignar un valor a `from` y ejecutas tu programa veras un error.

Pero sólo hay un par de palabras reservadas como ésta, así que no te preocupes demasiado por ellas, pronto te explicare más de ellas.
Aparte de estas tres reglas, tus variables pueden tener los nombres que quieras.

Ahora ejecuta tu programa o descarga el archivo `variables.py` para que veas como funciona y juega con el.
