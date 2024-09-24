'''
Largo de una lista

Ideas clave
*Las listas permiten guardar múltiples valores.
*Podemos acceder a uno de estos valores utilizando la posición que ocupa dentro de la lista. Esta posición recibe el nombre de índice.
*El primer elemento de una lista tiene un índice de 0.
*Podemos determinar la longitud de una lista utilizando la función len().

Longitud de una lista
En Python, podemos determinar la cantidad de elementos que tiene una lista ya creada utilizando la función len().

nombres = ["Juan", "Pedro", "Ana", "Luis"]
print(len(nombres))  # 4
lista_vacia = []
print(len(lista_vacia))  # 0

Los conceptos de funciones y métodos son similares. Por ahora, solo es importante destacar que las funciones se llaman directamente, 
por ejemplo len(), mientras que los métodos se llaman sobre un objeto, por ejemplo nombres.append(). 
Más adelante profundizaremos en las diferencias entre ambos.
'''

#Ejercicio
'''
Crea una función llamada largo_lista que reciba un parámetro llamado nombres. 
La función debe retornar el texto "muchos" si hay más de 5 elementos en la lista, en caso contrario debe retornar "pocos".

Ejemplo:

largo_lista(["Juan", "Pedro", "Ana", "Luis"])  # pocos
largo_lista(["Juan", "Pedro", "Ana", "Luis", "Carlos", "Maria"])  # muchos
'''

# Escribe tu código aquí
def largo_lista(nombres):
    if len(nombres) > 5:
        return "muchos"
    else:
        return "pocos"

# Fin
print(largo_lista([3, 4, 1, 5]))
print(largo_lista(["e", "t", "r"]))
print(largo_lista(["ruby", "javascript", "python", "c", "c#", "java"]))
