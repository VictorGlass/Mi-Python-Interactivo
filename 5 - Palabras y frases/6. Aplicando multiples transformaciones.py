'''
Aplicando múltiples transformaciones

Ideas clave
*En Python, tenemos múltiples herramientas para trabajar con cadenas de texto.
*El método upper() nos permite transformar un texto a mayúsculas.
*El método lower() nos permite transformar un texto a minúsculas.
*El método strip() nos permite eliminar los espacios innecesarios al inicio y al final de una cadena de texto.
*Podemos aplicar múltiples transformaciones sucesivas a una cadena de texto.

Aplicando múltiples transformaciones

Es posible combinar múltiples transformaciones. Por ejemplo, podemos limpiar los espacios innecesarios de un texto y luego transformarlo a mayúsculas. Para ello:

texto = "   hola mundo   "
texto_limpio = texto.strip()
texto_mayusculas = texto_limpio.upper()
print(texto_mayusculas) # HOLA MUNDO
También podemos hacer lo mismo en una sola línea:

texto = "   hola mundo   "
print(texto.strip().upper()) # HOLA MUNDO
'''

#Ejercicio
'''
Crea una función llamada limpiar_y_mayusculas que reciba dos parámetros, texto1 y texto2. 
La función debe retornar un nuevo texto que sea la concatenación de texto1 y texto2 donde ambos textos estén en mayúsculas y 
limpios de espacios innecesarios al inicio y al final.

Ejemplo:

print(limpiar_y_mayusculas("   hola", "mundo   ")) # HOLAMUNDO
'''


# Escribe tu código aquí

def limpiar_y_mayusculas(texto1, texto2):
    return (texto1.strip() + texto2.strip()).strip()

# Fin
print(limpiar_y_mayusculas("  hola","mundo"))
print(limpiar_y_mayusculas("vaso ","  agua"))
print(limpiar_y_mayusculas("sal  ","    pimienta"))