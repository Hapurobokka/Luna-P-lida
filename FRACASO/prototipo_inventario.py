def sumar_objeto(objeto, inventario):
    """
    Esta función añade el objeto especificado al inventario
    """
    inventario.append(objeto)


def remover_objeto(objeto, inventario):
    """
    Esta función elimina la primera instancia del objeto especificado del
    inventario
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


def objeto_en_inventario(objeto, inventario):
    if objeto in inventario:
        return True


def control_inventario(argumento, objeto, inventario):

    if objeto_en_inventario(objeto, inventario) == False:
        print("Ese objeto no esta en el inventario") 
    else:
        if argumento == "inspeccionar":
            