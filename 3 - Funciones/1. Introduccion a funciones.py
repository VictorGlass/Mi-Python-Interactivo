'''
Introducción a funciones

Idea clave
*Las funciones nos permiten reutilizar código.
*Las funciones deben ser definidas una vez y luego pueden ser llamadas a lo largo del programa.
*Palabras clave: definir, llamar.

¿Qué son las funciones?

Las funciones son bloques de código que nos permiten reutilizar y estructurar nuestro código 
de una manera más organizada. 
Al definir una función, estamos creando un conjunto de instrucciones que realizan una tarea específica. 
Luego, podemos llamar a esa función en cualquier parte de nuestro programa cada vez que necesitemos ejecutar esa tarea. 
Esto nos ayuda a evitar la repetición de código en nuestras aplicaciones.

Veamos un ejemplo:

# Definimos la función 

def saludar():
  print("Hola Mundo")

saludar() # Llamamos a la función
saludar() # Llamamos a la función una segunda vez
saludar() # Llamamos a la función una tercera vez

En el código mostrado, primero se define la función saludar que muestra el mensaje "Hola Mundo". 
Luego, llamamos a la función tres veces. Cada vez que llamamos a la función, se ejecuta el código 
dentro de la función saludar, mostrando el mensaje "Hola Mundo".
'''

#Ejercicio
'''
Se tiene definida la función despedir, pero no se está llamando. 
Llama a la función despedir para que imprima "Adiós Mundo" en la consola.
'''

#def despedir():
#  print("Adiós Mundo")

# Escribe tu código aquí

def despedir():
    print("Adios Mundo")

despedir()


# Fin