'''
Mayor de 2

Ideas clave
*La sentencia if se utiliza para ejecutar código si se cumple una condición.
*La sentencia if...else se utiliza para ejecutar un código si se cumple una condición y otro código si no se cumple.

Apliquemos lo aprendido.
'''

#Ejercicio
'''
Crea una función llamada mayorQue que dependa de dos parámetros : a y b

Si a es mayor que b, la función debe retornar "El primer número es mayor que el segundo"
Si b es mayor que a, la función debe retornar "El segundo número es mayor que el primero"
Si ambos números son iguales, la función debe retornar "Ambos números son iguales"
'''

# Escribe tu código aquí 
def mayorQue(a, b):
    if a > b:
        return "El primer numero es mayor que el segundo"
    elif b > a:
        return "El segundo numero es mayor que el primero"
    elif a == b:
        return "Ambos numeros son iguales"
    else:
        return "Ingresa un numero valido"
# Fin 
print(mayorQue(3,5))
print(mayorQue(6,3))
print(mayorQue(5,5))