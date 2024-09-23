'''
Limpiando espacios en un texto

Ideas clave
*En Python, tenemos múltiples herramientas para trabajar con cadenas de texto.
*El método strip() nos permite eliminar los espacios innecesarios al inicio y al final de una cadena de texto.

Limpiando espacios en un texto

Podemos limpiar los espacios en blanco al inicio y al final de un texto utilizando el método strip().

texto = "   hola mundo   "
print(texto.strip()) # hola mundo
'''

#Ejercicio
'''
Crea una función llamada limpiar_texto que reciba dos parámetros, texto1 y texto2. 
La función debe retornar un nuevo texto que sea la concatenación de texto1 y texto2 donde ambos textos estén limpios de espacios innecesarios al inicio y al final.
'''

# Escribe tu código aquí
def limpiar_texto(texto1, texto2):
    return (texto1).strip() + (texto2).strip()

# Fin
print(limpiar_texto("  hola","  mundo"))
print(limpiar_texto("vaso   ","agua    "))
print(limpiar_texto("   sal   ","   pimienta "))

