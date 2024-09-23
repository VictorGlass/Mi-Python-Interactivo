'''
Otros tipos de comparadores

Ideas clave
*Podemos comparar valores utilizando operadores de comparación.
*El operador de igualdad == compara dos valores y nos dice si son iguales o no.
*Existen operadores de comparación como mayor que > y menor que <.
*El operador de mayor o igual que >= compara dos valores y nos dice si el primero es mayor o igual al segundo, 
y el operador de menor o igual que <= compara dos valores y nos dice si el primero es menor o igual al segundo.
*El operador de desigualdad != compara dos valores y nos dice si son diferentes.

Operadores de comparación

Existen varios operadores de comparación que podemos utilizar en Python. 
A continuación, se muestra una tabla con los operadores de comparación más comunes:

Operador	Tipo de comparación	Ejemplo	Resultado
==	Igualdad	2 == 2	true
>	Mayor que	3 > 2	true
<	Menor que	2 < 3	true
>=	Mayor o igual que	3 >= 3	true
<=	Menor o igual que	3 <= 3	true
!=	Distinto	1 != 2	true

'''

#Ejercicio

'''
Un programador ha escrito esta sección de código para evaluar si tiene suficiente dinero 
para comprar un producto. 
Sin embargo, el programa tiene un caso no contemplado. ¿Puedes corregirlo?

Tip: El caso no contemplado puede ser resuelto utilizando uno de los operadores 
de comparación mencionado en la tabla anterior.
'''

#dinero = 500
#costo = 500
#me_alcanza = dinero > costo # Modifica esta línea
#print(me_alcanza)

dinero = 500
costo = 500
me_alcanza = dinero >= costo
print(me_alcanza)