'''
Slice hasta el final

Ideas clave
*Una parte de una cadena de texto o string suele llamarse substring.
*Podemos obtener un substring utilizando la técnica de slicing (cortes)
*Para hacer un corte, utilizamos la notación de corchetes y dos puntos. 
 Por ejemplo, texto[0:4] nos devolverá los caracteres desde el índice 0 hasta el 4, sin incluir el 4.
*Si no especificamos el punto final, el corte se hará hasta el final del texto.

Ejemplo
texto = "Hola Mundo"
print(texto[2:4]) # la
print(texto[2:]) # la Mundo
'''

#Ejercicio
'''
Crea una función llamada exceptoLosPrimeros que reciba dos parámetros: texto y cantidad. 
La función debe retornar el texto sin los primeros caracteres, donde la cantidad de caracteres a omitir es el segundo parámetro.

Ejemplo:

exceptoLosPrimeros("Hola Mundo", 5) # Mundo
exceptoLosPrimeros("Hola Mundo", 2) # la Mundo
'''

# Escribe tu código aquí 
def exceptoLosPrimeros(texto, cantidad):
    return texto[cantidad:]
# Fin 
print(exceptoLosPrimeros("Hola Mundo",6))
print(exceptoLosPrimeros("Programación en Javascript",8))
print(exceptoLosPrimeros("Tutoriales",3))
