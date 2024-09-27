'''
Rotar a la izquierda

Ideas clave
*Podemos usar el método pop(0) para eliminar y obtener el primer elemento de una lista.
*El método append() nos permite agregar un elemento al final de una lista.
*Podemos combinar estos métodos para rotar los elementos de una lista.
'''

#Ejercicio
'''
Crea una función llamada rotar_a_la_izquierda que reciba como parámetro una lista. 
La función debe eliminar el primer elemento de la lista y luego agregar este mismo elemento al final. 
Retorna la lista modificada.

Ejemplos:

print(rotar_a_la_izquierda([1, 2, 3, 4]))  # [2, 3, 4, 1]
print(rotar_a_la_izquierda(["Juan", "Pedro", "Ana", "Luis"]))  # ["Pedro", "Ana", "Luis", "Juan"]
'''

# Escribe tu código aquí
def rotar_a_la_izquierda(lista):
    if lista:
        elimina_primer_elemento = lista.pop(0)
        lista.append(elimina_primer_elemento)
    return lista

# Fin
print(rotar_a_la_izquierda(['uno','dos','tres','cuatro']))
print(rotar_a_la_izquierda([1,2,3,4]))
print(rotar_a_la_izquierda(['perro','gato','pájaro','pez']))
