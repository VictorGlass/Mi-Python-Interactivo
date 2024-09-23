'''
Transformando a minúsculas

Ideas clave
*En Python, tenemos múltiples herramientas para trabajar con cadenas de texto.
*El método upper() nos permite transformar un texto a mayúsculas.
*El método lower() nos permite transformar un texto a minúsculas.

Transformando a minúsculas

Para transformar un texto a minúsculas en Python utilizamos el método lower() de los strings. 
Este método no recibe parámetros y devuelve el texto original en minúsculas.

texto = "HOLA MUNDO"
print(texto.lower()) # hola mundo

El resultado de lower() es un nuevo texto, por lo que, si queremos guardar el resultado 
para usarlo posteriormente, debemos guardarlo en una variable.

texto = "HOLA MUNDO"
texto_minusculas = texto.lower()
print(texto_minusculas) # hola mundo
'''

#Ejercicio
'''
Crea una función llamada a_minusculas_primero que reciba dos parámetros, texto1 y texto2. 
La función debe retornar un nuevo texto que sea la concatenación de texto1 y texto2, 
en donde texto1 esté transformado a minúsculas y texto2 se mantenga sin transformación.

Ejemplo:

print(a_minusculas_primero("HOLA", "MUNDO")) # holaMUNDO
'''

# Escribe tu código aquí
def a_minusculas_primero(texto1, texto2):
    return (texto1).lower() + texto2

# Fin
print(a_minusculas_primero("HOLA", "MUNDO"))
print(a_minusculas_primero("CAT", "dog"))
print(a_minusculas_primero("King", "KONG"))
