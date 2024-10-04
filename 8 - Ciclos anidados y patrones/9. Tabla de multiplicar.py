'''
Tabla de multiplicar

Ideas clave
*Los ciclos anidados son útiles para crear tablas como una tabla de multiplicar.

En este ejercicio, crearemos una representación visual de la tabla de multiplicar del 1 al 10. El resultado se verá así:

  1   2   3   4   5   6   7   8   9  10
  2   4   6   8  10  12  14  16  18  20
  3   6   9  12  15  18  21  24  27  30
  4   8  12  16  20  24  28  32  36  40
  5  10  15  20  25  30  35  40  45  50
  6  12  18  24  30  36  42  48  54  60
  7  14  21  28  35  42  49  56  63  70
  8  16  24  32  40  48  56  64  72  80
  9  18  27  36  45  54  63  72  81  90
 10  20  30  40  50  60  70  80  90 100

Para lograr esto, usaremos ciclos anidados y formateo de cadenas. Aquí tienes un ejemplo de cómo podría ser la estructura básica:

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:3d}", end=" ")
    print()  # Nueva línea después de cada fila

Este código utiliza dos ciclos for anidados para generar todas las multiplicaciones del 1 al 10. 
El formateo {i*j:3d} asegura que cada número ocupe 3 espacios, alineando las columnas.
'''

#Ejercicio
'''
Crea una función llamada tabla_multiplicar que no reciba parámetros y muestre en la consola la tabla de multiplicar del 1 al 10 en formato de matriz.

Ejemplo de uso:

tabla_multiplicar()
# Debe mostrar la tabla como se ve en el ejemplo anterior
La función no debe retornar valor alguno, utiliza print() para mostrar la tabla. Asegúrate de que los números estén correctamente alineados en columnas.
'''

# Escribe tu código aquí
def tabla_multiplicar():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i*j:3d}", end=" ")
        print()

# Fin
tabla_multiplicar()
