'''
Introducción a diagramas de flujo

Ideas clave:
*Los programas por defecto se ejecutan de manera lineal, de arriba a abajo.
*Podemos cambiar el flujo de un programa utilizando sentencias de control de flujo.
*Los diagramas de flujo son una herramienta visual que nos permite representar el flujo de un programa.

Diagramas de flujo
El flujo de un programa es el orden en el que se ejecutan las instrucciones y, 
si bien podemos seguir el flujo de un programa leyendo el código, a veces es más fácil visualizarlo. 
Para esto se utilizan los diagramas de flujo, que son una herramienta visual que nos permite representar 
el flujo de un programa.

Los diagramas de flujo se componen de bloques que representan instrucciones y flechas que indican 
el flujo de ejecución. Cada bloque tiene una forma específica que indica el tipo de instrucción que representa. 
Por ejemplo, un bloque rectangular representa una instrucción, un rombo representa una condición y un óvalo representa el inicio o fin del programa.
'''

#Ejercicio
'''
*Inicio
*Asignar el texto 'hola' a variable 'saludo'
*¿El saludo es igual a 'hola'?
*Si > Mostrar 'Es el saludo correcto'
*No > Fin
'''
# Escribe tu código aquí
#saludo = 'hola'
#if saludo == 'hola':
#    print('Es el saludo correcto')
# Fin

saludo = 'hola'
if saludo == 'hola':
    print("Es el saludo correcto!")
else:
    print("No es el saludo correcto")



