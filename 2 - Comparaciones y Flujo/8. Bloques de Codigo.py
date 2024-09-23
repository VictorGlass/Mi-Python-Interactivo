'''
Bloques de código

Ideas clave
*Podemos cambiar el flujo de un programa utilizando condiciones.
*Un bloque es un conjunto de instrucciones que se ejecutan juntas.

¿Qué es un bloque?

Un bloque de código o simplemente bloque es un conjunto de instrucciones que se ejecutan juntas.

En Python, los bloques se delimitan por la indentación, como se muestra en el siguiente ejemplo:

if condición:
  # Conjunto de instrucciones si la condición se cumple
else:
  # Conjunto de instrucciones si la condición no se cumple

Los bloques resultan útiles para ejecutar un conjunto de instrucciones si una condición se cumple, o si no se cumple.

Veamos un ejemplo práctico:

color = "azul"
if color === "azul":
  print("La variable color es azul")
  print("El azul es mi color favorito")

En este caso, ambos mensajes se mostrarán ya que la condición se cumple. 
Sin embargo, si cambiamos el valor de color a "rojo", entonces ninguno de los mensajes se mostrará.

Ahora, probemos el mismo código dejando solo el primer mensaje dentro del bloque:

color = "rojo"
if (color == "azul") 
  print("La variable color es azul")
print("El azul es mi color favorito")

En este segundo ejemplo, si la variable color es "azul", se mostrarán ambos mensajes. 
Pero si fuera cualquier otro color, se mostrará únicamente el segundo mensaje, 
independientemente de si la condición se cumple o no.

Desde el momento en que se escribe el bloque if, la indentación es obligatoria. 
Python utiliza esa información para determinar que ese código solo debe ejecutarse si se cumple la condición.
'''

#Ejercicio
'''
El programador que escribió este código no dejó los prints dentro del bloque 
if por lo que el código no funciona como debería. ¿Puedes corregirlo?
'''


#formulario = "incompleto";
#if formulario == "completo":
#print("Formulario completo");
#print("Enviando email"); 
#print("Este mensaje debe aparecer siempre"); 
# Fin

# Escribe tu código aquí.
formulario = "incompleto"
if formulario == "completo":
    print("Fromulario completo")
    print("Enviando email")
    print("Este mensaje debe aparecer siempre")