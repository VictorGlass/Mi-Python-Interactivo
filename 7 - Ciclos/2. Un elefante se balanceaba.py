'''
Un elefante se balanceaba

Ideas clave
*Con while podemos repetir un bloque de código mientras una condición sea verdadera.
*Es importante asegurarse de que la condición del while eventualmente se vuelva falsa para evitar bucles infinitos.
*Podemos usar print() para mostrar texto en la consola.
*Las f-strings en Python permiten insertar valores de variables directamente en strings.

Generador de la Canción del Elefante

La canción "Un elefante se balanceaba" es una canción infantil que cuenta cómo los elefantes se 
van sumando uno a uno sobre la tela de una araña. 
Vamos a crear una función que genere esta canción automáticamente.

Ejemplo de cómo funciona la canción:

1 elefante se balanceaba sobre la tela de una araña,
como veía que resistía, fue a llamar a otro elefante.

2 elefantes se balanceaban sobre la tela de una araña,
como veían que resistía, fueron a llamar a otro elefante.

3 elefantes se balanceaban sobre la tela de una araña,
como veían que resistía, fueron a llamar a otro elefante.

...y así sucesivamente.
'''

#Ejercicio
'''
Crea una función llamada cancion_elefantes que genere la letra de esta canción para los primeros 10 elefantes.

Ejemplos:

cancion_elefantes()
1 elefante se balanceaba sobre la tela de una araña,
como veía que resistía, fue a llamar a otro elefante.
2 elefantes se balanceaban sobre la tela de una araña,
como veían que resistía, fueron a llamar a otro elefante.
...
10 elefantes se balanceaban sobre la tela de una araña,
como veían que resistía, fueron a llamar a otro elefante.
El uso interpolación es útil para este tipo de situaciones. 

Recuerda: print(f"Hola, me llamo {nombre} y tengo {edad} años.") Utiliza ciclos para generar el texto de la canción. 
La función no debe retornar valor alguno, utiliza print() para mostrar la canción.
'''

# Escribe tu código aquí

#Funcion para la cancion:
def cancion_elefantes():
    #Variable de contador de elenfantes:
    contador_elefantes = 1

    #Mientras el contador sea menor que 10...
    while contador_elefantes <= 10:
        
        #Si el contador es igual a 1:
        if contador_elefantes == 1:
            print(f"{contador_elefantes} elefante se balanceaba sobre la tela de una araña, ")
            print("como veia que resistia, fue a llamar a otro elefante.")
            print()
        else:
            print(f"{contador_elefantes} elefantes se balanceaban sobre la tela de una araña, ")
            print("como veian que resistian, fueron a llamar a otro elefante.")
            print()
            #Contador y autoincremento.
        contador_elefantes +=1

#Llamando a la funcion:
cancion_elefantes()
# Fin   

