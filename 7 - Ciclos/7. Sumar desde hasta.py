'''
Sumar desde hasta

Ideas clave
*Con while podemos repetir un bloque de código mientras una condición sea verdadera.
*Es importante asegurarse de que la condición del while eventualmente se vuelva falsa para evitar bucles infinitos.
Apliquemos lo aprendido
'''

#Ejercicio
'''
Crea una función llamada sumarDesdeHasta que reciba dos números como parámetros y retorne la suma de los números desde el primer número hasta el segundo número.

Ejemplo
sumarDesdeHasta(1, 5) # 15
sumarDesdeHasta(10, 20) # 165
sumarDesdeHasta(100, 200) # 15150
'''

# Escribe tu código aquí
def sumarDesdeHasta(num1, num2):
    contador = num1
    suma = 0

    while contador <= num2:
        suma = suma  + contador
        contador += 1
    return suma

# Fin
print(sumarDesdeHasta(4,9))
print(sumarDesdeHasta(2,5))
print(sumarDesdeHasta(50,136))

