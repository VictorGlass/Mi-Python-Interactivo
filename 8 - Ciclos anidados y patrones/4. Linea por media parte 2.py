'''
Línea por medio parte 2

Previamente creamos patrones como la media pirámide, el cuadrado relleno y las líneas horizontales alternadas. 
Ahora, vamos a crear un nuevo patrón: líneas verticales alternadas. El patrón se verá así:

* * *
* * *
* * *
* * *
En este patrón, imprimimos asteriscos en las columnas impares y espacios vacíos en las columnas pares.
'''

#Ejercicio
'''
Crea una función llamada lineas_verticales_alternadas que reciba dos números filas y columnas como parámetros 
y muestre en la consola un patrón de líneas verticales alternadas con asteriscos y espacios en blanco.

Ejemplos:

lineas_verticales_alternadas(3, 5)
* * *
* * *
* * *

lineas_verticales_alternadas(4, 4)
* * 
* * 
* * 
* * 
La función no debe retornar valor alguno, utiliza print() para mostrar el patrón. 
Asegúrate de que tu función funcione correctamente incluso para casos donde el número de filas o columnas sea 1.
'''


# Escribe tu código aquí
def lineas_verticales_alternadas(filas, columnas):

    #Para i en el rango de filas:
    for i in range(filas):
        linea = ""
        #Para j en el rango de columnas:
        for j in range(columnas):
            if j % 2 == 0:        #Si en columnas hay numeros impares/ con asterisco.
                linea += "*"
            else:                 #Y en columnas pares con un espacio.
                linea += " "
        
        print(linea)

# Fin
lineas_verticales_alternadas(4,5)
lineas_verticales_alternadas(2,3)
lineas_verticales_alternadas(1,6)
lineas_verticales_alternadas(5,1)