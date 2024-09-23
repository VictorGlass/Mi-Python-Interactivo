'''
Slicing en listas

Ideas clave
*Las listas en Python permiten almacenar múltiples valores en una sola variable.
*Podemos acceder a elementos individuales de una lista usando índices, comenzando desde 0.
*El slicing nos permite obtener un subconjunto de elementos de una lista.
*Los índices negativos nos permiten acceder a elementos desde el final de la lista.

Slicing en listas

El slicing en una lista funciona de manera similar al slicing en cadenas de texto. 
Podemos obtener un subconjunto de elementos especificando un rango de índices.

frutas = ["manzana", "pera", "uva", "naranja", "kiwi"]
print(frutas[1:4])  # ["pera", "uva", "naranja"]
print(frutas[:3])   # ["manzana", "pera", "uva"]
print(frutas[3:])   # ["naranja", "kiwi"]
print(frutas[::2])  # ["manzana", "uva", "kiwi"]
print(frutas[-2:])  # ["naranja", "kiwi"]
'''

#Ejercicio
'''
Crea una función llamada obtener_subcadena que reciba como parámetro una lista de strings y 
devuelva una nueva lista con los elementos en las posiciones pares (0, 2, 4, etc.) de la lista original.

Tip: Utiliza slicing con paso.

Ejemplo:

print(obtener_subcadena(["a", "b", "c", "d", "e"]))  # ["a", "c", "e"]
'''

#Al utilizar slicing se puede obtener los elementos en las posiciones pares.

# Escribe tu código aquí
def obtener_subcadena(lista):
    #lista[0::2] indica que se comienza en el indice 0 y se toma un elemento cada 2 posiciones
    #lo que corresponde a las posiciones (0,2,4, etc.)
    return lista[0::2] 


# Fin
print(obtener_subcadena(["manzana", "pera", "uva", "naranja", "kiwi", "mango"]))
print(obtener_subcadena(["rojo", "azul", "verde", "amarillo", "negro", "blanco"]))
print(obtener_subcadena(["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]))