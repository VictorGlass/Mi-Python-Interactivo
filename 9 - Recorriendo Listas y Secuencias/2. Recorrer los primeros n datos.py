'''
Recorrer los primeros n datos

Ideas clave
*Los ciclos while pueden usarse para recorrer listas, al igual que los ciclos for.
*Al usar while con listas, generalmente necesitamos un contador o índice que incrementamos manualmente.
*Los ciclos while nos permiten controlar con precisión cuántos elementos de una lista procesamos y en qué orden.

Recorriendo listas con un índice

Si queremos limitar la cantidad de elementos que procesamos de una lista podemos 
utilizar la condición del while para controlar cuántos elementos procesamos.

datos = [1, 2, 3, 4, 5]
i = 0
while i < 2: # Cambiar el 2 por el número de elementos que deseas mostrar
    print(datos[i])
    i += 1
'''

#Ejercicio
'''
Utilizando while, crea una función llamada mostrar_datos que reciba una lista y un número n como parámetros y 
muestre en consola los primeros n elementos de la lista donde n es el parámetro. Ejemplo:

mostrar_datos([1, 2, 3, 4, 5], 3)
"""
1
2
3
"""
mostrar_datos([10, 20, 30, 40, 50, 60, 70], 4)
"""
10
20
30
40
"""
La lista siempre tendrá al menos n elementos. > Tip: Recuerda que cuando se pide mostrar, 
no debes retornar nada, solo mostrar los datos utilizando print.
'''

# Escribe tu código aquí
def mostrar_datos(lista, n):
    #El comienzo sera en 0:
    indice = 0
    #Mientras el indice sea menor a n:
    while indice < n:
        #Se imprimira la lista desde el primer numero:
        print(lista[indice])
        #Autoincrementador:
        indice +=1


# Fin
mostrar_datos([4,6,8,2,3],2)
print()
mostrar_datos([1,2,3,4,5,6],4)
