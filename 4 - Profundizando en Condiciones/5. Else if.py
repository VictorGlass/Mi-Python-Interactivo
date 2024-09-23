'''
Else if

Ideas clave
*La sentencia if se utiliza para ejecutar código si se cumple una condición.
*La sentencia if...else se utiliza para ejecutar código si se cumple una condición y otro código si no se cumple.
*La sentencia elif, la cual es una abreviatura de else if, se utiliza para evaluar múltiples opciones.
*Las tres sentencias se combinan para evaluar múltiples condiciones, se lee cómo si se 
 cumple la condición 1, entonces se ejecuta el código 1, si no se cumple la condición 1, 
 se evalúa la condición 2, si se cumple la condición 2, se ejecuta el código 2, si no se cumple la condición 2, 
 se ejecuta el código 3 y si no se cumple ninguna de las condiciones anteriores (else), se ejecuta el código 4.

Elif

En ciertos escenarios, es necesario evaluar múltiples opciones. Por ejemplo, 
al determinar si un número es mayor, menor o igual a otro. En estos casos, empleamos la sentencia elif.

Imaginemos que queremos crear una función que adivine nuestro color favorito:

def adivina_color(color):
    if color == "azul":
        return "Adiviné, mi color favorito es azul"
    elif color == "verde":
        return "Mi segundo color favorito es verde"
    elif color == "rojo":
        return "Mi tercer color favorito es rojo"
    else:
        return "Estás equivocado, mi color favorito no es " + color

Podemos observar que la sentencia elif nos permite evaluar más de una opción. 
Si la primera condición no se cumple, se evalúa la siguiente condición. 
Si ninguna condición se cumple, se ejecuta el código dentro del bloque else.
'''

#Ejercicio
'''
Crea una función que se llame adivinaNumero y que dependa de un parámetro numero.

Si el número es 7, la función debe retornar "Adivinaste el número secreto".

Si el número es 6, la función debe retornar "Casi, pero no es el número secreto".

Cualquier otro número debe retornar "Estás equivocado, el número secreto no es " 
seguido del número que se ingresó. 
Por ejemplo: Si el número ingresado es 8, la función debe retornar "Estás equivocado, el número secreto no es 8".

Pistas:

*Puedes utilizar la sentencia else if para evaluar más de una opción.
*No olvides que el bloque else se ejecuta si ninguna de las condiciones anteriores se cumple.
*Cuida la ortografía y los espacios en los mensajes que retornas. 
Influyen en la evaluación de los ejercicios. Puedes copiar y pegar los mensajes de ejemplo para evitar errores.
*Se pide retornar los mensajes, no mostrarlos con print.
'''

# Escribe tu código aquí
def adivinaNumero(numero):
    if numero == 7:
        return "Adivinaste el numero secreto"
    elif numero == 6:
        return "Casi, pero no es el numero secreto"
    else:
        print(f"Estas equivocado, el numero secreto no es: {numero}")

# Fin

print(adivinaNumero(7))
print(adivinaNumero(8))
print(adivinaNumero(6))