'''
Desde hasta

Ideas clave
*Los ciclos while pueden usarse para recorrer listas, al igual que los ciclos for.
*Al usar while con listas, generalmente necesitamos un contador o índice que incrementamos manualmente.
*Los ciclos while nos permiten controlar con precisión cuántos elementos de una lista procesamos y en qué orden.

Combinemos lo aprendido en los ejercicios anteriores para resolver un problema más complejo.
'''

#Ejercicio
'''
Crea una función llamada desde_hasta que reciba tres parámetros:

Una lista de números
Un índice de inicio desde
Un índice de fin hasta
La función debe mostrar los elementos de la lista desde el índice de inicio desde hasta el índice hasta (sin incluir el elemento en el índice hasta).

Ejemplo:

desde_hasta([1, 2, 3, 4, 5, 6], 2, 4)
"""
3
4
"""
'''

# Escribe tu código aquí
def desde_hasta(lista, desde, hasta):
    #Iniciar el indice usando el parametro desde:
    indice = desde
    #Mientras el indice sea menor a hasta:
    while indice < hasta:
        #Imprimimos la lista partiendo de el primer parametro(desde):
        print(lista[indice])
        #Autoincrementador:
        indice += 1

# Fin
desde_hasta([4,6,8,2,3],2,3)
print()
desde_hasta([1,2,3,4,5,6,7,8,9],4,6)
