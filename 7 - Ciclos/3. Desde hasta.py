'''
Desde hasta

Ideas clave
*Con while podemos repetir un bloque de código mientras una condición sea verdadera.
*Es importante asegurarse de que la condición del while eventualmente se vuelva falsa para evitar bucles infinitos.

Previamente mencionamos que podemos utilizar el ciclo while para contar del 1 al 10 de la siguente forma:

contador = 1
while contador <= 10:
    print(contador)
    contador = contador + 1  # Incrementamos el contador en 1
print("Fin del ciclo")
'''

#Ejercicio
'''
El siguiente es un ejercicio de intuición y lógica. Sí necesitáramos ahora crear un función que partiera desde un número distinto a 1, ¿Qué cambio harías en el código?

Crea una función llamada desde_hasta que reciba 2 parámetros, desde y hasta. Muestra en consola todos los números entre medio. Por ejemplo:


desde_hasta(5, 10)
5
6
7
8
9
10
'''

# Escribe tu código aquí 
def desde_hasta(valor1, valor2):

    contador = valor1
    while contador <= valor2:
        print(contador)
        contador +=1
    print("Fin del ciclo")

# Fin 
desde_hasta(3,7)
desde_hasta(15,21)
desde_hasta(8,13)
