'''
Membresía y listas

Ideas clave
*En Python, podemos verificar si un elemento está presente en una lista utilizando el operador in.
*El operador in devuelve True si el elemento está en la lista y False si no lo está.
*Podemos combinar el operador in con bucles para realizar verificaciones sobre múltiples elementos.
*Esta operación es útil para filtrar datos o verificar condiciones basadas en la presencia de elementos en una lista.

Verificando membresía en listas

En Python, el operador in nos permite verificar fácilmente si un elemento está presente en una lista. La sintaxis básica es:

elemento in lista
Esta expresión devuelve True si el elemento está en la lista y False si no lo está. Por ejemplo:

frutas = ["manzana", "banana", "cereza", "dátil"]
print("manzana" in frutas)  # True
print("kiwi" in frutas)     # False
Podemos combinar esto con un bucle para verificar múltiples elementos:

frutas = ["manzana", "banana", "cereza", "dátil"]
buscar = ["manzana", "kiwi", "cereza"]

for fruta in buscar:
    if fruta in frutas:
        print(f"{fruta} está en la lista de frutas")
    else:
        print(f"{fruta} no está en la lista de frutas")
Este código imprimirá:

manzana está en la lista de frutas
kiwi no está en la lista de frutas
cereza está en la lista de frutas

La verificación de membresía es útil en muchos escenarios, como filtrar datos, verificar condiciones o buscar 
elementos específicos en una colección de datos.
'''

#Ejercicio
'''
Crea una función llamada contar_presentes que reciba dos listas como parámetros: una lista de elementos a buscar y una lista donde buscar. 
La función debe devolver el número de elementos de la primera lista que están presentes en la segunda lista.

Ejemplo:

frutas = ["manzana", "banana", "cereza", "dátil", "uva"]
buscar1 = ["manzana", "kiwi", "cereza"]
buscar2 = ["pera", "sandía", "mango", "uva"]

print(contar_presentes(buscar1, frutas))  # 2
print(contar_presentes(buscar2, frutas))  # 1
'''

# Escribe tu código aquí  
def contar_presentes(lista1, lista2):
    contador = 0
    for elemento in lista1:
        if elemento in lista2:
            contador +=1
    return contador
    

# Fin
print(contar_presentes(["a","b","c"],["x","y","z","a","b"])) 
print()
print(contar_presentes([1,2,3,4],[1,3,5,7,9])) 
print()
print(contar_presentes(["rojo","verde","azul"],["amarillo","verde","naranja","azul"])) 