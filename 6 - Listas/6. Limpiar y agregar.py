'''
Limpiar y agregar

Ideas clave
*Las listas permiten guardar múltiples valores.
*Podemos agregar un nuevo elemento a una lista utilizando el método append().
*El método strip() nos permite eliminar los espacios innecesarios al inicio y al final de una cadena de texto.

Apliquemos lo aprendido
'''

#Ejercicio
'''
Crea una función llamada limpiar_y_agregar que reciba una lista y un parámetro llamado nombre. 
La función debe remover los espacios vacíos al inicio y al final del nombre y luego agregar el nombre al final de la lista. 
Finalmente, la función debe retornar la lista.

Ejemplo:

limpiar_y_agregar(["Juan", "Pedro", "Ana", "Luis"], "  Maria  ")  # ["Juan", "Pedro", "Ana", "Luis", "Maria"]
'''

# Escribe tu código aquí
def limpiar_y_agregar(lista, nombre):
    nombre_limpio = nombre.strip() #variable nombre limpio con strip() le quita los espacios
    lista.append(nombre_limpio) #luego a la lista usando append() se agrega el ultimo parametro
    return lista

# Fin
print(limpiar_y_agregar(["uno", "dos", "tres", "cuatro"], "       cinco"))
print(limpiar_y_agregar(["Camilo", "Ignacio", "Constanza"], "      Juana     "))
print(limpiar_y_agregar(["perro", "gato", "pájaro", "pez"], "    cabra   "))
