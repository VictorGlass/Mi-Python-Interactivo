'''
Membresías

Ideas clave
*En Python, podemos verificar si un elemento está presente en una lista utilizando el operador in.
*El operador in devuelve True si el elemento está en la lista y False si no lo está.

Verificando membresía en listas

Una membresía se refiere a la presencia de un elemento en la lista. En Python, el operador in nos permite verificar 
fácilmente si un elemento está presente en una lista. La sintaxis básica es:

elemento in lista
Esta expresión devuelve True si el elemento está en la lista y False si no lo está. Por ejemplo:

frutas = ["manzana", "banana", "cereza", "dátil"]
print("manzana" in frutas)  # True
print("kiwi" in frutas)     # False
'''

#Ejercicio
'''
Crea una función llamada miembro_en_dos que recibe 3 parámetros: arr1, arr2, y valor. 
La función debe retornar True si valor está presente en ambas listas arr1 y arr2, y False en caso contrario.
'''

# Escribe tu código aquí
def miembro_en_dos(arr1, arr2, valor):
    if valor in arr1 and valor in arr2:
        return True
    elif valor in arr2:
        return False
    elif valor in arr1 and arr2:
        return True
    else:
        return "No aparece en ninguno de los dos"

# Fin
arr1 = ["Nueva York", "Londres", "Tokio", "Sídney"]
arr2 = ["Londres", "París", "Tokio", "Berlín"]

print(miembro_en_dos(arr1, arr2, "Londres"))  
print(miembro_en_dos(arr1, arr2, "París"))   
print(miembro_en_dos(arr1, arr2, "Tokio"))  
print(miembro_en_dos(arr1, arr2, "Chile"))
