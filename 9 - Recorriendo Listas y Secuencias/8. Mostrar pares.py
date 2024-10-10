'''
Mostrar pares

Ideas clave
*En Python, el ciclo for puede iterar directamente sobre los elementos de una lista.
*La sentencia if se utiliza para ejecutar código si se cumple una condición.
*El operador resto % nos entrega el resto de la división de dos números y lo podemos utilizar para determinar si un número es par o impar.

Ejemplo de for
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)
'''

#Ejercicio
'''
Aplica lo aprendido para crear una función llamada mostrar_pares que reciba una lista de números 
y muestre en consola todos los números pares de la lista. Utiliza un ciclo for.
'''

# Escribe tu código aquí
def mostrar_pares(lista):
    for numeros in lista:
        if numeros % 2 == 0:
            print(numeros)



# Fin
mostrar_pares([1, 2, 3, 4, 5])
mostrar_pares([-3, -2, -1, 0, 1, 2, 3])
