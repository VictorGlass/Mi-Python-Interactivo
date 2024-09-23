'''
Obtener día

Ideas clave
*La sentencia if se utiliza para ejecutar código si se cumple una condición.
*La sentencia if...else se utiliza para ejecutar código si se cumple una condición y otro código si no se cumple.
*La sentencia elif se utiliza para evaluar múltiples opciones.
*Las tres sentencias se combinan para evaluar múltiples condiciones. 
Se lee así: si se cumple la condición 1, entonces se ejecuta el código 1; si no se cumple la condición 1, 
se evalúa la condición 2; si se cumple la condición 2, se ejecuta el código 2; si no se cumple la condición 2, 
se ejecuta el código 3; y si no se cumple ninguna de las condiciones anteriores (else), se ejecuta el código 4.
'''

#Ejercicio
'''
Utilizando lo aprendido en ejercicios anteriores, crea una función llamada obtener_dia que permita 
obtener el nombre correspondiente al día de la semana a partir del parámetro día. 
El valor pasado será un número del 0 al 6 que representa el día de la semana. 
Si el día es 0, la función debe retornar "Domingo". 
Si el día es 1, la función debe retornar "Lunes", y así sucesivamente hasta el día 6 que corresponde a "Sábado". 
Si el día es cualquier otro valor, la función debe retornar "Valor inválido".

Pistas:

No muestres los mensajes con print, solo retorna el mensaje. Ten cuidado con las mayúsculas y minúsculas de los mensajes y la ortografía.
La función solo debe devolver el nombre del día sin puntos ni comas y con la primera letra en mayúscula.
Hacer un diagrama de flujo te puede ayudar a visualizar el problema.
'''

# Escribe tu código aquí
def obtener_dia(dia):
    if dia == 0:
        return "Domingo"
    elif dia == 1:
        return "Lunes"
    elif dia == 2:
        return "Martes"
    elif dia == 3:
        return "Miercoles"
    elif dia == 4:
        return "Jueves"
    elif dia == 5:
        return "Viernes"
    elif dia == 6:
        return "Sabado"
    else:
        print("Valor invalido")

# Fin

print(obtener_dia(1))
print(obtener_dia(2))
print(obtener_dia(6))
print(obtener_dia(9))

