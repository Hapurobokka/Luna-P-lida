import control_descripciones as cd
import control_inventario as cm
import control_interacciones as ci

def control_principal(accion, inventario, instancia):
	"""
	Esta funcion redirige la accion del jugador a nuestros tres modulos de
	interacción principales: el modulo de inventario, el modulo de 
	descripciones y el modulo de interacciones.
	"""

	# En caso de que el jugador introduzca una unica palabra, manejamos
	# la excepcion para evitar que el programa se detenga.
	try:
		clave, cadena = accion.split(" ", 1)
	except ValueError:
		return print("Intenta escribir al menos dos palabras")

	if clave == "inspeccionar":
		cd.control_descripcion_p(cadena, inventario, instancia)	

	elif clave == "inventario":
		try: 
			interaccion, objeto = cadena.split()
		except ValueError:
			return print("Intenta escribirlo de esta manera: inventario interaccion objeto")
		else:
			cm.control_inventario_p(interaccion, objeto, inventario)	

	elif clave == "usar":
		try:
			objeto, lugar = cadena.split()
		except ValueError:
			return print("Intenta escribirlo de esta manera: usar objeto lugar")
		else:
			ci.control_interaccion_p(objeto, lugar, inventario)

	elif clave == "terminar" and cadena == "programa":
		global final 
		final = True

	else:
		print("Comando no reconocido")


inventario = []
instancia = 1
final = False


while not final:
	accion = input("> ")
	control_principal(accion, inventario, instancia)
else:
	print("El programa termino correctamente")
