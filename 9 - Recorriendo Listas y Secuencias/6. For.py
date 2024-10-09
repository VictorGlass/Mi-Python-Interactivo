'''
For

Ideas clave**
*En Python, el ciclo for puede iterar directamente sobre los elementos de una lista.
*Este enfoque es más simple y directo cuando queremos procesar cada elemento de una lista.
*Es especialmente útil cuando no necesitamos el índice de los elementos durante la iteración.

Recorriendo listas con for

En Python, el ciclo for es muy versátil y puede iterar directamente sobre los elementos de una lista

for elemento in lista:
    # Bloque de código

En cada iteración del ciclo, la variable elemento toma el valor del siguiente elemento en la lista. 
Esto hace que el código sea más legible y directo cuando queremos procesar cada elemento de una lista.

Por ejemplo, si queremos imprimir cada elemento de una lista de números:

numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)
Este código imprimirá cada número en la lista en una línea separada.
'''

#Ejercicio
'''
Crea una función llamada imprimir_lista que reciba como parámetro una lista de números y muestre en consola cada número de la lista utilizando la instrucción for.

Ejemplo:

imprimir_lista([1, 2, 3, 4, 5])
"""
1
2
3
4
5
"""
'''

# Escribe tu código aquí
def imprimir_lista(lista):
    for numero in lista:
        print(numero)

# Fin
imprimir_lista(["Manzana", "Banana", "Cereza", "Dátil"])
imprimir_lista([10, 20, 30, 40, 50])
