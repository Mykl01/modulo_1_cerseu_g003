""" Meylin Kcomt Loo

Requisitos

1. Crear 2 variables enteras, 2 varaibles flotanes, 2 variable string, 1 variables string con contenido netamiente
numérico y una variable boolean
2. Obtener y mostrar la suma de una variable entera con la variable string numérica
(Conversiones, realizarla si fuera necesario)
3. Obtener y mostrar la suma de las 2 variables enteras más la variable string numérica y la variable flotantes
4. Obterner y mostrar el módulo de las variables enteras: %
5. Obtener y mostrar el resultado o la parte entera de las 2 variables int: //
6. Obtener una potencia usando una de las variables foltantes como base y la variable entera como pontencia

Nota: Las variables string pueden ser tu nombre y apellido

Hora de entrega máxima : 7pm
Correo: docente.cerseu.unmsm@gmail.com
Asunto: Ejercicio Participación - Semana 02
Adjuntar archivo .py
En la parte superior dejar su nombre y apellido: como comentario

Adjuntar versión de git a su correo: WIN+R, escribir CMD y enter -> git --version
"""

# 1. Crear variables
ent1 = 10
ent2 = 3

float1 = 2.5
float2 = 4.8

nombre = "Meylin"
apellido = "Kcomt"

text_num = "7"  #este es el string numerico
var01 = True      #este es el booleano
var02 = 600%30

# 2. Suma de variable entera + string numérico (convertimos string a entero)
sum_ent = ent1 + int(text_num)
print("El resultado de la suma es {}, ejecutado por {} {}".format(sum_ent,nombre,apellido))

# 3. Suma de los enteros + string numérico + flotantes
sum_total = ent1 + ent2 + int(text_num) + float1 + float2
print("El resultado de la Suma total es {} , ejecutado por {} {}".format (sum_total,nombre,apellido))

# 4. Módulo de las variables enteras
mod = var02 % var01
print("El resultado del modulo es {} ".format (mod))

# 5. Parte entera de la división (división entera)
division = ent1 // ent2
print ("El resultado de la division es {}".format(division))

# 6. Potencia: el flotante1 elevado a un entero2
pot = float1 ** ent2
print("El resultado de la Potencia es {}".format(pot))
