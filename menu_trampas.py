import control_uno as c1
import control_dos as c2

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

		seleccion = int(input())

		if seleccion == 1:
			inventario.append("Estatuilla de oro")
			c1.d_lista["Objetos cueva"].remove("Estatuilla de oro")
		elif seleccion == 2:
			inventario.append("Trozo de tela")
			c1.d_lista["Objetos cueva"].remove("Trozo de tela")
		elif seleccion == 3:
			inventario.append("Mapa de la Isla")
			c1.d_lista["Objetos cueva"].remove("Mapa de la Isla")
		elif seleccion == 4:
			c1.d_bool["Animal furioso"] = False
		elif seleccion == 5:
			c1.d_bool["Pierna herida"] = False
		elif seleccion == 6:
			c1.cueva_terminada = True
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

		seleccion = int(input())

		if seleccion == 1:
			inventario.append("Monoculo raro")
			c2.objetos_lab.remove("Monoculo raro")
		elif seleccion == 2:
			inventario.append("Colgante con forma de ojo")
			c2.objetos_lab.remove("Colgante con forma de ojo")
		elif seleccion == 3:
			inventario.append("Llave calavera")
			c2.objetos_lab.append("Llave calavera")
		elif seleccion == 4:
			inventario.append("Emblema calavera")
			c2.objetos_lab.remove("Emblema calavera")
		elif seleccion == 5:
			break

	return

def control_trampas(inventario):
	print("Elija una habitación que trampear: ")
	print("1. Cueva submarina")
	print("2. Laberinto")
	habitacion = int(input())
	if habitacion == 1:
		trampas_uno(inventario)
	elif habitacion == 2:
		trampas_dos(inventario)

	return