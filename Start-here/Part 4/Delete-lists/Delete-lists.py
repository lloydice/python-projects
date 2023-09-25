user_names = ['John', 'Tere', 'Michael', 'Molly', 'Ramiro', 'Jackson', 'Joaquin']

print(user_names) #Imprime los valores que hay dentro de la lista
print(user_names[2]) #Imprime el tercer elemento de la lista
del user_names[2] #Elimina el tercer elemento de la lista

print(user_names) #Imprime los valores que hay dentro de la lista
print(user_names[2]) #Imprime el tercer elemento de la lista ¿Qué notas diferente? 

del user_names[3:] #Elimina después del tercer elemento de la lista
print(user_names) #Imprime los valores que hay dentro de la lista


del user_names[:] #Elimina todos los elementos de la lista
print(user_names) #¿Qué notas diferente ahora?

#Para probar este último espacio, elimina el # para probar el código
#del user_names #Elimina la propia lista
#print(user_names) #¿Qué notas diferente ahora?
