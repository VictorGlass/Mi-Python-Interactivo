'''
If anidado parte 3

Ideas clave
*Existe un tipo de dato que únicamente se compone de verdaderos y falsos. 
 Este tipo de dato se llama booleano o bool.
*Los valores booleanos pueden ser True o False y pueden ser almacenados en 
 variables de la misma manera que guardamos números o textos.

A continuación, vamos a realizar un ejercicio similar al anterior, 
pero en lugar de comparar contra cadenas de texto, vamos a comparar contra valores booleanos.
'''

#Ejercicio
'''
Se busca hacer un asistente que te ayude a revisar todo lo que tienes que llevar antes de salir de casa. 
Para esto, se te pide crear una función que se llame revisar_antes_de_salir que depende de dos parámetros llaves y celular.

*Si tienes las llaves y el celular, la función debe retornar "Todo listo, puedes salir de casa".
*Si tienes solo las llaves, la función debe retornar "Te falta el celular".
*Si no tienes las llaves, la función debe retornar "Te falta las llaves".

Los valores que pueden tomar llaves y celular son True o False, donde True significa 
que tienes el objeto y False que no lo tienes. 
No se pide considerar otros valores.
'''


# Escribe tu código aquí
def revisar_antes_de_salir(llaves, celular):
    if llaves and celular:
        return "Todo listo, puedes salir de casa"
    elif llaves:
        return "Te falta el celular"
    else:
        return "Te falta las llaves"     
# Fin
print(revisar_antes_de_salir(True, True))
print(revisar_antes_de_salir(True, False))
print(revisar_antes_de_salir(False, True))
print(revisar_antes_de_salir(False, False))