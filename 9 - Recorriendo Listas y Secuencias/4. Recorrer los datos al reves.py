'''
Recorrer los datos al revés

Ideas clave
*Los ciclos while pueden usarse para recorrer listas, al igual que los ciclos for.
*Al usar while con listas, generalmente necesitamos un contador o índice que incrementamos manualmente.
*Los ciclos while nos permiten controlar con precisión cuántos elementos de una lista procesamos y en qué orden.

datos = ["hola", "mundo", "desde", "python"]
i = len(datos) - 1 
while i >= 0:
  print(datos[i])
  i = i - 1
'''

#Ejercicio
'''
Crea una función llamada mostrarDatosAlReves que reciba un arreglo y que muestre los datos del arreglo en orden inverso.

Ejemplo:

mostrarDatosAlReves([1, 2, 3, 4, 5]) 
/* 
5
4
3
2
1
*/
'''

# Escribe tu código aquí 
def mostrarDatosAlReves(lista):
    #Indice sera igual al largo de la lista -1:
    indice = len(lista) -1
    #Mientras el indice sea mayor o igual a 0:
    while indice >= 0:
        #Imprimimos la lista con el la variable de indice:
        print(lista[indice])
        #Autodecremento:
        indice -= 1

# Fin
mostrarDatosAlReves([4,6,8,2,3])
print()
mostrarDatosAlReves([1,2,3,4,5,6,7,8])
print()
mostrarDatosAlReves([10,11,12,13])
