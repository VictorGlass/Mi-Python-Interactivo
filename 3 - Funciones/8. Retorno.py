'''
Retorno

Ideas clave
*Retornar un valor no es lo mismo que mostrar un valor.
*Si piden mostrar un valor utilizaremos print. Cuando nos piden retornar un valor, debemos utilizar return.
*Una función puede tener un retorno utilizando la palabra return seguida de una expresión. Ejemplo: return a + b.
*Si el return no se especifica, la función retornará undefined.

Las funciones como cajas negras

Las funciones son como cajas que guardan instrucciones que tienen puntos de entrada donde 
podemos enviarle datos, y un punto de salida donde puede devolver datos. 
Los puntos de entrada se llaman parámetros y el punto de salida se llama retorno.

Creando una función que retorne un valor

Veamos un ejemplo:

def sumar(a, b):
  return a + b


print(sumar(5, 3)) # 8 
print(sumar(10, 20)) # 30 

En este ejemplo, la función sumar retornará la suma de los parámetros a y b.

El valor que retorna la función se puede guardar en una variable para utilizarlo posteriormente.

resultado1 = sumar(5, 3)
resultado2 = sumar(resultado1, 20)
print(resultado2) # 28 

Por ahora, más que entender los detalles, lo importante es entender los conceptos de 
parámetros y retorno, ya que los utilizaremos en ejercicios futuros. 
La mayoría de los ejercicios consistirá en crear una función que reciba parámetros y retorne un valor específico de acuerdo a las instrucciones.
'''

#Ejercicio
'''
Crea la función multiplicar que dependa de dos parámetros y que retorne la multiplicación de ambos.

Casos de prueba
Puedes revisar los argumentos que ejecutaremos para evaluar tu función:
'''


#print(multiplicar(5,3))
#print(multiplicar(10,20))
#print(multiplicar(7,8))

# Escribe tu código aquí 

def multiplicar(a, b):
    return a * b

print(multiplicar(5, 3))
print(multiplicar(10, 20))
print(multiplicar(7, 8))