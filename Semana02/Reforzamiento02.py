"""""
1. El valor de ‘¡HI TuNombre Apellido!’ imprimirlo por pantalla,
el texto debe ser un string y deberás guardarlo en una variable llamada mi_saludo.
Tu nombre completo debe estar en otra variable.
"""
from statistics import median

nombre = "Meylin Kcomt"
mi_saludo = "Hi," + str(nombre)

print ("Punto 1. {}".format (mi_saludo))

""" 
2. Crea una variable tipo int. Luego, multiplica por 10 y restarle el valor de 10.
 Debes hacer todo esto en dos pasos. 
 Finalmente convertirlo a float y mostrar el resultado 
 por pantalla y el tipo de variable también. 
"""

ent01 = 16
ent02 = (ent01 * 10)-10
resultado_float = float(ent02)

print ("punto 2. el resultado es {}".format(resultado_float,type(resultado_float)))

"""
3. Crear una variable tipo string, luego súmala con otra variable tipo int, 
para esto convertir una de las variables para realizar este procedimiento sin errores.
 Mostrar la suma en pantalla. 
"""

var03 = "8500"
var04 = 650
suma = int(var03) + var04
print ("Punto 3. El resultado es {}".format(suma))


"""
4. Hallar el volumen de una esfera, 
cada dato requerido para hallar el volumen debe estar en una variable. 
Mostrar el volumen por pantalla indicándoselo al usuario. Considera a π  = 3.14159 
"""

pi  = float (3.14159)
radio = 5.5
volumen =float ((4/3) * pi)*pow(radio,3)

print ("Punto 4. El resultado es {} ".format(f"{volumen:.2f}"))

"""
5. Crear un programa que inicia creando un sueldo en una variable, 
sepamos si es par o impar mediante un mensaje. 
Utilizar módulo y condicional (if). 
"""
sueldo = 451
if sueldo % 2 == 0:
    print ("Punto 5.El sueldo es {} es par " .format(sueldo))
else:
    print ("Punto 5.El sueldo es {} es impar " .format(sueldo))

"""
6. Calcular la media de 5 datos (floats), 
cada dato debe estar en una variable y la media también. 
Mostrar el resultado en pantalla y el tipo de dato también mostrarlo. 
"""
var05 = 5.6
var06 = 6.5
var07 = 7.8
var08 = 9.5
var09 = 10.2

media = float((var05 + var06 + var07 + var08 + var09) / 5)
print("Punto 6.La media es {} y el tipo de dato es: {}".format(media, type(media)))

"""
7. De 3 números asignados mayores a 30 (entre positivos y negativos tú los propones) a 3 variables, 
se pide hallar la suma de los valores de los módulos con 3, 5, y 7 respectivamente, 
mostrar en pantalla el valor de la suma. 
"""

num1 = 35
num2 = -45
num3 = 90

mod_3 = num1 % 3
mod_5 = num2 % 5
mod_7 = num3 % 7

sum_mod =  mod_3 + mod_5 + mod_7

print ("Punto 7. La suma de los 3 mod es {}".format(sum_mod))

"""
8. Usando la condicional if imprimir por pantalla si una lista ([]) está vacía o no, 
comprobar con una lista vacía y otra con una lista con dato al menos ([dato_1, dato_2]). 
"""
clientes = []

nombre_clientes = ['Perez','Lopez','Sanchez']


if clientes:
    print("Punto 8_a.La lista '{}' NO está vacía. ¡Tiene datos!".format(clientes))
else:
    print("Punto 8_a.La lista '{}' SÍ está vacía. ¡No tiene datos!".format(clientes))

if nombre_clientes:
    print("Punto 8_b.La lista {} NO está vacía. ¡Tiene elementos!".format(nombre_clientes))
else:
     print("Punto 8_b.La lista {} SÍ está vacía. ¡No tiene elementos!".format(nombre_clientes))

"""
9. Elevar una base al exponente de 6 (que estará dentro una variable), 
este número el cual su valor estará asignado a una variable 
y luego restar este mismo valor multiplicado por dos (usar pow o **). 
Mostrar el resultado final en pantalla. 
"""
base = 10
exp = 6
resultado_exp = pow(base,exp)
resultado_final = resultado_exp - (resultado_exp * 2)

print("Punto 9. El resultado final es {}".format(resultado_final))

"""
10. Crear un programa que tome un número flotante en una variable con 6 decimales y
 se imprima de diferentes modos: - - - 1 decimal 2 decimales 4 decimales 
"""
num4 = 16.568973
dec1 = 1
dec2 = 2
dec4 = 4
print("Punto 10_1. El resultado es {:.1f} con {} decimal(es).".format(num4,dec1))
print("Punto 10_2. El resultado es {:.2f} con {} decimal(es).".format(num4,dec2))
print("Punto 10_3. El resultado es {:.4f} con {} decimal(es).".format(num4,dec4))

"""
11. Identificar qué tipo de dato se obtiene al elevar tu edad con exponente 5 
y luego dividirlo por 10. Mostrar el resultado de su módulo con 3 en pantalla 
"""
edad = 30
exp = 5
resultado_11 = (pow(edad,exp))
resultado_10 = resultado_11/10
resultado_mod = resultado_10 % 3
print ("Punto 11. El resultado de elevar la edad {} al exponente {} es {}, \nesta resultado divido entre 10 da como resultado {} \ny se finaliza con el resultado final del modulo con 3 lo que da {}".format(edad,exp,resultado_11,resultado_10,resultado_mod))

"""
12. Escribe un programa que almacene información de un producto: 
Tu nombre, nombre del producto, precio unitario (float), cantidad (int) 
e imprimirá finalmente algo como lo siguiente: 
Buen día Nombre, 
el detalle de su compra es el siguiente: - Producto: Pollo a la brasa - - - 
Precio unitario: 50.50 
Cantidad: 2 Total a pagar: 101 
"""
nombre = "Meylin"
producto = "Pollo a la Brasa"
precio = 50.50
cant = 2
total_paga = precio * cant

print ("Punto 12.\nBuen dia {},\nEl detalle de su compra es el siguiente:\n {}\n Precio Unitario: {}\n Cantidad:{}\n Total a pagar:{}".format(nombre,producto,precio,cant,int(total_paga)))

"""
13. Crea un programa que convierta una temperatura en grados Celsius a Fahrenheit.
 La fórmula que tiene que tener en cuenta es la siguiente: F = (C * 9)/5  + 32 Deberá imprimir algo como lo siguiente: 
 La temperatura en °C: 30 Temperatura en Fahrenheit: 86.00 Realizarlo con dos distintos datos para la temperatura en Celsius 
(usar dos variables iniciales para obtener dos temperaturas finales en Fahrenheit) 
"""

temp_celsius_1 = 30
temp_celsius_2 = 35
temp1_fahrenheit = (temp_celsius_1 * 9/5)+32
temp2_fahrenheit = (temp_celsius_2 * 9/5)+32

print("La temperatura en °C: {} Temperatura en Fahrenheit: {:.2f}".format(temp_celsius_1,temp1_fahrenheit))
print("La temperatura en °C: {} Temperatura en Fahrenheit: {:.2f}".format(temp_celsius_2,temp2_fahrenheit))

