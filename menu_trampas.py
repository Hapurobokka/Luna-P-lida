from control_uno import d_lista, d_bool, cueva_terminada
from control_dos import objetos_lab

def obtener_input():
	try:
		variable = int(input())
		return variable
	except ValueError:
		print("Solo numeros por favor")
		return


def trampas_uno(inventario):
	while True:	
		print("Selecciona una variable para modificar: ")
		print("Objetos:\n")
		print("\t1. Estuatuilla recogida")
		print("\t2. Tela recogida")
		print("\t3. Papel recogido")
		print("Eventos:\n")
		print("\t4. Animal furioso")
		print("\t5. Pierna herida")
		print("6. Pasar al laberinto")
		print("7. Terminar trampas")

		seleccion = obtener_input()

		if seleccion == 1:
			inventario.append("Estatuilla de oro")
			d_lista["Objetos cueva"].remove("Estatuilla de oro")
		elif seleccion == 2:
			inventario.append("Trozo de tela")
			d_lista["Objetos cueva"].remove("Trozo de tela")
		elif seleccion == 3:
			inventario.append("Mapa de la Isla")
			d_lista["Objetos cueva"].remove("Mapa de la Isla")
		elif seleccion == 4:
			d_bool["Animal furioso"] = False
		elif seleccion == 5:
			d_bool["Pierna herida"] = False
		elif seleccion == 6:
			cueva_terminada = True
		elif seleccion == 7:
			break

	return

def trampas_dos(inventario):
	while True:
		print("Selecciona una variable para modificar: ")
		print("""
Objetos:
	1. Monoculo raro
	2. Colgante con forma de ojo
	3. Llave calavera
	4. Emblema calavera

5. Terminar trampas
			""")

		seleccion = obtener_input()

		if seleccion == 1:
			inventario.append("Monoculo raro")
			objetos_lab.remove("Monoculo raro")
		elif seleccion == 2:
			inventario.append("Colgante con forma de ojo")
			objetos_lab.remove("Colgante con forma de ojo")
		elif seleccion == 3:
			inventario.append("Llave calavera")
			objetos_lab.append("Llave calavera")
		elif seleccion == 4:
			inventario.append("Emblema calavera")
			objetos_lab.remove("Emblema calavera")
		elif seleccion == 5:
			break

	return

def control_trampas(inventario):
	print("Elija una habitación que trampear: ")
	print("1. Cueva submarina")
	print("2. Laberinto")

	habitacion = obtener_input()

	if habitacion == 1:
		trampas_uno(inventario)
	elif habitacion == 2:
		trampas_dos(inventario)
	else:
		print("Ingresa un numero valido")

	return