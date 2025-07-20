
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
