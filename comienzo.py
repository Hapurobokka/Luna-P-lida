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

	if clave in claves_misc:
		miscelaneos_lab(clave, cadena, inventario)

	elif clave == "moverse":
		movimiento_lab(cadena, inventario)

	elif clave == "inspeccionar":
		inspecciones_lab(cadena, inventario)
	
	elif clave == "recoger":
		recolecciones_lab(cadena, inventario)

	elif clave == "activar" and cadena == "trampas":
		control_trampas(inventario)
  
	elif clave == "terminar" and cadena == "programa":
		exit(0)

	else:
		print("Comando no reconocido")


def cueva_submarina(inventario):
	"""
	Aqui va el contenido de la primera habitación del juego
	"""
	global cueva_terminada

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

	if clave == "inspeccionar":
		inspecciones_cue(cadena, inventario)

	elif clave == "recoger":
		recolecciones_cue(cadena, inventario)

	elif clave in d_lista["Claves miscelaneas"]:
		miscelaneos_cue(clave, cadena, inventario)

	elif clave == "moverse" and "salida" in cadena:
		if "Mapa de la Isla" in inventario:
			cueva_terminada = True
		else:
			print("¿A donde vas a salir?")

	elif clave == "activar" and "trampas" in cadena:
		control_trampas(inventario)
	
	elif clave == "terminar" and "programa" in cadena:
		exit(0)
	
	else:
		print("Comando no reconocido")


inventario = []

juego_terminado = False

while not juego_terminado:
	if cueva_terminada is False:
		cueva_submarina(inventario)
	elif laberinto_terminado is False:
		laberinto_oculto(inventario)