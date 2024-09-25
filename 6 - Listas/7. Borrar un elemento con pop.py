'''
Borrar un elemento con pop

Ideas clave
*Las listas en python permiten guardar múltiples valores.
*El método pop() se usa para eliminar y devolver un elemento de una lista.
*pop() sin argumentos elimina y devuelve el último elemento de la lista.
*pop(index) elimina y devuelve el elemento en la posición especificada por index.

Usando el método pop()

El método pop() es versátil y puede usarse de dos formas principales:

Sin argumentos: Elimina y devuelve el último elemento.
frutas = ["manzana", "pera", "uva"]
ultima_fruta = frutas.pop()
print(ultima_fruta)  # "uva"
print(frutas)  # ["manzana", "pera"]
Con un índice como argumento: Elimina y devuelve el elemento en esa posición.
numeros = [10, 20, 30, 40]
segundo_numero = numeros.pop(1)
print(segundo_numero)  # 20
print(numeros)  # [10, 30, 40]
'''

#Ejercicio
'''
Crea una función llamada eliminar_especial que reciba una lista de números. La función debe comportarse de la siguiente manera:

Si la lista tiene más de 5 elementos, debe eliminar el último elemento y devolver la lista modificada.
Si la lista tiene exactamente 5 elementos, debe eliminar el elemento en la posición 2 y devolver la lista modificado.
Si la lista tiene menos de 5 elementos debe devolver la lista sin modificar.

Ejemplos:

print(eliminar_elementos([1, 2, 3, 4]))  # Devuelve: (4, [1, 2, 3])
print(eliminar_elementos([1, 2, 3, 4], 1))  # Devuelve: (2, [1, 3, 4])
'''

# Escribe tu código aquí
def eliminar_especial(lista):
    if len(lista) > 5:         #Si la lista tiene mas de 5 elementos
        lista.pop()            #eliminamos el ultimo con .pop()
        return lista           #y devuelve la lista
    elif len(lista) == 5:      #Si la lista tiene 5 elementos
        lista.pop(2)           #elimina el elemento en la posicion dos usando .pop(2)
    return lista               #y devuelve la lista si hay menos de 5 elementos.

# Fin
print(eliminar_especial([10, 20, 30, 40, 50, 60]))
print(eliminar_especial(["manzana", "pera", "uva", "naranja", "kiwi"]))
print(eliminar_especial([1, "dos", 3.0, "cuatro"]))