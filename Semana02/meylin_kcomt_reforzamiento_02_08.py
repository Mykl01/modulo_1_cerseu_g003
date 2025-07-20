
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
