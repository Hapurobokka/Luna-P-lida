from control_uno import inspecciones_cue, recolecciones_cue, miscelaneos_cue
from control_uno import d_texto, d_bool, d_lista, cueva_terminada
from control_dos import movimiento_lab, inspecciones_lab, recolecciones_lab, miscelaneos_lab
from control_dos import l_texto, laberinto_terminado, introduccion_laberinto, claves_misc
from menu_trampas import control_trampas

from sys import exit
def laberinto_oculto(inventario):
	global laberinto_terminado, introduccion_laberinto

	if introduccion_laberinto is False:
		print(l_texto["Inicio laberinto"])
		introduccion_laberinto = True

	accion = input("> ")

	try:
		clave, cadena = accion.split(" ", 1)
	except ValueError:
		print("Un comando tiene que tener al menos dos palabras")
		return

	match clave:
		case accion if accion in claves_misc:
			miscelaneos_lab(clave, cadena, inventario)
		case "moverse":
			movimiento_lab(cadena, inventario)
		case "inspeccionar":
			inspecciones_lab(cadena, inventario)
		case "recoger":
			recolecciones_lab(cadena, inventario)
		case "activar" if "trampas" in cadena:
			control_trampas(inventario)
		case "terminar" if "programa" in cadena:
			exit(0)
		case _:
			print("Comando no reconocido")


def cueva_submarina(inventario):
	global cueva_terminada

	condiciones_salida = "Mapa de la Isla" in inventario

	if not d_bool["Introduccion cueva"]:
		print(d_texto["Inicio cueva"])
		d_bool["Introduccion cueva"] = True

	if "Mapa de la Isla" in inventario and not d_bool["Mensaje final"]:
		print(d_texto["Final cueva"])
		d_bool["Mensaje final"] = True

	accion = input("> ")

	try:
		clave, cadena = accion.split(" ", 1)
	except ValueError:
		print("Un comando tiene que tener al menos dos palabras")
		return

	match clave:
		case "inspeccionar":
			inspecciones_cue(cadena, inventario)
		case "recoger":
			recolecciones_cue(cadena, inventario)
		case accion if accion in d_lista["Claves miscelaneas"]:
			miscelaneos_cue(clave, cadena, inventario)
		case "moverse" if "salida" in cadena and condiciones_salida:
			cueva_terminada = True
		case "activar" if "trampas" in cadena:
			control_trampas(inventario)
		case "activar" if "salto" in cadena:
			cueva_terminada = True
		case "terminar" if "programa" in cadena:
			exit(0)
		case _:
			print("Comando no reconocido")


inventario = []

while True:
	if cueva_terminada is False:
		cueva_submarina(inventario)
	elif laberinto_terminado is False:
		laberinto_oculto(inventario)
	else:
		break