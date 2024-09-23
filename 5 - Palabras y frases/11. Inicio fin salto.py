'''
Inicio fin salto

Ideas clave
*Podemos obtener un substring utilizando la técnica de slicing (cortes)
*Para hacer un corte, utilizamos la notación de corchetes y dos puntos. Por ejemplo, texto[0:4] nos devolverá los caracteres desde el índice 0 hasta el 4, sin incluir el 4.
*Si no especificamos el punto final, el corte se hará hasta el final del texto.
*Podemos hacer un corte indicando un salto. Por ejemplo, texto[0:4:2] nos devolverá los caracteres desde el índice 0 hasta el 4, saltando de 2 en 2.

Ejemplo

texto = "Hola Mundo"
print(texto[0:4:2]) # Hl
Tambien es posile no especificar el punto final, pero si el salto.

texto = "Hola Mundo"
print(texto[1::2]) # oaMno
'''

#Ejercicio
'''
Crea una función que se llame encontrar_secreto que dependa de un parámetro de tipo string y devuelva un nuevo string con un salto de 2.

encontrar_secreto("2s1eecBr1eto") => "secreto"
'''

# Escribe tu código aquí 
def encontrar_secreto(texto):
    #Usar slicing con un salto de 2 caracteres
    return texto[1::2]


# Fin 
print(encontrar_secreto("3t2e1s2t2i2n5g"))
print(encontrar_secreto("8m4y6s4e7c7r8e8t"))
print(encontrar_secreto("9h3i1d4d4e7n8m8e4s9s5a9g8e"))