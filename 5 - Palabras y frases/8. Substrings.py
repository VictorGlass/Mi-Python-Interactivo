'''
Substrings

Ideas clave
*Una parte de una cadena de texto o string suele llamarse substring.
*Podemos obtener un substring utilizando la técnica de slicing (cortes)
*Para hacer un corte, utilizamos la notación de corchetes y dos puntos. 
 Por ejemplo, texto[0:4] nos devolverá los caracteres desde el índice 0 hasta el 4, sin incluir el 4.

Slicing

En algunas ocasiones, necesitamos obtener solo una parte de una cadena de texto, lo que se conoce como una subcadena. 
En Python, utilizamos la técnica de "slicing" para hacer esto, que consiste en cortar la cadena de texto en los puntos que indiquemos. 

Por ejemplo:

texto = "Hola Mundo"
print(texto[0:4]) # Hola
Para realizar un corte, debemos indicar el punto de inicio y el punto final de la cadena que queremos obtener. 
El punto de inicio es la posición del primer carácter que deseamos, y el punto final es la posición del primer carácter que NO queremos incluir. 
Es importante recordar que la posición del primer carácter es 0.

En el ejemplo de slicing, obtenemos los caracteres desde el índice 0 hasta el índice 3, sin incluir el índice 4.
'''


#Ejercicio
'''
Crea una función llamada primeros_caracteres que dependa del parámetro texto y devuelva los primeros 3 caracteres del texto. 
Para simplificar, asumiremos que el texto siempre tiene al menos 3 caracteres.
'''

# Escribe tu código aquí
def primeros_caracteres(texto):
    return texto[0:4]
# Fin
print(primeros_caracteres("Hello"))
print(primeros_caracteres("Lenguaje"))
print(primeros_caracteres("Tutoriales"))

