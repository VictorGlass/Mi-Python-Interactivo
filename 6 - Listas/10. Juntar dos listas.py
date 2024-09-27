'''
Juntar dos listas

Ideas clave
*En Python, podemos combinar listas usando el operador + o el método extend().
*La concatenación de listas crea una nueva lista, sin modificar las originales.

Combinando listas en Python

Para combinar listas en Python, podemos usar el operador +:

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2
print(lista3)  # [1, 2, 3, 4, 5, 6]
También podemos usar slicing para excluir elementos a la hora de combinar listas:

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
nueva_lista = lista1[1:] + lista2[1:]
print(nueva_lista)  # [2, 3, 5, 6]
'''

#Ejercicio
'''
Crea una función llamada juntar_arreglos que reciba dos parámetros, arreglo1 y arreglo2, y retorne una nueva lista con los elementos de ambas listas excluyendo el primer elemento de cada una.

Ejemplos:

print(juntar_arreglos([1, 2, 3], [4, 5, 6]))  # [2, 3, 5, 6]
print(juntar_arreglos(["hola", "mundo"], ["desde", "python"]))  # ["mundo", "python"]
Las listas siempre tendrán al menos 2 elementos.
'''

# Escribe tu código aquí
def juntar_arreglos(arreglo1, arreglo2):
    nueva_lista = arreglo1[1:] + arreglo2[:1]
    return nueva_lista

# Fin
print(juntar_arreglos([1,2,3,4], [5,6,7,8]))
print(juntar_arreglos(['a','b','c'], ['d','e','f']))
print(juntar_arreglos(['uno','dos','tres'], ['cuatro','cinco','seis']))

