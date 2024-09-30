'''
Contando de dos en dos

Ideas clave
*Con while podemos repetir un bloque de código mientras una condición sea verdadera.
*Es importante asegurarse de que la condición del while eventualmente se vuelva falsa para evitar bucles infinitos.
*Podemos modificar el incremento del contador para contar de dos en dos o en cualquier otro intervalo.

Recordemos el uso básico del ciclo while:

let contador = 1
while (contador <= 10) {
    print(contador)
    contador = contador + 1 # Incrementamos el contador en 1
}
print("Fin del ciclo")
'''

#Ejercicio
'''
Crea una función llamada contarDeDosEnDos que reciba un número como parámetro. 
La función debe mostrar todos los números pares entre 1 y el número dado.

Ejemplo:

contarDeDosEnDos(10) # Debería imprimir: 2, 4, 6, 8, 10
contarDeDosEnDos(20) # Debería imprimir: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20

Tip: Sabemos que podemos utilizar un if para evaluar si un número es par o no, pero ¿es necesario?
'''

# Escribe tu código aquí
def contarDeDosEnDos(numero):
    contador = 2
    while contador <= numero:
        print(contador, end=", " if contador < numero else "\n")
        contador += 2

# Fin 
contarDeDosEnDos(7)
contarDeDosEnDos(16)
contarDeDosEnDos(12)

