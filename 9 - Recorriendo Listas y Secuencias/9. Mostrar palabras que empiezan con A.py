'''
Mostrar palabras que empiezan con A

Ideas clave**
*En Python, el ciclo for puede iterar directamente sobre los elementos de una lista.
*La sentencia if se utiliza para ejecutar código si se cumple una condición.
*Para hacer un corte, utilizamos la notación de corchetes y dos puntos. 
 Por ejemplo, texto[0:4] nos devolverá los caracteres desde el índice 0 hasta el 4, sin incluir el 4.
'''

#Ejercicio
'''
Crea una función llamada mostrarLasPalabrasQueEmpiezanConA que reciba un arreglo de palabras y 
muestre las palabras que empiezan con la letra "a".

Ejemplo
MostrarLasPalabrasQueEmpiezanConA(["lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit"])
"""
amet
adipiscing
"""
'''

# Escribe tu código aquí 
def mostrarLasPalabrasQueEmpiezanConA(palabras):
    for palabra in palabras:
        if palabra[0].lower() == 'a': #Comprobar si la primera letra es 'a', ignorando a mayusculas.
            print(palabra)


# Fin
mostrarLasPalabrasQueEmpiezanConA(["manzana", "Arándanos", "naranja", "pera", "uva"])
mostrarLasPalabrasQueEmpiezanConA(["gato", "perro", "ardilla", "pez", "conejo", "alce"])
mostrarLasPalabrasQueEmpiezanConA(["rojo", "azul", "verde", "amarillo"])
