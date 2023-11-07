import control_inventario as cm
import control_variables as cv

def instancia_uno_descripciones(cadena, inventario):
	"""
	Aquí se imprimen las descripciones de la habitación uno. Le corresponde
	el archivo "descripcion_habitacion1.txt"
	"""
	file = open("descripcion_habitacion1.txt", "r")

	if cadena == "habitacion":
		file.seek(219, 0)	
		for x in range(1, 10):
			print(file.readline(), end="")

	elif cadena == "piedras":
		if not cv.tela_recogida:
			file.seek(644, 0)
			for x in range(0, 4):
				print(file.readline(), end="")	
			cm.sumar_objeto("trozo de tela", inventario)
			cv.tela_recogida = True
		else:
			file.seek(739, 0)
			print("\n")
			print(file.readline())

	elif cadena == "naufragio":
		if not cv.naufragio_explorado:
			file.seek(838, 0)
			for x in range(0, 4):
				print(file.readline(), end="")
		else:
			file.seek(1003, 0)
			print(file.readline())

	elif cadena == "animal":
		if not cv.animal_enfurecido:
			file.seek(1075, 0)	
			for x in range(0, 5):
				print(file.readline(), end="")
		else:
			print("Aqui habra texto")

	else:
		print("Que")


def control_descripcion_p(cadena, inventario, instancia):
	"""
	Función principal del modulo. Obtiene la instancia actual del jugador y 
	dirige el programa a la habitacion correcta.
	"""
	if cadena == "mochila":
		cm.mostrar_inventario(inventario)
	else:
		match instancia:
			case 1:
				instancia_uno_descripciones(cadena, inventario)
			case _:
				print("Que")
