import control_uno as c1
import control_dos as c2
import menu_trampas as t

from sys import exit

def laberinto_oculto(inventario):
	"""
	Aqui va el contenido de la segunda habitación del juego
	"""
	if not c2.introduccion_laberinto:
		print(c2.l_texto["Inicio laberinto"])
		c2.introduccion_laberinto = True

	accion = input("> ")

	try:
		clave, cadena = accion.split(" ", 1)
	except ValueError:
		print("Un comando tiene que tener al menos dos palabras")
		return

	if clave in c2.claves_misc:
		c2.miscelaneos(clave, cadena, inventario)

	elif clave == "moverse":
		c2.movimiento(cadena, inventario)

	elif clave == "inspeccionar":
		c2.inspecciones(cadena, inventario)
	
	elif clave == "recoger":
		c2.recolecciones(cadena, inventario)
  
	elif clave == "terminar" and cadena == "programa":
		exit(0)

	else:
		print("Comando no reconocido")


def cueva_submarina(inventario):
	"""
	Aqui va el contenido de la primera habitación del juego
	"""
	global cueva_terminada

	if not c1.d_bool["Introduccion cueva"]:
		print(c1.d_texto["Inicio cueva"])
		c1.d_bool["Introduccion cueva"] = True

	if "Mapa de la Isla" in inventario and not c1.d_bool["Mensaje final"]:
		print(c1.d_texto["Final cueva"])
		c1.d_bool["Mensaje final"] = True

	accion = input("> ")

	try:
		clave, cadena = accion.split(" ", 1)
	except ValueError:
		print("Un comando tiene que tener al menos dos palabras")
		return

	if clave == "inspeccionar":
		c1.inspecciones(cadena, inventario)

	elif clave == "recoger":
		c1.recolecciones(cadena, inventario)

	elif clave in c1.d_lista["Claves miscelaneas"]:
		c1.miscelaneos(clave, cadena, inventario)

	elif clave == "moverse" and "salida" in cadena:
		if "Mapa de la Isla" in inventario:
			cueva_terminada = True
		else:
			print("¿A donde vas a salir?")

	elif clave == "activar" and "trampas" in cadena:
		t.control_trampas(inventario)
	
	elif clave == "terminar" and "programa" in cadena:
		exit(0)
	
	else:
		print("Comando no reconocido")


inventario = []

juego_terminado = False

while not juego_terminado:
	if c1.cueva_terminada is False:
		cueva_submarina(inventario)
	elif c2.laberinto_terminado is False:
		laberinto_oculto(inventario)