'''
Transformando a mayúsculas

Ideas clave
*En Python, tenemos múltiples herramientas para trabajar con cadenas de texto.
*El método upper() nos permite transformar un texto a mayúsculas.

Cadenas de texto

Las cadenas de texto, o strings en inglés, son el tipo de dato que se utiliza para representar texto en Python. 
Las cadenas de texto se pueden definir utilizando comillas simples o dobles.

a = "hola"
b = 'mundo'
A lo largo de los siguientes ejercicios, trabajaremos con cadenas de texto y aprenderemos a manipularlas y transformarlas.

Transformando a mayúsculas
Para transformar una cadena de texto a mayúsculas, utilizaremos el método upper() que nos proporciona Python.

El concepto de método es muy importante en Python y no lo hemos estudiado previamente, 
pero por ahora podemos entenderlo como una función que se aplica a un tipo de dato en particular. 
Por ejemplo, el método upper() es un método que no recibe parámetros y se aplica a los textos, devolviéndonos el texto original en mayúsculas. 
Estudiaremos más a fondo los métodos en el futuro.

texto = "hola mundo"
print(texto.upper()) # HOLA MUNDO

El resultado de upper() es un nuevo texto, por lo que, si queremos guardar el resultado para usarlo posteriormente, debemos guardarlo en una variable.

texto = "hola mundo"
texto_mayusculas = texto.upper()
print(texto_mayusculas) # HOLA MUNDO
'''

#Ejercicio
'''
Crea una función llamada a_mayusculas que reciba dos parámetros, texto1 y texto2. 
La función debe retornar un nuevo texto que sea la concatenación de texto1 y texto2 en mayúsculas, sin espacios adicionales entre ambos textos.

Ejemplo:

print(a_mayusculas("hola", "mundo")) # HOLAMUNDO
'''

# Escribe tu código aquí

def a_mayusculas(texto1, texto2):
    return (texto1 + " " + texto2).upper()

# Fin
print(a_mayusculas("hola", "mundo"))
print(a_mayusculas("cat", "Dog"))
print(a_mayusculas("King", "kong"))
