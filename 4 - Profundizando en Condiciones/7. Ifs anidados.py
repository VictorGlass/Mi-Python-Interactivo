'''
Ifs anidados

Ideas clave
*Una sentencia if puede estar dentro de otra, lo cual se conoce como un if anidado.
*El if interior solo es ejecutado si el if exterior es verdadero. Si el if exterior es falso, el if interior no es ejecutado.

if anidado

Una sentencia if puede estar dentro de otra, lo cual se conoce como un if anidado. En código se vería de la siguiente manera:

if condicion1:
    print("Código a ejecutar si la condición 1 es verdadera")
    if condicion2:
        print("Código a ejecutar si la condición 1 y 2 son verdaderas")
El if interior solo es ejecutado si el if exterior es verdadero. Si el if exterior es falso, el if interior no es ejecutado.
'''

#Ejercicio
'''
Se busca hacer un asistente que te ayude a revisar todo lo que tienes que llevar antes de salir de casa. 
Para esto se te pide crear una función que se llame revisarAntesDeSalir que depende de dos parámetros llaves y celular,

*Si tienes las llaves y el celular, la función debe retornar "Todo listo, puedes salir de casa".
*Si tienes solo las llaves, la función debe retornar "Te falta el celular".
*Si no tienes las llaves, la función debe retornar "Te falta las llaves".

Los valores que pueden tomar llaves y celular son 'Si' o 'No', donde 'Si' significa que tienes el objeto 
y 'No' que no lo tienes, no se pide considerar otros valores. Si y No deben ser escritos con la primera letra en mayúscula.

Tip 1: No inventes situaciones adicionales, solo considera las tres opciones mencionadas. 
Tip 2: Copia y pega los mensajes para evitar errores de tipeo. Tip 3: Se pide retornar los mensajes, no mostrarlos con print.
'''

# Escribe tu código aquí
def revisarAntesDeSalir(llaves, celular):
    if llaves == "Si" and celular == "Si":
        return "Todo listo, puedes salir de casa"
    elif llaves == "Si" and celular == "No":
        return "Te falta el celular"
    elif llaves == "No" and celular == "Si":
        return "Te falta las llaves"
    else:
        return "Vuelve a revisar todo de nuevo"


# Fin 
print(revisarAntesDeSalir('Si', 'Si'))
print(revisarAntesDeSalir('Si', 'No'))
print(revisarAntesDeSalir('No', 'Si'))
print(revisarAntesDeSalir('No', 'No'))

