# Eliminar elementos de la lista

Aprenderemos a eliminar elementos de una lista.

Para ello, vamos a utilizar una nueva palabra `del` es decir, eliminar, su uso es sencillo.
Escribimos `del` y proporcionamos el elemento o elementos de los que queremos deshacernos.

Escribiremos `print(user_names[2])` e imprimiremos la lista ¿Qué resulta?
> Michael

Posteriormente utilizaremos: `del user_names[2]`
Y puedes ver que 'Michael' ha desaparecido de la lista, pero, ¿qué ha pasado con el espacio de la lista con índice dos?
Cuando borramos Michael, resulta que todos los valores a la derecha se desplazan a la izquierda, de modo que no hay huecos ni espacios vacíos en la lista.
Si ahora accedes al nombre de usuario dos, verás que apunta a un nuevo elemento: 'Molly'

Supongamos ahora que queremos mantener los tres primeros elementos de la lista y queremos eliminar los dos restantes.
Podemos usar la instrucción `del` junto con 'Slicing' para hacer eso en una sola operación de `user_names` índice tres e imprimir la lista después.
Esta instrucción significa borrar todos los elementos a partir del índice tres hasta el final de la lista.

`del user_names[3:]`

Esta instrucción deja intactos los tres primeros elementos, los elementos con índices cero uno y dos siguen ahí en la lista.
También puedes borrar todos los elementos de una lista usando un slice con ambos índices omitidos.

`del user_names[:]`

Imprime la lista después y podrás ver una lista vacía como resultado, curiosamente, también puedes utilizar la instrucción `del` para borrar la propia lista,
sólo tienes que proporcionar su nombre sin ningún índice `del user_names`

Y ahora si intentas imprimir la lista en la salida, `print(user_names)` arroja un error porque después de borrar la lista, la variable ya no está disponible.

Ten en cuenta que `del` no es una función, llámala mejor una instrucción, no es una llamada a función porque cada llamada a función requiere un nombre de función seguido de
un par de corchetes.

Y eso es todo por ahora (●'◡'●)