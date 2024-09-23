'''
Combinando transformaciones

Ideas clave
En Python, tenemos múltiples herramientas para trabajar con cadenas de texto.
El método upper() nos permite transformar un texto a mayúsculas.
El método lower() nos permite transformar un texto a minúsculas.

Apliquemos lo aprendido.
'''

#Ejercicio
'''
Crea una función llamada transformar que reciba dos parámetros, texto1 y texto2. 
El primer parámetro debe ser transformado a mayúsculas y el segundo a minúsculas. 
La función debe retornar un nuevo texto que sea la concatenación de texto1 y texto2 sin espacios adicionales entre ambos textos.

Ejemplo:

transformar("hola", "MUNDO") # HOLAmundo
'''

# Escribe tu código aquí
def transformar(texto1, texto2):
    return (texto1).upper() + (texto2).lower()
# Fin

print(transformar("hola", "mundo"))
print(transformar("cat", "Dog"))
print(transformar("KING", "KONG"))
