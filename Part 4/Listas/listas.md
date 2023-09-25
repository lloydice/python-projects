# Listas
Las listas se utilizan normalmente para almacenar múltiples valores del mismo tipo, 
múltiples enteros, múltiples flotantes o múltiples cadenas.
En este ejemplo, vamos a almacenar nombres de un grupo de personas.
Podríamos hacerlo así: nombre uno, nombre dos, nombre tres, ..., nombre seis, ...,


`nombre_uno = John`
`nombre_dos = Tere`s
`nombre_tres = Michael`

Desafortunadamente, trabajar con múltiples variables como esta no es fácil, 
es mucho mejor utilizar una sola variable con una lista dentro para declarar una lista vacía.
Todo lo que tenemos que hacer es proporcionar un par de corchetes `[]`, una lista vacía es igual a un par de corchetes,
cada vez que veas una declaración de variable como ésta que utiliza corchetes, debes pensar inmediatamente en ella como una lista.

`lista_vacia = []` o `empty_list = []`

Ahora, ahora si requerimos elementos solo los ingresamos a los corchetes separados por comas.

`user_names = ['John', 'Tere', 'Michael', 'Molly', 'Ramiro', 'Jackson']`

si usas `print()` con una variable de lista dentro obtendras una salida similar: 
> ['John', 'Tere', 'Michael', 'Molly', 'Ramiro', 'Jackson']

En donde John es el primer elemento, Tere es el segundo elemento y así sucesivamente.

Los elementos también están indexados, lo que significa que cada elemento tiene un índice numérico único que puede utilizar/
*RECUERDA: Los índices de lista empiezan en cero y no en uno.
Así que el primer elemento de la lista tiene el índice cero, el segundo elemento tiene el índice uno y así sucesivamente.

Para obtener un elemento específico y no toda la lista, tenemos que proporcionar el índice de elementos dentro de corchetes, así obtendremos la lista completa.

`user_names`

Si deseamos obtener solo un elemento introducimos: `user_names[0]`

Nota: Python también puede buscar indices de manera negativa, por ejemplo: `user_names[-1]` te dara el ultimo elemento de la lista

Sabemos que podemos obtener la lista completa con todos los elementos, si sólo proporcionamos el nombre de la variable que conocemos, también podemos utilizar la indexación para acceder a un solo elemento.
Python también permite acceder a algunos elementos, pero no necesariamente a todos, al mismo tiempo, para ello, utilizamos algo llamado: Slicing 
Para obtener los dos primeros elementos, haremos lo siguiente:  `user_names[0:2]`

Así que cuando hacemos un corte de 0 a 2, esto significa que tomamos el primer elemento, con índice cero, tomamos el segundo elemento con índice uno y luego nos detenemos en el tercer elemento con índice dos y no lo incluimos.

> En otras palabras, el primer índice es inclusivo, el segundo es excluyente.

Toma en cuenta que nunca se produce un error al intentar introducir índices inexistentes con 'Slicing'.