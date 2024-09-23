'''
Tipos booleanos

Ideas clave
*Existe un tipo de dato que únicamente se compone de verdaderos y falsos. 
 Este tipo de dato se llama booleano o bool.
*Los valores booleanos pueden ser True o False y pueden ser almacenados en 
 variables de la misma manera que guardamos números o textos.

Tipos Booleanos

Los valores True y False pertenecen a un tipo especial de datos llamados booleanos. 
El nombre booleano es en honor al matemático George Boole, quien inventó la lógica booleana, 
un sistema de lógica que solo tiene dos valores posibles: verdadero (True) y falso (False).

Así como el sistema lógico creado por George Boole, los valores booleanos son exclusivamente 
verdaderos (true) o falsos (false) y pueden ser almacenados en variables de la misma manera 
que guardamos números o textos u otros tipos de datos.

a = True
b = False

if a == True:
    print("a es verdadero")

if a:  # Esta expresión es equivalente a la anterior
    print("a es verdadero")

if b == False:
    print("b es falso")

Un detalle importante a observar es que los valores son True y False y no "True" y "False". 
Los valores True y False son palabras reservadas en Python que representan los valores booleanos 
verdadero y falso, respectivamente. 
Por otro lado, "True" y "False" son cadenas de texto que representan palabras y no valores booleanos.
'''

#Ejercicio
'''
Agrega los datos del tipo correspondiente a las variables usuarioRegistrado y usuarioPremium para que el programa funcione correctamente.
El programa funcionando correctamente debería mostrar que el usuario está registrado y que es premium.
'''

#usuarioRegistrado =  # Agrega el tipo de dato correcto 
#usuarioPremium = # Agrega el tipo de dato correcto 

#if usuarioRegistrado:
#  print("El usuario está registrado")
#  if usuarioPremium:
#    print("El usuario es premium")
#  else:
#    print("El usuario no está registrado")

# Escribe tu código aquí

usuarioRegistrado = True
usuarioPremium = False

if usuarioRegistrado:
    print("El usuario esta registrado")
    if usuarioPremium:
        print("El usuario es premium")
    else:
        print("El usuario no esta registrado")

