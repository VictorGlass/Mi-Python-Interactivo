'''
Agregando un elemento al final de un arreglo

Ideas clave
*Las listas permiten guardar múltiples valores.
*Podemos agregar un nuevo elemento a una lista utilizando el método append().

Agregando un elemento a una lista

Para añadir un nuevo elemento a una lista, utilizamos el método append(). 
Este método recibe un parámetro y lo agrega al final de la lista.

nombres = ["Juan", "Pedro", "Ana", "Luis"]
nombres.append("Maria")
print(nombres)  # ["Juan", "Pedro", "Ana", "Luis", "Maria"]
También podemos agregar un elemento a una lista vacía.

nombres = []
nombres.append("Maria")
print(nombres)  # ["Maria"]

En estos ejemplos, después de llamar al método append() con el argumento "Maria", 
la lista se modifica y se agrega el nuevo elemento al final de la lista.
'''

#Ejercicio
'''
Crea una función llamada agregar_si que reciba una lista y un parámetro llamado nombre. 
La función debe agregar el nombre a la lista si el largo de la lista es menor a 5. La función debe retornar la lista.

Ejemplo:

agregar_si(["Juan", "Pedro", "Ana", "Luis"], "Maria")  # ["Juan", "Pedro", "Ana", "Luis", "Maria"]
agregar_si(["Juan", "Pedro", "Ana", "Luis", "Carlos", "Maria"], "Jose")  # ["Juan", "Pedro", "Ana", "Luis", "Carlos", "Maria"]
'''

# Escribe tu código aquí
def agregar_si(lista, nombre):
    if len(lista) < 5:
        lista.append(nombre)
    return lista


# Fin
print(agregar_si(["perro", "gato", "delfin", "tortuga"], "caballo"))
print(agregar_si(["Francisco", "Rene", "Gonzalo", "Consuelo"], "Javier"))
print(agregar_si(["ruby", "javascript", "python", "c", "c#", "java"], "php"))
