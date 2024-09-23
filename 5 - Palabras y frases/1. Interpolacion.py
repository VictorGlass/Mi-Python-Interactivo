'''
Interpolación

Ideas clave
*Las f-strings en Python permiten insertar valores de variables directamente en strings.
*Se crean colocando 'f' antes de las comillas del string.
*Las variables o expresiones se insertan entre llaves {} dentro del f-string.
*Las f-strings hacen el código más legible y conciso.

## Interpolación de strings con f-strings

En Python, las f-strings (formatted string literals) proporcionan una manera fácil y legible 
de insertar valores de variables en strings. Se crean añadiendo 'f' o 'F' antes de las comillas que abren el string.

Veamos algunos ejemplos simples:

nombre = "Ana"
edad = 25
print(f"Hola, me llamo {nombre} y tengo {edad} años.")
# Imprime: Hola, me llamo Ana y tengo 25 años.

x = 10
y = 5
print(f"La suma de {x} y {y} es {x + y}.")
# Imprime: La suma de 10 y 5 es 15.
Las f-strings pueden contener expresiones Python, lo que las hace muy versátiles:

precio = 19.99
cantidad = 3
total = precio * cantidad
print(f"El total de tu compra es ${total:.2f}")
# Imprime: El total de tu compra es $59.97

En este último ejemplo, .2f especifica que queremos mostrar el número con dos decimales.
'''

#Ejercicio
'''
Crea una función llamada presentar_numero que reciba un número como parámetro. 
La función debe imprimir un mensaje que diga "El número es X", donde X es el número recibido. 
Usa f-strings para crear el mensaje.

Ejemplo:

presentar_numero(42)
# Debe imprimir: El número es 42

presentar_numero(3.14)
# Debe imprimir: El número es 3.14
Tip: Recuerda usar 'f' antes de las comillas para crear un f-string, y coloca la variable entre llaves {} dentro del string.
'''

# Escribe tu código aquí
def presentar_numero(numero):
    print(f"El numero es {numero}")


# Fin
presentar_numero(56)
presentar_numero(9.3)
