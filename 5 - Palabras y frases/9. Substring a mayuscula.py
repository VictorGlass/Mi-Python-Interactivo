'''
Substring a mayúscula

Ideas clave
*En Python, tenemos múltiples herramientas para trabajar con cadenas de texto.
*La técnica de slicing nos permite obtener una substring o una parte de una cadena de texto.
*El método upper() nos permite transformar un texto a mayúsculas.

A continuación, combinaremos la técnica de slicing con el método upper estudiado previamente para obtener un substring en mayúsculas.
'''

#Ejercicio
'''
Crea una función llamada primeros_caracteres_mayusculas que dependa del parámetro texto y devuelva los 5 primeros caracteres del texto en mayúsculas. 
Para simplificar, asumiremos que el texto siempre tiene al menos 5 caracteres.
'''

# Escribe tu código aquí
def primeros_caracteres_mayusculas(texto):
    return texto[0:5].upper()


# Fin
print(primeros_caracteres_mayusculas("Hola Mundo"))
print(primeros_caracteres_mayusculas("Bye bye"))
print(primeros_caracteres_mayusculas("Tutoriales"))
