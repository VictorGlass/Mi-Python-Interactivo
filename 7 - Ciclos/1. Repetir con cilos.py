'''
Repetir con ciclos

Ideas clave
*Con while podemos repetir un bloque de código mientras una condición sea verdadera.
*Es importante asegurarse de que la condición del while eventualmente se vuelva falsa para evitar bucles infinitos.

Usando while
While (o 'mientras' en español) es una estructura de control que se utiliza para repetir un bloque de código mientras una 
condición sea verdadera. Por ejemplo, podemos contar del 1 al 10 con un ciclo while:

contador = 1
while contador <= 10:
    print(contador)
    contador += 1  # Incrementamos el contador en 1
print("Fin del ciclo")
'''

'''
Inicio
contador = 1
contador <= 10
print(contador)
incrementar el contador en1
print('Fin del ciclo')
Fin



Partiendo de un contador en 1, el ciclo while se ejecutará mientras el contador sea menor o igual a 10. 
En cada iteración, se muestra el valor del contador y se incrementa en 1. 
Cuando el contador llega a 11, la condición del while se vuelve falsa y el ciclo termina.
'''

#Ejercicio
'''
Crea una función llamada contar_hasta que reciba un número como parámetro y 
muestre en la consola los números del 1 al número ingresado.

Ejemplos:

contar_hasta(5)
1
2
3
4
5

contar_hasta(10)
1
2
3
4
5
6
7
8
9
10
La función no debe retornar valor alguno, utiliza print() para mostrar los números.
'''

# Escribe tu código aquí

def contar_hasta(numero):
    #Declarando la variable contador que inicia en 1
    contador = 1
    #Mientras el contador sea menor o igual al numero por parametro...
    while contador <= numero:
        print(contador)
        #Creando un incrementador y se ira sumando en 1
        contador +=1


# Fin
print("Imprimiendo hasta el numero 4")
contar_hasta(4)
print()
print("Imprimiendo hasta el numero 12")
contar_hasta(12)
print()
print("Imprimiendo hasta el numero 7")
contar_hasta(7)

