'''
Mostrar la palabra con la inicial indicada

Ideas clave**
*En Python, el ciclo for puede iterar directamente sobre los elementos de una lista.
*La sentencia if se utiliza para ejecutar código si se cumple una condición.
*Para hacer un corte, utilizamos la notación de corchetes y dos puntos. 
 Por ejemplo, texto[0:4] nos devolverá los caracteres desde el índice 0 hasta el 4, sin incluir el 4.
'''

#Ejercicio
'''
Crea una función llamada mostrarPalabrasQueEmpiecenCon que reciba un arreglo de palabras y una letra. El programa debe mostrar en consola las palabras que empiecen con la letra recibida.

Ejemplo
mostrarPalabrasQueEmpiecenCon(["lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit"], "a")

# amet
# adipiscing

mostrarPalabrasQueEmpiecenCon(["lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit"], "c")

# consectetur
'''

# Escribe tu código aquí
def mostrarPalabrasQueEmpiecenCon(palabras, letra):
    for palabra in palabras:
        #Si palabra comienza en indice 0, se baja a minuscula
        #y ese indice es igual a la letra:
        if palabra[0].lower() == letra.lower(): 
            print(palabra)


# Fin
mostrarPalabrasQueEmpiecenCon(["manzana", "maracuyá", "naranja", "pera", "uva"], "m")
print()
mostrarPalabrasQueEmpiecenCon(["gato", "perro", "ardilla", "pez", "conejo", "camello"], "c")
print()
mostrarPalabrasQueEmpiecenCon(["rojo", "azul", "verde", "amarillo"], "a")
