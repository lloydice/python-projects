# Agregar nuevos elementos a la lista

Los métodos son un tipo específico de funciones, se puede decir que un método es propiedad de los datos para los que trabaja.
Los métodos existen junto a los datos a los que pertenecen, si no hay datos, no puedes usar sus métodos.

Digamos que tenemos la siguiente lista con enteros, en donde calificamos celulares en una escala del 0 al 10.
`phone_ratings = [8, 7, 6, 3, 5]`
Supon entonces que una persona probo el télefono y quiere darle otra calificación (8) para eso utilizaremos un método llamado `Append`.
`phone_ratings.append(8)`
Y ahora vamos a imprimir las valoraciones de los télefonos después de esta operación.
`print(phone_ratings)`
Y puedes ver el nuevo valor de '8' al final de la lista.
> [8, 7, 6, 3, 5, 8]

Recuerda: `Append` es un método que pertenece a la lista de clasificación de télefonos, puedes ver que un método se invoca usando 
su nombre y un par de corchetes con argumentos dentro, pero a diferencia de las funciones normales, 
los métodos se invocan con un punto después de los datos sobre los que trabajan `phone_ratings.append` en otras palabras, 
no puedes llamar a append como a print o input ya que te encontrarias con un error.
Ten en cuenta lo siguiente.

* Los métodos son funciones que pertenecen a datos específicos.

Existe otro método que se puede utilizar para añadir un elemento en otros lugares de la lista.
`phone_ratings = [8, 7, 6, 3, 5]`
TEndremos de nuevo el valor inicial de las valoraciones de los télefonos, y ahora usaremos el siguiente punto de valoración insertando dentro un uno y nueve.
`phone_ratings.insert(1,9)`
Y vamos a imprimir la lista después de esta operación.
`print(phone_ratings)`
Y ahora puedes ver un nuevo valor nueve en el índice, uno entre los antiguos valores de ocho y siete de la lista original.
> [8, 9, 7, 6, 3, 5]
Esta invocación al método añade el valor de nueve indicandole en que parte del indice deseas introducir el valor todos los demás valores se desplazan
a la derecha para hacer sitio a este nuevo valor.