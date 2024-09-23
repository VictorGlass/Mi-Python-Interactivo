'''
Parámetros y argumentos

Ideas clave
*Una función puede depender de múltiples parámetros para llevar a cabo su tarea.
*Los valores que uno pasa cuando llama a una función formalmente reciben el nombre de argumentos.
*Agregar más parámetros a una función es tan sencillo como separarlos por comas.
*Los argumentos se pasan en el mismo orden que los parámetros de la función.

¿Cómo trabajar con múltiples parámetros?

Así como una función puede depender de uno o dos parámetros, también puede depender de tres o más parámetros.

Por ejemplo, considera la función sumar(a, b, c) que suma tres números y los muestra en la consola:

def sumar(a, b, c):
  print(a + b + c)

sumar(5, 3, 2) # 10 

Los argumentos se pasan en el mismo orden que los parámetros de la función.

Parámetros vs. Argumentos
Existen dos conceptos parecidos pero distintos que es importante tener en cuenta al trabajar con funciones:

Parámetros: Son los nombres que usas en una función para recibir datos. Por ejemplo, en sumar(a, b, c), a, b y c son parámetros.

Argumentos: Son los valores que le das a la función cuando la llamas. Por ejemplo, en sumar(5, 3, 2), 5, 3 y 2 son argumentos.

Ocasionalmente, se usa el término argumento para referirse a ambos conceptos, 
pero es importante tener en cuenta la diferencia al leer mensajes de error o documentación.
'''

#Ejercicio
'''
Crea la función restar que dependa de tres parámetros a, b y c. 
Esta función al ser llamada debe mostrar el resultado de la resta de los tres valores ingresados.
'''

#restar(10, 5, 3)
#restar(3, 5, 2)
#restar(9, 4, 1)

# Escribe tu código aquí 

def restar(a, b, c): #parametros 
    resta = a - b - c
    print(f"Al restar los valores -> {a}, {b} y {c}, el resultado es: {resta}")

restar(10, 5, 3) #argumentos
restar(3, 5, 2)
restar(9, 4, 1)