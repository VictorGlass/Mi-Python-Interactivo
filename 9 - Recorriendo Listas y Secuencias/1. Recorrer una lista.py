'''
Recorrer una lista

Ideas clave
*Los ciclos while pueden usarse para recorrer listas, al igual que los ciclos for.
*Al usar while con listas, generalmente necesitamos un contador o índice que incrementamos manualmente.
*Es importante asegurarse de que la condición del while eventualmente se vuelva falsa para evitar bucles infinitos.

Recordando listas

Previamente estudiamos las listas y cómo acceder a elementos específicos dentro de ellas. 
Al combinar listas y ciclos, podemos recorrer todos los elementos de una lista y realizar operaciones con cada uno de ellos.

El siguiente código muestra cómo recorrer una lista de nombres y mostrar cada uno de ellos utilizando un ciclo while:

nombres = ["Juan", "Pedro", "Ana", "Luis"]
indice = 0
while indice < len(nombres):
    print(nombres[indice])
    indice += 1
"""
Juan
Pedro
Ana
Luis
"""
Cada print agrega automáticamente un salto de línea al final de la cadena que muestra. 
Por lo tanto, cada nombre se mostrará en una línea diferente.

Usualmente, al recorrer ciclos while, se utiliza una variable llamada i de indice. 
Es importante tener en cuenta que esto es simplemente una convención y el nombre de la variable puede ser cualquier otro.
'''

#Ejercicio
'''
Crea una función llamada mostrar que reciba una lista de números y que muestre los primeros 3 números de la lista utilizando un ciclo while. 
Considera que todos los casos de prueba tienen al menos 3 elementos. Ejemplo:

mostrar([1, 2, 3, 4, 5, 6])
"""
1
2
3
"""
mostrar([10, 20, 30, 40, 50, 60, 70])
"""
10
20
30
"""
Tip: Recuerda que cuando se pide mostrar, no debes retornar nada, solo mostrar los datos utilizando print. 
Asegúrate de usar un ciclo while para esta tarea.
'''

# Escribe tu código aquí
def mostrar(lista):
    #El comienzo sera en 0:
    indice = 0
    #Mientras el indice sea menor que 3:
    while indice < 3:
        #Se imprimira la lista desde el primer numero:
        print(lista[indice])
        #Autoincrementador:
        indice +=1

# Fin
mostrar([4,6,8,2,3])
print()
mostrar([1,2,3,4,5,6])
print()
mostrar([10,11,12])
