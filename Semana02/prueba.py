# --- Caso 1: Lista Vacía ---
mi_lista_vacia = [1]

# La condición 'if mi_lista_vacia:' se evalúa a False porque la lista está vacía.
if mi_lista_vacia:
    print("La lista '{}' NO está vacía. ¡Tiene elementos!".format(mi_lista_vacia))
else:
    print("La lista '{}' SÍ está vacía. ¡No tiene elementos!".format(mi_lista_vacia))

print("-" * 40) # Separador para mejor lectura