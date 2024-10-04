'''
Cuadrado hueco

Ideas clave
*Los ciclos anidados son útiles para crear patrones bidimensionales complejos.
*El ciclo externo controla las filas, mientras que el ciclo interno controla las columnas.
*Para crear un cuadrado hueco, necesitamos diferenciar entre el borde y el interior del cuadrado.

Previamente creamos un cuadrado relleno con asteriscos. 
Ahora, vamos a modificar ese patrón para crear un cuadrado hueco. 
Un cuadrado hueco de lado 4 se vería así:

****
*   *
*   *
****
Para lograr esto, necesitamos modificar nuestro código anterior para distinguir entre las filas y columnas del borde y las del interior. 

Aquí tienes un ejemplo de cómo podría ser la estructura básica:

lado = 4
fila = 1
while fila <= lado:
    columna = 1
    while columna <= lado:
        if fila == 1 or fila == lado or columna == 1 or columna == lado:
            print("*", end="")
        else:
            print(" ", end="")
        columna += 1
    print()  # Nueva línea después de cada fila
    fila += 1

Este código verifica si estamos en el borde del cuadrado (primera o última fila, o primera o última columna) para decidir si imprimir un asterisco o un espacio.
'''

#Ejercicio
'''
Crea una función llamada cuadrado_hueco que reciba un número n como parámetro y muestre en la consola un cuadrado hueco de asteriscos de lado n.

Ejemplos:

cuadrado_hueco(3)
***
* *
***

cuadrado_hueco(5)
*****
*   *
*   *
*   *
*****
La función no debe retornar valor alguno, utiliza print() para mostrar el patrón. Asegúrate de que tu función funcione correctamente incluso para cuadrados de lado 1 o 2.
'''

# Escribe tu código aquí
def cuadrado_hueco(n):
    lado = n   #Lado sera igual al parametro n.                                                                     
    fila = 1   #Fila sera igual a 1.     
    #Mientras fila sea menor o igual a lado:                                                                
    while fila <= lado:                                                             
        columna = 1  #Columna sera igual a 1. 
        #Mientras columna sea menor o igual a lado:                                                    
        while columna <= lado:
            #Si fila es igual a 1, o fila es igual a lado, o columna es igual a 1, o columna es igual a lado:                                                      
            if fila == 1 or fila == lado or columna == 1 or columna == lado:
                #Imprime un asterisco
                print("*", end="")
            else:
                print(" ", end="")
            columna += 1 #Columna ira incrementando en 1.
        print()
        fila += 1 #Fila ira incrementando en 1.

# Fin
cuadrado_hueco(4)
cuadrado_hueco(2)
cuadrado_hueco(6)
cuadrado_hueco(1)
