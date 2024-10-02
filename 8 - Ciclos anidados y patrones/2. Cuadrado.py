'''
Cuadrado

Ideas clave
*Los ciclos anidados son útiles para crear patrones bidimensionales.
*El ciclo externo controla las filas, mientras que el ciclo interno controla las columnas.

Previamente creamos un patrón para dibujar media pirámide. 
Ahora, vamos a utilizar ciclos anidados para crear un cuadrado relleno con asteriscos como el siguiente:

****
****
****
En este ejemplo el cuadrado tendría 3 filas y 4 columnas. 
Utiliza como base el código que desarrollamos para la media pirámide y modifícalo para que el patrón sea un cuadrado.

filas = 5
for fila_actual in range(1, filas + 1):
    string = ''
    for columnas in range(1, fila_actual + 1):
        string = string + '*'
    print(string)
'''

#Ejercicio
'''
Crea una función llamada cuadrado_relleno que reciba un número n como parámetro y muestre en la consola un cuadrado relleno de asteriscos de lado n.

Ejemplos:

cuadrado_relleno(3)
***
***
***

cuadrado_relleno(5)
*****
*****
*****
*****
*****
La función no debe retornar valor alguno, utiliza print() para mostrar el patrón.
'''

# Escribe tu código aquí
def cuadrado_relleno(n):
    
    for i in range(n):
        print("*" * n)

# Fin
cuadrado_relleno(4)
cuadrado_relleno(2)
cuadrado_relleno(6)
