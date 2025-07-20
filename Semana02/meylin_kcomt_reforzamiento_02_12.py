
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
