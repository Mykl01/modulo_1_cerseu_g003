
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
