'''
Largo de una cadena de texto

Ideas clave
*Podemos conocer la longitud de una cadena de texto utilizando la función len() de los strings. Ejemplo: print(len("Hola Mundo")) # 10.

Longitud de una cadena de texto
*La longitud de una cadena de texto es la cantidad de caracteres que tiene.

hola -> 4
mundo -> 5

Función len()
*En Python podemos conocer la longitud de una cadena de texto utilizando la función len().

texto = "Hola Mundo"
print(len(texto)) # 10
Por ejemplo, el texto "Hola Mundo" tiene 10 caracteres. ¡Los espacios también cuentan como caracteres!
'''

#Ejercicio
'''
Crea una función llamada largo_texto que reciba dos parámetros, texto1 y texto2. 
La función debe retornar la suma de las longitudes de texto1 y texto2.

Ejemplo:

print(largo_texto("Hola", "Mundo")) # 9
print(largo_texto("Passport", "1234567890")) # 18
'''

# Escribe tu código aquí
def largo_texto(texto1, texto2):
    return len(texto1) + len(texto2)

# Fin
print(largo_texto("hola","mundo"))
print(largo_texto("día","noche"))
print(largo_texto("javascript","sqlite"))
