"""Requisitos:

1. Crear dos varaibles para los valores de nombre, profesión y ciudad
2. Crear 2 varialbes para la remuneración de enero y febrero (más de 1500)
3. Crear 1 variable donde se sumará el ingreso de los dos meses de enero y febrero
4. Mostrar en pantalla el mensaje de:

"Hola soy 'nombre' mi profesión es 'profesión' y mi remnuneración acumulada es de 'remuneracion_total''"
"""


#creacion de las variables
nombre = "Meylin"
profesion = "Sociologo"
nacionalidad = "Peruana"
ciudad = "Lima"
r_enero = 1500
r_febrero = 2500
acum = r_enero + r_febrero

print("Hola soy {} mi profesión es {} , soy de la ciudad de {} y mi remnuneración acumulada es {} ".format(nombre,profesion,ciudad,acum))