'''
Múltiples parámetros

Ideas clave
*Una función puede depender de múltiples parámetros para llevar a cabo su tarea.

Cómo trabajar con múltiples parámetros

Podemos especificar más de un parámetro en una función separándolos por comas. 
Por ejemplo, para crear una función que sume dos números, escribiremos:

def sumar(a, b):
  print(a + b)


sumar(5, 3) # 8 
sumar(10, 20); # 30 
'''

#Ejercicio
'''
Crea la función restar que dependa de dos parámetros y que imprima la resta de ambos.
'''


#restar(10, 5)
#restar(3, 5)
#restar(9, 4)

# Escribe tu código aquí 

#Primera forma
'''
def restar(a, b):
    print(a - b)

restar(10, 5)
restar(3, 5)
restar(9, 4)
'''


#Segunda forma
def restar(a, b):
    resta = a - b
    print(f"La resta de {a} y {b} es: {resta}")

restar(10, 5)
restar(3, 5)
restar(9, 4)