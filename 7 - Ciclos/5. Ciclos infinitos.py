'''
Ciclos infinitos

Ideas clave
*Con while podemos repetir un bloque de código mientras una condición sea verdadera.
*Es importante asegurarse de que la condición del while eventualmente se vuelva falsa para evitar bucles infinitos.

Un ciclo infinito

Supongamos que estamos resolviendo el ejercicio del contador y escribimos el siguiente código:

contador = 1
while contador <= 10:
    print(contador)
Como el contador nunca se incrementa, la condición contador <= 10 siempre será verdadera, 
por lo que el ciclo nunca terminará y se convertirá en un ciclo infinito.
'''

'''
Al intentar un ciclo infinito dentro del simulador obtendremos un mensaje de error. 
Si lo hacemos dentro de nuestro entorno de desarrollo, el programa se quedará ejecutando indefinidamente, 
donde podemos detenerlo manualmente utilizando Ctrl + C sobre la terminal que lo está ejecutando.
'''

#Ejercicio
'''
El siguiente código está incompleto y por lo mismo produce un ciclo infinito. Ejecútalo para que veas el error.

Luego, complétalo para que muestre en consola los números del 1 al 10.
'''

# Escribe tu código aquí 

contador = 1
while (contador <= 10):
  print(contador) 
  #Agregando un contador con autoincremento se evita el ciclo infinito.
  contador+=1

# Fin 

