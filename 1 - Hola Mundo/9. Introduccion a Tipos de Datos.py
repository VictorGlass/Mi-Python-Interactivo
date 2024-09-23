'''
Introducción a tipos de datos

Idea clave
*El resultado de las operaciones dependen de los tipos de datos involucrados.

Tipos de datos

En Python, existen diferentes tipos de datos. Hasta ahora, hemos utilizado dos tipos: 
números enteros (ints) y cadenas de texto (string). Sin embargo, hay muchos otros tipos de datos que exploraremos más adelante.

print(2 + 2) # 4
print("hola " + "mundo") # hola mundo
print("2" + "2") # 22

*En el primer caso, sumamos dos números enteros, obteniendo como resultado 4.
*En el segundo caso, concatenamos dos cadenas de texto, resultando en "hola mundo".
*En el tercer caso, también concatenamos dos cadenas de texto, lo que produce "22".
*Este comportamiento también se aplica cuando operamos con variables. Por ejemplo:

a = "2"
b = "2"
print(a + b) # "22"
En Python hay tipos de datos que no se pueden mezclar. Por ejemplo, si intentamos sumar un número y una cadena de texto, obtendremos un error:

a = 2
b = "2"
print(a + b) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
Por lo tanto, es importante prestar atención al tipo de datos que estamos utilizando para evitar errores.
'''

#Ejercicio

'''
Modifica el valor asignado a la variable a para que el resultado sea el número 4.
'''

#a = "2";  # Modifica esta línea
#b = 2;
#print(a + b);

a = 2
b = 2
print(a + b)