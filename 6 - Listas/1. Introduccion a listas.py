'''
Introducción a listas

Ideas clave
*Las listas permiten guardar múltiples valores.
*Podemos acceder a uno de estos valores utilizando la posición que ocupa dentro del arreglo. Esta posición recibe el nombre de índice.
*El primer elemento de un arreglo tiene un índice de 0.
*Si tenemos un arreglo llamado nombres, podemos acceder al primer elemento con nombres[0], al segundo con nombres[1], y así sucesivamente.

¿Qué son las Listas?

Las listas son una estructura de datos que nos permite guardar múltiples valores juntos, 
como por ejemplo, múltiples nombres de clientes, temperaturas de diferentes ciudades y teléfonos de contactos, entre otros.

Para propósitos prácticos, las listas en Python son similares a los arreglos en otros lenguajes de programación.

¿Cómo se crean una lista?

Para crear una lista, utilizamos corchetes [] y separamos los elementos con comas ,. Por ejemplo:

nombres = ["Juan", "Pedro", "Ana", "Luis"]
numeros = [1, 2, 3, 4, 5]
En este ejemplo, estamos guardando un conjunto de nombres en la variable nombres y un conjunto de números en la variable numeros.

Acceder a los elementos de una lista
Podemos acceder a uno de estos valores utilizando la posición que ocupa dentro de la lista. 
Esta posición recibe el nombre de índice. El primer elemento de una lista en Python tiene un índice de 0, el segundo un índice de 1, el tercero un índice de 2 y así sucesivamente. Por ejemplo:

nombres = ["Juan", "Pedro", "Ana", "Luis"]
print(nombres[0])  # Juan
print(nombres[1])  # Pedro
print(nombres[2])  # Ana
print(nombres[3])  # Luis
'''

#Ejercicio
'''
Crea una función llamada primer_elemento que reciba una lista y retorne el primer elemento del lista.

Ejemplo:

primer_elemento(["Juan", "Pedro", "Ana", "Luis"])  # Juan
primer_elemento([1, 2, 3, 4, 5])  # 1
'''

# Escribe tu código aquí
def 

# Fin
print(primer_elemento([3, 4, 1, 5]))
print(primer_elemento(["e", "t", "r"]))
print(primer_elemento(["ruby", "javascript", "python"]))
