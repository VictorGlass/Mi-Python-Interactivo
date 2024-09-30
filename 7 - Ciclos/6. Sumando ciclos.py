'''
Sumando con ciclos

Ideas clave
*Con while podemos repetir un bloque de código mientras una condición sea verdadera.
*Es importante asegurarse de que la condición del while eventualmente se vuelva falsa para evitar bucles infinitos.

Sumando con ciclos

Otro uso frecuente de ciclos es para llevar a cabo operaciones de suma. 
Por ejemplo, si queremos sumar los números del 1 al 10, podemos utilizar while para contar de uno en uno y en una variable acumular la suma.

contador = 1
suma = 0
while (contador <= 10):
    suma = suma + contador
    contador = contador + 1
print(suma)

En este ejemplo, contador se inicializa en 1, mientras que suma se inicializa en 0. 
Dentro del ciclo, en cada iteración, se suma el valor de contador a suma, y luego se incrementa contador en 1. 
Esto se repite hasta que contador alcanza o supera el valor de 10, momento en el cual el ciclo se detiene. 
Al finalizar, suma contendrá la suma total de los números del 1 al 10.
'''

#Ejercicio
'''
Crea una función llamada sumarHasta que reciba un número como parámetro.

La función debe retornar la suma de los números del 1 al número ingresado.

Por ejemplo, si el número ingresado es 5, la función debe retornar 15. Si el número ingresado es 10, la función debe retornar 55.
'''

# Escribe tu código aquí
def sumarHasta(numero):
    contador = 1
    suma = 0
    while (contador <= numero):
        suma = suma  + contador
        contador += 1
    return suma

# Fin
print(sumarHasta(4))
print(sumarHasta(11))
print(sumarHasta(2))
