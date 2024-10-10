'''
Mostrar mayores

Ideas clave**
*En Python, el ciclo for puede iterar directamente sobre los elementos de una lista.
*Este enfoque es más simple y directo cuando queremos procesar cada elemento de una lista.
*Es especialmente útil cuando no necesitamos el índice de los elementos durante la iteración.

Ejemplo de for

numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)
'''

#Ejercicio
'''
Aplica lo aprendido para crear una función llamada mostrar_mayores que reciba una lista de 
números y un número n y muestre en consola todos los números mayores a n utilizando un ciclo for.
'''

# Escribe tu código aquí

def mostrar_mayores(lista, n):
    for numero in lista:
        if numero > n:
            print(numero)

# Fin
mostrar_mayores([1, 2, 3, 4, 5], 2)
print()
mostrar_mayores([10, 20, 30, 40, 50], 25)