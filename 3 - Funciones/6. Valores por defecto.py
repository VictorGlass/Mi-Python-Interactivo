'''
Valores por defecto

En python, una función puede tener valores por defecto en sus parámetros. 
Esto significa que si al llamar a la función no se le pasa un valor para un parámetro, 
este tomará el valor por defecto que se le haya asignado.

*Veamos un ejemplo:

def saludar(nombre="Mundo"):
  print("Hola ", nombre)

saludar("Juan") # Hola Juan
saludar() # Hola Mundo
Puede haber mas de un parámetro con valor por defecto.

def saludar(nombre="Mundo", saludo="Hola"):
  print(saludo, nombre)

saludar("Juan") # Hola Juan
saludar() # Hola Mundo

*Si hay parámetros sin valor por defecto, estos deben ir al principio y los que tienen valor por defecto al final.

def saludar(saludo, nombre="Mundo"):
  print(saludo, nombre)

saludar("Hola", "Juan") # Hola Juan
saludar() # Error  saludar() missing 1 required positional argument: 'saludo'
'''

#Ejercicio
'''
Crea la función suma que reciba tres parámetros y muestre la suma de estos. 
Si no se le pasa un valor a alguno de los parámetros, este debe tomar el valor por defecto de 0.

Ejemplo:

suma(5, 3) # Es igual a suma(5, 3) # 8
suma(10) # Es igual a suma(10, 0) # 10
suma() # Es igual a suma(0, 0) # 0
'''
 
#suma(10, 5, 2)
#suma(3)
#suma(9, 4)

# Escribe tu código aquí

def suma(a=0, b=0, c=0):
    sumar = a + b + c
    if a == 0 and b == 0 and c == 0:
        print("Lo lamento no es posible llevar a cabo la suma")
    else:
        print(f"La suma de los valores: {a}, {b} y {c} es: {sumar}")

suma(5, 3)
suma(10)
suma()
