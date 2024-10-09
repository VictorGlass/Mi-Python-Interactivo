'''
Índice vs datos

Ideas clave
*En una lista, el índice es la posición del dato, mientras que el dato es el valor en esa posición.

Índice vs datos

Existe una diferencia importante entre el índice y el dato de una lista. 
El índice es la posición del dato en la lista, mientras que el dato es el valor que se encuentra en esa posición. 

Podemos usar un bucle while para recorrer la lista y acceder tanto al índice como al dato:

nombres = ["Juan", "Pedro", "María"]
# Mostrar el valor y el índice
i = 0
while i < len(nombres):
    print(f"{nombres[i]} en la posición {i}")
    i += 1

Por ejemplo, podríamos crear una función llamada mostrar_indice_y_dato que reciba una lista y muestre el índice y el dato de cada elemento de la lista:

def mostrar_indice_y_dato(datos):
    i = 0
    while i < len(datos):
        print(f"{datos[i]} en la posición {i}")
        i += 1

# Luego podemos llamar a la función
mostrar_indice_y_dato(["Juan", "Pedro", "María"])
"""
Juan en la posición 0
Pedro en la posición 1
María en la posición 2
"""
'''

#Ejercicio
'''
Modifica la siguiente función para que se muestren los datos de una lista en el siguiente formato: "El valor en la posición 0 es Galleta", utilizando un bucle while.
'''

# Escribe tu código aquí
def mostrar_dato_e_indice(datos):
    i = 0
    while i < len(datos):
        print(f"El valor en la posicion {i} es {datos[i]}")
        i += 1
# Fin
mostrar_dato_e_indice(["Galleta", "Chocolate", "Caramelo"])
