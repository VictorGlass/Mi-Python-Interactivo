'''
Indentando con espacios

Ideas clave:
*Los programas se ejecutan de manera lineal, de arriba a abajo.
*Podemos cambiar el flujo de un programa utilizando condiciones.
*La indentación es la cantidad de espacios en blanco que hay al principio de una línea de código.
*La indentación en Python indica que una línea de código está dentro de un if. Formalizaremos esta idea más adelante.

Qué es la indentación
La indentación es la cantidad de espacios en blanco que hay al principio de una línea de código. 
En Python, la indentación es muy importante porque indica que una línea de código está dentro de un if, 
pero para que funcione correctamente, debemos ser consistentes con el uso de espacios. 
A continuación, se muestra un ejemplo de código con una indentación inconsistente:

codigo = "1234" 
if codigo == "1234": 
  print("Código correcto")
    print("Segundo mensaje pero agregamos mas espacios")

Al ejectuar el código anterior, obtendremos el siguiente error: 
IndentationError: unexpected indent. 
Este error se produce porque estamos ocupando una indentación inconsistente. 
El primer print tiene dos espacios y el segundo tiene cuatro. Para corregirlo, 
ambos deben tener la misma cantidad de espacios sin importar si son dos, cuatro u otra cantidad.
'''

#Ejercicio
'''
Modifica el siguiente código para que funcione.
'''

#codigo = "1234" 
#if codigo == "1234": 
#  print("Código correcto")
#    print("Segundo mensaje") # Modifica esta línea 

codigo = "1234"
if codigo == "1234":
    print("Codigo correcto")
    print("Segundo mensaje")