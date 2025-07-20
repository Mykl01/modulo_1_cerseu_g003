
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
