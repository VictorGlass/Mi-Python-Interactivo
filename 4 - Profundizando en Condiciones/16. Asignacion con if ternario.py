'''
Asignación con if ternario

Ideas clave
*El if ternario es una forma de escribir un if en una sola línea.
*Podemos utilizarlo para ejecutar una instrucción si se cumple una condición y otra si no se cumple.
*También podemos utilizarlo para asignar un valor a una variable dependiendo de una condición.

Asignación con if ternario
Utilizando el operador ternario podemos asginar un valor a una variable dependiendo de una condición.

edad = 18
mensaje = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
En este código, la variable edad tiene un valor de 18. Luego, se evalúa si la variable edad es mayor o igual a 18. 
Si es verdadero, se asigna el mensaje "Eres mayor de edad" a la variable mensaje, de lo contrario, se asigna "Eres menor de edad".

Podemos lograr lo mismo con un if normal:

edad = 18
if (edad >= 18): 
  mensaje = "Eres mayor de edad"
else:
  mensaje = "Eres menor de edad"
'''

#Ejercicio
'''
El siguiente código no funciona como debería. 
El código correcto es 1234, pero el programa muestra "Código incorrecto" y no "Código correcto".

¿Puedes corregirlo?
'''

codigo = "1234"
# Escribe tu código aquí 

mensaje = "Código correcto" if codigo == "1234" else "Código incorrecto"
print(mensaje)

# Fin 
