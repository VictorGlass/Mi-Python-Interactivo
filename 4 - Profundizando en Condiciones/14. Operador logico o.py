'''
Operador lógico o

Ideas clave
*Los valores booleanos pueden ser True o False y pueden ser almacenados en variables de la misma manera que guardamos números o textos.
*El operador de negación, representado por el símbolo !, invierte el valor de verdad de una expresión.
*El operador lógico and nos permite combinar dos o más condiciones. Cada condición individual debe ser verdadera para que la expresión completa sea verdadera.
*El operador lógico or nos permite combinar dos o más condiciones. Basta con que una de las condiciones sea verdadera para que la expresión completa sea verdadera.

El operador lógico or

Existe un tercer operador lógico muy utilizado que es el operador o or. 
Este operador devuelve verdadero si al menos una de las condiciones es verdadera. Por ejemplo:

def verificar_descuento_por_edad(edad):
    if edad < 12 or edad > 60:
        return "Califica para descuento"
    return "No califica para descuento"

Aquí, basta con que una de las dos condiciones sea verdadera para que la función retorne "Califica para descuento".
'''

#Ejercicio
'''
Crea una función llamada verificar_puntaje que dependa de un parámetro puntaje. 
La función debe retornar "Califica para bono" si el puntaje es mayor que 90 o menor que 10. 
En caso contrario, la función debe retornar "No califica para bono".
'''

# Escribe tu código aquí
def verificar_puntaje(puntaje):
    if puntaje > 90 or puntaje < 10:
        return "Califica para bono"
    else:
        return "No califica para bono"
# Fin
print(verificar_puntaje(91))
print(verificar_puntaje(6))
print(verificar_puntaje(40))

