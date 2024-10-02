'''
Línea por medio

Previamente creamos un cuadrado relleno con asteriscos. 
Ahora, vamos a modificar ese patrón para crear un rectángulo con líneas alternadas. 
Un patrón de líneas alternadas de 5x8 se vería así:

********
        
********
        
********     

Este patrón muestra claramente cómo se alternan las líneas de asteriscos con las líneas en blanco. 
En las líneas impares, se imprimen asteriscos, mientras que en las líneas pares se imprimen espacios en blanco.

Para lograr esto, necesitamos modificar nuestro código anterior para imprimir asteriscos solo en las filas pares 
(o impares, dependiendo de cómo lo contemos). Para determinar si una fila es par o impar, podemos utilizar el operador módulo (%).

if fila % 2 == 0:
    # Fila par
else:
    # Fila impar
'''

#Ejercicio
'''
Crea una función llamada lineas_alternadas que reciba dos números filas y columnas como parámetros y 
muestre en la consola un patrón de líneas alternadas de asteriscos.

Ejemplos:

lineas_alternadas(4, 5)
*****
     
*****
     

lineas_alternadas(3, 3)
***
   
***
La función no debe retornar valor alguno, utiliza print() para mostrar el patrón. 
Asegúrate de que tu función funcione correctamente incluso para casos donde el número de filas o columnas sea 1.
'''

# Escribe tu código aquí
def lineas_alternadas(filas, columnas):
    for i in range(filas):#Ciclo para las filas
        if i % 2 == 0: #Si la fila es par, imprime asteriscos.
            print('*' * columnas)
        else: #Si la fila es impar, imprime una linea en blanco.
            print(' ' * columnas)


# Fin
lineas_alternadas(4,6)
lineas_alternadas(5,2)
lineas_alternadas(1,3)
lineas_alternadas(2,1)
