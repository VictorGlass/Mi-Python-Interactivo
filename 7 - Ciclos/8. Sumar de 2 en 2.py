'''
Sumar de 2 en 2

Ideas clave
*Con while podemos repetir un bloque de código mientras una condición sea verdadera.
*Es importante asegurarse de que la condición del while eventualmente se vuelva falsa para evitar bucles infinitos.

Apliquemos lo aprendido.
'''

#Ejercicio
'''
Crea una función llamada sumarDeDosEnDos que reciba dos parámetros, desde y hasta. La función debe retornar la suma de los números.

Ejemplo
sumarDeDosEnDos(5, 10) # 5 + 7 + 9 = 21
sumarDeDosEnDos(10, 20) # 10 + 12 + 14 + 16 + 18 + 20 = 90
sumarDeDosEnDos(3, 7) # 3 + 5 + 7 = 15
'''

# Escribe tu código aquí 

def sumarDeDosEnDos(num1, num2):
    contador = num1
    suma = 0

    while contador <= num2:
        suma = suma  + contador
        contador += 2
    return suma
     
# Fin
print(sumarDeDosEnDos(4,9))
print(sumarDeDosEnDos(2,5))
print(sumarDeDosEnDos(25,67))
