'''
Introducción a flujo

Ideas clave:
*Los programas se ejecutan de manera lineal, de arriba a abajo.
*Podemos cambiar el flujo de un programa utilizando condiciones.

¿Qué es el flujo?

El flujo de un programa es el orden en el que se ejecutan las instrucciones. 
Hasta el momento, los programas que hemos construido han seguido un flujo lineal, 
lo que significa que las instrucciones se ejecutan en el mismo orden, de la primera línea a la última. 
Sin embargo, en la mayoría de los programas necesitamos tomar decisiones y ejecutar instrucciones diferentes 
dependiendo de ciertas condiciones. 
Podemos manipular el flujo de un programa utilizando la instrucción if.

La sintaxis de un if es la siguiente:

if condición:
  # Código a ejecutar si la condición es verdadera
Veamos un ejemplo:

edad = 18
if edad >= 18: 
  print("Eres mayor de edad")

En el código mostrado, la variable edad tiene un valor de 18. Luego, se evalúa si 
la variable edad es mayor o igual a 18 y sólo si es así, se ejecuta el código dentro del bloque 'if'.

La indentación (Espaciado / Sangría) previo al print es obligatoria, python utiliza esa información 
para determinar que ese código solo debe ejecutarse si se cumple la condición.

Es importante destacar que, aunque en este ejemplo el valor está asignado directamente a una variable, 
en la práctica este valor podría provenir de un formulario, un archivo, ser ingresado por el usuario o generado por un número aleatorio.

Con condiciones podemos crear programas que tomen decisiones dependiendo de la información disponible.
'''

#Ejercicio
'''
El siguiente programa está mal configurado, alguien cambió la 
contraseña y ahora no funciona correctamente. 
Debería mostrar que el código es correcto si la variable codigo es igual a "1234". 
Sin embargo, el programa no muestra nada en absoluto. ¿Puedes corregirlo?
'''

codigo = "1234" # Modifica esta línea
if codigo == "1234": 
  print("Código correcto")
