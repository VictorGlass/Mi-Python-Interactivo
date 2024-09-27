'''
De variable a lista

Ideas clave
*En Python, podemos crear una lista con un solo elemento usando corchetes: [elemento].
*Podemos combinar listas usando el operador +.
*Para agregar un elemento a una lista, podemos usar el método append() o simplemente concatenar una lista con un solo elemento.

Creando y combinando listas en Python

Para crear una lista a partir de una variable y combinarla con otras listas:

variable = 123
lista = [variable]
print(lista)  # [123]

En este código se crea una variable llamada variable que contiene el número 123. Luego, se crea una lista llamada 
lista que contiene un solo elemento, que es el valor de la variable "variable". Esto se logra utilizando corchetes [] alrededor de variable.

lista.append(456)
print(lista)  # [123, 456]
En este segundo ejemplo, se utiliza el método append() para agregar el número 456 al final de la lista lista.

otra_lista = [789]
lista_combinada = lista + otra_lista
print(lista_combinada)  # [123, 456, 789]

Finalmente, tenemos la tercera opción de definir otra lista, en este caso llamada otra_lista, que 
contiene el número 789. Luego, se combina la lista "lista" (que ahora es [123, 456]) con otra_lista usando el operador +. 

La operación lista + otra_lista crea una nueva lista llamada lista_combinada que contiene todos los elementos de lista seguidos por todos los elementos de otra_lista.
'''

#Ejercicio
'''
Crea una función llamada juntar_elementos que reciba 3 parámetros: arr1, valor, y arr2, donde arr1 y arr2 serán listas y valor un número. 
La función debe retornar una nueva lista juntando los elementos de arr1, el valor, y los elementos de arr2.

Ejemplo:

print(juntar_elementos([1, 2, 3], 4, [5, 6, 7]))  # [1, 2, 3, 4, 5, 6, 7]
Tip: Puedes utilizar el operador + para combinar las listas y agregar el valor como una lista de un solo elemento.
'''

# Escribe tu código aquí
#def juntar_elementos(arr1, valor, arr2):
#    nueva_lista = [arr1, valor ,arr2]
#    return nueva_lista

def juntar_elementos(arr1, valor, arr2):
    nueva_lista = arr1 + [valor] + arr2
    return nueva_lista

# Fin
print(juntar_elementos([1,2,3], 4, [5,6,7]))
print(juntar_elementos(['a','b'], 'c', ['d','e']))
print(juntar_elementos(['uno','dos'], 'tres', ['cuatro','cinco']))
