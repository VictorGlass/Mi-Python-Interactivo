'''
Diagonal

Previamente creamos patrones de cuadrados rellenos y huecos. 
Ahora, vamos a crear un patrón que muestre solo la diagonal de un cuadrado. 
Un patrón de diagonal de un cuadrado de 5x5 se vería así:

*    
 *   
  *  
   * 
    *
'''

#Ejercicio
'''
Crea una función llamada diagonal_cuadrado que reciba un número n como parámetro y muestre en la consola la diagonal de un cuadrado de lado n.

Ejemplos:

diagonal_cuadrado(3)
*  
 * 
  *

diagonal_cuadrado(5)
*    
 *   
  *  
   * 
    *
La función no debe retornar valor alguno, utiliza print() para mostrar el patrón. 
Asegúrate de que tu función funcione correctamente incluso para casos donde el lado del cuadrado sea 1 o 2.
'''

# Escribe tu código aquí
def diagonal_cuadrado(n):
    #Para cada fila en el rango de (n)
    #imprime espacios en blancos antes del asterisco.
    for fila in range(n):
        print(' ' * fila + '*')
        


# Fin
diagonal_cuadrado(4)
diagonal_cuadrado(2)
diagonal_cuadrado(1)
diagonal_cuadrado(6)
