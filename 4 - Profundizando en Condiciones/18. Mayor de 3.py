'''
Mayor de 3

Ideas clave
*La sentencia if se utiliza para ejecutar código si se cumple una condición.
*La sentencia if...else se utiliza para ejecutar un código si se cumple una condición y otro código si no se cumple.
*El operador lógico && nos permite combinar dos o más condiciones. 
 Cada condición individual debe ser verdadera para que la expresión completa sea verdadera.

Este ejercicio puede ser un poco más complicado que los anteriores. Hay más de una solución y puedes usar cualquier método que hayas aprendido hasta ahora.
'''

#Ejercicio
'''
Crea una función llamada mayorDeTres que dependa de tres parámetros: a, b y c.

Si a es mayor que b y c, la función debe retornar "El primer número es el mayor"
Si b es mayor que a y c, la función debe retornar "El segundo número es el mayor"
Si c es mayor que a y b, la función debe retornar "El tercer número es el mayor"
Si los tres números son iguales, la función debe retornar "Los tres números son iguales"
'''

# Escribe tu código aquí 
def mayorDeTres(a, b, c):
    if a > b and a > c:
        return "El primer numero es el mayor"
    elif b > a and b > c:
        return "El segundo numero es el mayor"
    elif c > a and c > b:
        return "El tercer numero es el mayor"
    else:
        return "Los tres numeros son iguales"
# Fin 
print(mayorDeTres(4,3,2))
print(mayorDeTres(5,6,1))
print(mayorDeTres(9,8,10))
print(mayorDeTres(7,7,7))
