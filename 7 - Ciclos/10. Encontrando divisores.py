'''
Encontrando divisores

Ideas clave**
*Con while podemos repetir un bloque de código mientras una condición sea verdadera.
*Es importante asegurarse de que la condición del while eventualmente se vuelva falsa para evitar bucles infinitos.

Calculando divisores

El uso de ciclos while se extiende a muchas aplicaciones matemáticas, como calcular sumas, productos y encontrar divisores, entre otras funciones.

Un ejercicio recurrente en entrevistas de trabajo es el de encontrar los divisores de un número específico.

Por ejemplo, podríamos crear una función que tome un número y muestre todos sus divisores.

Para resolver este ejercicio necesitamos un ciclo que recorra todos los números desde 1 hasta el número dado. 
Si el número dado es 10, necesitamos recorrer los números 1, 2, 3, 4, 5, 6, 7, 8, 9 y 10.

Dentro del ciclo necesitamos evaluar si el número actual es un divisor del número dado. 
En el caso del número 10, necesitamos evaluar si 1, 2, 3, 4, 5, 6, 7, 8, 9 y 10 son divisores de 10.

Aunque esta tarea implica un proceso similar al de contar o sumar, aquí la diferencia radica en la necesidad de verificar 
si el número actual es un divisor del número dado. Si lo es, entonces lo mostramos.

Para determinar si un número es un divisor del número dado, usamos el operador módulo %. 
Si el resultado de la operación numero % divisor es 0, significa que el número es divisor del número dado.

La función para obtener este resultado sería la siguiente:

def mostrar_divisores(numero):
    contador = 1
    while contador <= numero:
        if numero % contador == 0:
            print(contador)
        contador = contador + 1

mostrar_divisores(10)  # 1, 2, 5, 10
mostrar_divisores(20)  # 1, 2, 4, 5, 10, 20
'''

#Ejercicio

'''
Crea una función llamada divisores_comunes que reciba dos números y que muestre los divisores comunes de ambos números. Ejemplo:

divisores_comunes(10, 20)  # 1, 2, 5, 10
divisores_comunes(15, 30)  # 1, 3, 5, 15
> Tip: el operador y se escribe and en Python.
'''

# Escribe tu código aquí
def divisores_comunes(num1, num2):
    contador = 1
    divisores = []

    while contador <= min(num1, num2):
        if num1 % contador == 0 and num2 % contador == 0:
            divisores.append(contador)
            print(contador)
        contador += 1
    return divisores

# Fin
divisores_comunes(18, 24)
divisores_comunes(7, 14)
divisores_comunes(25, 35)
