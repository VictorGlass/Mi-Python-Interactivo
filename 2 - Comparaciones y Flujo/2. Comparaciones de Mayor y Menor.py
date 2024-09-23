'''
Comparaciones de mayor y menor

Ideas clave:
*Podemos comparar valores utilizando operadores de comparación.
*El operador de igualdad == compara dos valores y nos dice si son iguales o no.
*Existen operadores de comparación como mayor que > y menor que <.

Operador de mayor que

El operador mayor que > compara dos valores:

*Si el primer valor es mayor que el segundo, el resultado es verdadero o en inglés True.
*Si el primer valor no es mayor que el segundo, el resultado es falso en inglés False.

print(2 > 3) # False 
print(3 > 2) # True 

Operador de menor que

También existe el operador de menor que <, el cual compara dos valores, 
resultando en true si el primer valor es menor que el segundo, y false si no lo es.

print(2 < 3) # True 
print(3 < 2) # False
'''

#Ejercicio
'''
Un programador ha escrito el siguiente código para comparar dos números. 
Sin embargo, el programa no está funcionando correctamente. 
¿Puedes corregirlo únicamente cambiando el signo de comparación?
'''

#a = 4
#b = 3
#c = a < b  # Modifica esta línea
#print("a es mayor que b: " + str(c))

a = 4
b = 3
c = a > b
print("a es mayor que b: " + str(c))
