
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
