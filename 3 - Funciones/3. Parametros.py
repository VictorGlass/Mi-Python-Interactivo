'''
Parámetros

Ideas clave
*Una función puede depender de parámetros para llevar a cabo su tarea.
*Utilizando parámetros, podemos hacer que una función se adapte a diferentes situaciones.

Las funciones como un robot

Consideremos estas dos opciones.

*Tenemos un robot que saluda a cada persona con un "Hola".
*Tenemos un robot que saluda a cada persona con un "Hola" seguido de su nombre, 
pero para ello necesita saber el nombre de la persona.

Podemos imaginar una función como un robot que realiza una tarea. 
El primer caso sería una función que muestre el mensaje "Hola" cada vez que se llama. 
En el segundo caso, es una función que muestra un mensaje personalizado, 
pero para ello necesita como entrada el nombre de la persona.

¿Qué son los parámetros?

Los parámetros son los valores de los que depende una función para realizar una tarea. 
Depender de valores hace que una función sea más versátil y adaptable a diferentes situaciones.

Veamos un ejemplo en código de una función que salude a una persona con su nombre:

def saludar(nombre):
    print("Bienvenido, " + nombre)

saludar("Alex")  # Bienvenido, Alex
saludar("Juan")  # Bienvenido, Juan
saludar("Pepe")  # Bienvenido, Pepe

En el ejemplo mostrado, la función saludar depende del parámetro nombre, 
que se utiliza para personalizar el mensaje de bienvenida. Al llamar a la 
función con diferentes nombres, cada llamada produce un mensaje único y personalizado. 
Esto ilustra cómo los parámetros permiten que una función sea más versátil y adaptable a diversas situaciones.
'''

#Ejercicio
'''
Se ha definido una función llamada mostrar_mensaje_secreto. 
Esta función depende de un parámetro llamado mensaje. 
Si el mensaje es "secreto", mostrará "Mensaje correcto". 
Sin embargo, si el mensaje es cualquier otro, la función finalizará, 
mostrando "Término de la función".

Para resolver el ejercicio debes llamar a la función dos veces, 
primero, con el mensaje "secreto" y luego con el mensaje "no secreto" para verificar que funciona correctamente.
'''

#def mostrar_mensaje_secreto(mensaje):
#    if mensaje == "secreto":
#        print("Mensaje correcto")
#    print("Término de la función")

# Escribe tu código aquí

def mostrar_secreto(mensaje):
    if mensaje == "secreto":
        print("Mensaje correcto")
    else:
        print("Termino de la funcion")

mostrar_secreto("secreto")
mostrar_secreto("no secreto")
# Fin


