Al hablar del bucle for, mencionamos el término secuencias, recuerda que las secuencias en Python son estructuras de datos 
especiales que pueden almacenar más de un valor y pueden ser recorridas secuencialmente, es decir, elemento por elemento.
Las cadenas son un buen ejemplo de secuencias, puedes recorrer los caracteres de una cadena uno a uno.
Resulta que también puedes iterar listas de la misma manera ya que las listas son también secuencias.

Probemos con este ejemplo.
`top_food = ['Sushi', 'Hamburguesa', 'HotDog', 'Torta', 'Tamales', 'Pizza', 'Subway']`

Usamos un bucle for para acceder a los elementos de la lista uno a uno.
`for food in top_food:`
Definimos una variable de control llamada `food`.

Observa que el bucle for obtiene los elementos de la lista en el orden exacto en que fueron proporcionados, primero obtenemos el elemento con índice cero,
luego obtenemos el elemento con índice uno y así sucesivamente.

>Current food: Sushi
>Current food: Hamburguesa
>Current food: HotDog
>Current food: Torta
>Current food: Tamales
>Current food: Pizza
>Current food: Subway

La sintaxis es muy conveniente cuando quieres hacer algo con cada elemento de una lista ☜(ﾟヮﾟ☜)
Ten en cuenta, que dentro del cuerpo del bucle no se tiene acceso al índice del elemento actual.
Por ejemplo, en la segunda iteración obtienes 'Hamburguesa' como valor de la variable food, pero no tienes forma de comprobarlo, 'Hamburguesa' tiene el índice uno.
También hay otra forma de iterar sobre una lista de forma que puedas acceder tanto al elemento como a su índice.

Checa este ejemplo. 
`top_food = ['Sushi', 'Hamburguesa', 'HotDog', 'Torta', 'Tamales', 'Pizza', 'Subway']`
`for food_index in range(len(top_food)):`
    `print('Current index:', food_index, '| Current food:', top_food[food_index], )`

En primer lugar, la función `len` devuelve el número de caracteres con listas y el número de elementos.
Así que en nuestro caso, `len` devolverá seis ya que tenemos seis comidas en la lista.

>Current index: 0 | Current food: Sushi
>Current index: 1 | Current food: Hamburguesa
>Current index: 2 | Current food: HotDog
>Current index: 3 | Current food: Torta
>Current index: 4 | Current food: Tamales
>Current index: 5 | Current food: Pizza
>Current index: 6 | Current food: Subway

Ahora el resultado es que este bit es de rango seis `range(len(top_food))`
Esto significa que el rango seis nos generará los siguientes números cero, uno, dos, tres, cuatro y cinco,
y da la casualidad de que estos son exactamente los posibles índices de nuestra lista.

Dentro del Bucle, ahora tenemos dos opciones:
1. Si necesitamos el índice de un elemento dado, simplemente usamos la variable de control índice de `food_index, `
2. Pero si necesitamos el elemento en el índice dado, podemos usar el nombre de la lista entre corchetes para acceder a él `[food_index]`

* Veamos un ejemplo más de iteración sobre listas.

Un sencillo programa que suma los gastos tuyos o de alguien más, tenemos una lista inicial donde alguien escribió todos los gastos 
`[52.36, 15.23, 14.98, 78.45, 19.82]`
Ahora, necesitamos sumar todos estos números e imprir la cantidad total de dinero que se gasto.

En primer lugar, necesitamos una variable para la suma en donde al principio la suma sea igual a cero: `sum = 0.0`
Ahora vamos a iterar sobre los gastos: `for spendings in spendings:`
Unos suman el valor del gasto: `sum += spendings` 
y despues imprimen el dinero gastado: `print('Dinero gastado: ', sum)`
Y eso es todo. 

Esta es una forma sencilla de sumar todos los números de una lista tomando a consideración los ejemplos anteriores.