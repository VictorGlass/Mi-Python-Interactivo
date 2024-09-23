'''
Retornar vs Mostrar

Ideas clave
*Las funciones pueden devolver un valor.
*Retornar un valor no es lo mismo que mostrar un valor.
*En algunos ejercicios te pediremos que muestres un valor y en otros que devuelvas un valor.

Mostrar o devolver

Los valores que muestra una función no necesariamente son los mismos que devuelve.

def sumar(a, b):
    print("La suma es 8")
    return a + b

sumar(2, 2) # La suma es 8

Aquí vemos que la función sumar muestra un mensaje, pero el valor que devuelve es la 
suma de los parámetros a y b. 
Es decir, podemos hacer que la función muestre un mensaje y devuelva un valor diferente.

Este ejemplo es importante para entender que mostrar un valor y devolver un valor no es lo mismo y no están relacionados directamente.

En algunos ejercicios te pediremos que muestres un valor y en otros que devuelvas un valor.

El siguiente ejercicio te ayudará a entender la diferencia entre mostrar y devolver valores.
'''

#Ejercicio
'''
Crea la función sumar_y_duplicar que dependa de dos parámetros, a y b, y que devuelva la suma de ambos multiplicada por 2. 
Adicionalmente, antes de retornar el valor, la función debe mostrar el valor de la suma de la siguiente forma: "La suma es X", donde X es el resultado de la suma.

Ejemplo: sumar_y_duplicar(2, 2) # La suma es 4 sumar_y_duplicar(3, 3) # La suma es 6
'''

#print(sumar_y_duplicar(2, 2)) 
#print(sumar_y_duplicar(3, 3)) 

# Escribe tu código aquí

def sumar_y_duplicar(a, b):
    sumar = a + b
    print(f"La suma de: {a} y {b}, es de: {sumar}")
    return sumar * 2


print(sumar_y_duplicar(2, 2))
print(sumar_y_duplicar(3, 3))



