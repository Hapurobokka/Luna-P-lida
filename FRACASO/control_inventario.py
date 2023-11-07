def sumar_objeto(objeto, inventario):
	"""
	Añade un objeto al inventario del jugador.
	"""
	inventario.append(objeto)	


def remover_objeto(objeto, inventario):
    """
    Elimina la primera instancia del objeto seleccionado del inventario
    del jugador.
    """
    inventario.remove(objeto)


def mostrar_inventario(inventario):
    """
    Esta función le muestra al jugador su inventario a manera de lista
    """
    print("\n")

    print("Tu inventario actual es: ")
    for objeto in inventario:
        print("-", objeto)

    print("\n")


def control_inventario_p(interaccion, objeto, inventario):
	pass	
