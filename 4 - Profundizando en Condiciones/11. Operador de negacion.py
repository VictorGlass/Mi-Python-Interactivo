'''
Operador de negación

Ideas clave
*Los valores booleanos pueden ser True o False y pueden ser almacenados en variables de la misma manera que guardamos números o textos.
*El operador lógico not, invierte el valor de verdad de una expresión.
 not True es igual a False y not False es igual a True.

El operador de negación

El operador lógico not invierte el valor de verdad de una expresión. 
Si la expresión es verdadera, el operador la convierte en falsa; y si la expresión es falsa, el operador la convierte en verdadera.

Veamos el operador en acción:

a = True
print(not a)  # False
print(not not a)  # True
print(not not not a)  # False
print(not not not not a)  # True

b = False
print(not b)  # True

print(not False)  # True
print(not True)  # False
'''

#Ejercicio
'''
Crea una función llamada llevarLaContraria que dependa de un parámetro expresion. 
La función debe retornar el valor contrario de la expresión.
'''

# Escribe tu código aquí
def llevarLaContraria(expresion):
    return not expresion
# Fin

print(llevarLaContraria(True))
print(llevarLaContraria(False))
