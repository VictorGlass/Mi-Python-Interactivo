'''
Dibujando tablas

Ideas clave
*El uso correcto de print() es fundamental para crear estructuras visuales en la consola.
*Los ciclos anidados pueden usarse para crear filas y columnas.
*El parámetro end en print() nos permite controlar el final de cada impresión.
*El formateo de cadenas nos ayuda a alinear el contenido de la tabla.

En este ejercicio, crearemos una tabla simple con números. El resultado se verá así para una tabla de 5x5:

  1  2  3  4  5
  6  7  8  9 10
 11 12 13 14 15
 16 17 18 19 20
 21 22 23 24 25

Para lograr esto, usaremos ciclos anidados y formateo de cadenas. Aquí tienes un ejemplo de cómo podría ser la estructura básica:

n = 5
numero = 1
for i in range(n):
    for j in range(n):
        print(f"{numero:3d}", end="")
        numero += 1
    print()  # Nueva línea después de cada fila

Este código utiliza dos ciclos for anidados para generar la tabla. El formateo {numero:3d} asegura que cada número ocupe 3 espacios, alineando las columnas.
'''

#Ejercicio
'''
Crea una función llamada dibujar_tabla que reciba un parámetro n y muestre en la consola una tabla de n x n con números consecutivos.

Ejemplo de uso:

dibujar_tabla(3)
# Debe mostrar:
#  1  2  3
#  4  5  6
#  7  8  9

dibujar_tabla(4)
# Debe mostrar:
#  1  2  3  4
#  5  6  7  8
#  9 10 11 12
# 13 14 15 16

La función no debe retornar valor alguno, utiliza print() para mostrar la tabla. 
Asegúrate de que los números estén correctamente alineados en columnas. 
Tu función debe funcionar para cualquier valor de n mayor que 0.
'''

# Escribe tu código aquí
def dibujar_tabla(n):
    #Empezar el conteo de numeros en 1:
    numeros = 1
    #Este ciclo recorrera las filas de la tabla:
    for i in range(n):
        #Este ciclo imprimira los numeros de cada fila:
        for j in range(n):
            #El formateo {numero:3d} asegura que cada numero ocupe 3 espacios:
            print(f"{numeros:3d}", end=" ")
            numeros += 1
        print()
# Fin
dibujar_tabla(5)
dibujar_tabla(2)
dibujar_tabla(1)
dibujar_tabla(7)
