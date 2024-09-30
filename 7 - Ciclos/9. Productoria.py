'''
Productoria

Ideas clave
*Con while podemos repetir un bloque de código mientras una condición sea verdadera.
*Es importante asegurarse de que la condición del while eventualmente se vuelva falsa para evitar bucles infinitos.

¿Qué es la productoria?

La productoria es un concepto matemático que se utiliza para representar la multiplicación de una serie de números. 
Así como la sumatoria se utiliza para representar la suma de una serie de números, 
la productoria se utiliza para representar la multiplicación de una serie de números.

Por ejemplo, si se pide la productoria de los números del 1 al 5, el resultado sería 120, ya que 1 * 2 * 3 * 4 * 5 es igual a 120.

Tip: La productoria es similar a la sumatoria pero implica multiplicar en lugar de sumar.
'''

#Ejercicio
'''
Crea una función llamada productoria que reciba un número como parámetro y retorne la productoria de los números del 1 al número ingresado.

Por ejemplo, si el número ingresado es 5, la función debe retornar 120. Si el número ingresado es 10, la función debe retornar 3628800.
'''

# Escribe tu código aquí 
def productoria(numero):
    contador = 1
    multiplicar = 1

    while contador <= numero:
        multiplicar = multiplicar * contador
        contador +=1
    return multiplicar

# Fin
print(productoria(9))
print(productoria(12))
print(productoria(7))
