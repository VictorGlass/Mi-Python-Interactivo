'''
Media pirámide

Ideas clave
*Los ciclos anidados son ciclos dentro de otros ciclos.
*Se utilizan para trabajar con estructuras de datos multidimensionales o para crear patrones complejos.

Dibujando patrones

En este ejercicio aprenderemos a dibujar un patrón de asteriscos en forma de media pirámide.

*
**
***
****
*****
Para esto utilizaremos dos ciclos while anidados. El ciclo externo controlará cuantas filas se mostrarán. 
Por ejemplo si la pirámide tiene 5 filas, el ciclo externo hará algo como esto:

filas = 5
fila_actual = 1
while fila_actual <= filas:
    print('*')
    fila_actual += 1
Y esto mostrará:

*
*
*
*
*
Ahora nos falta mostrar el número correcto de asteriscos en cada fila. En la primera fila se mostrará 1 asterisco, 
en la segunda 2, en la tercera 3 y así sucesivamente. En otras palabras, el número de asteriscos en cada fila es igual al número de la fila.

Para esto utilizaremos un ciclo interno que se encargará de mostrar el número correcto de asteriscos para cada fila.

filas = 5
fila_actual = 1
while fila_actual <= filas:
    columnas = 1
    string = ''
    while columnas <= fila_actual:
        string = string + '*'
        columnas += 1
    print(string) 
    fila_actual += 1
'''

#Ejercicio
'''
Crea una función llamada patron_piramide que reciba un número n como parámetro y muestre en la consola un patrón de estrellas creciente. 
El patrón debe tener n filas, y cada fila debe tener tantas estrellas como su número de fila.

Ejemplos:

patron_piramide(3)
*
**
***

patron_piramide(5)
*
**
***
****
*****
La función no debe retornar valor alguno, utiliza print() para mostrar el patrón.
'''

# Escribe tu código aquí
def patron_estrellas(n):
    #Variable para el parametro de la funcion:
    filas = n
    #variable iniciada en 1:
    fila_actual = 1
    #Mientras fila actual sea menos a filas...
    while fila_actual <= filas:
        #Variable = 1:
        columnas = 1
        #Variable string:
        string = ''
        
        while columnas <= fila_actual:
            string = string + '*'
            columnas += 1
        print(string)
        fila_actual += 1


# Fin
patron_estrellas(4)
patron_estrellas(7)
patron_estrellas(2)
