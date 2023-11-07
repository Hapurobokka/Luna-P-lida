import prototipo_inventario as g_inventario
import control_acciones as acciones
from sys import exit
		

inventario = []
instancia = 1

acciones.inicio_juego()

accion = input("> ")

acciones.control_principal(accion, instancia, inventario)

g_inventario.mostrar_inventario(inventario)