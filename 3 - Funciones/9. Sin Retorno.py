'''
Sin retorno

Ideas clave
#Retornar un valor no es lo mismo que mostrar un valor.
#Si se pide mostrar un valor debemos utilizar print.
#Si se pide retornar un valor, debemos utilizar return.
#Si el return no se especifica, la función retornará None.

Sin retorno

En Python, cuando una función no tiene explícitamente un return, la función retornará None.

def sumar():
    2 + 2  # Realiza una operación pero no devuelve nada

print(sumar())  # None
Comparemos el código anterior con uno que sí tiene un return.

def sumar():
    return 2 + 2  # Devuelve el resultado de la operación

print(sumar())  # 4

¿Por qué una función retorna o no retorna algo?

Estas son decisiones que se toman al crear una función. Tiene sentido que una función no retorne 
algún valor si su propósito es simplemente realizar una acción, como mostrar un mensaje en pantalla, 
mientras que las funciones que realizan cálculos o procesos generalmente retornan un valor para que 
pueda ser utilizado en otro lugar del programa.
'''

#Ejercicio
'''
El siguiente código es una función que convierte grados Celsius a Fahrenheit, 
sin embargo, tiene un problema que debes corregir. 
Utiliza lo aprendido en esta lección para corregirlo.
'''

#def a_fahrenheit(celsius):
#  celsius * 9 / 5 + 32  # Agregar return para devolver el resultado

# Fin

#r1 = a_fahrenheit(0)
#r2 = a_fahrenheit(100)
#print("El agua se congela a " + str(r1) + " grados Fahrenheit")
#print("El agua hierve a " + str(r2) + " grados Fahrenheit")

#SOLUCION:

def a_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

r1 = a_fahrenheit(0)
r2 = a_fahrenheit(100)

print(f"El agua se congela a: {r1} grados Fahrenheit y el agua hierve a: {r2} grados Fahrenheit")