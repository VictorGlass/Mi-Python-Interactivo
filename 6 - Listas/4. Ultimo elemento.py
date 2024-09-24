'''
Último elemento

Ideas clave
*Las listas permiten guardar múltiples valores.
*Podemos acceder a uno de estos valores utilizando la posición que ocupa dentro de la lista. Esta posición recibe el nombre de índice.
*El primer elemento de una lista tiene un índice de 0.
*Podemos determinar la longitud de una lista utilizando la función len().
*El último elemento de una lista es el elemento en la posición len(lista) - 1.
*Otra forma de acceder al último elemento es utilizando el índice -1.

Encontrar el último elemento de una lista

Debido a que el primer elemento de una lista es el elemento en la posición 0, 
el último elemento de una lista es el elemento en la posición len(lista) - 1.

nombres = ["Juan", "Pedro", "Ana", "Luis"]
print(nombres[len(nombres) - 1])  # Luis

nombres = ["Juan", "Pedro", "Ana", "Luis", "Carlos", "Maria"]
print(nombres[len(nombres) - 1])  # Maria
También es posible acceder al último elemento de una lista utilizando el índice -1.

nombres = ["Juan", "Pedro", "Ana", "Luis", "Carlos", "Maria"]
print(nombres[-1])  # Maria
'''

#Ejercicio
'''
Crea una función llamada ultimo_y_primero que reciba una lista y retorne la concatenación del último y el primer elemento de la lista.

Ejemplo:

ultimo_y_primero(["Juan", "Pedro", "Ana", "Luis"])  # LuisJuan
ultimo_y_primero(["Azul", "Rojo", "Verde", "Amarillo"])  # AmarilloAzul
Puedes asumir que dentro de la lista siempre habrá al menos un elemento y que todos los elementos serán de tipo string.
'''


# Escribe tu código aquí
def ultimo_y_primero(lista):
    return lista[0] + " " + lista[-1]


# Fin
print(ultimo_y_primero(["perro", "gato", "delfin", "tortuga"]))
print(ultimo_y_primero(["e", "t", "r", "z"]))
print(ultimo_y_primero(["ruby", "javascript", "python", "c", "c#", "java"]))
