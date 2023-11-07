import prototipo_inventario
from sys import exit

def control_acciones(inventario):

	objetos = 0

	while True:
		print("¿Qué es lo que vas a hacer?")
		print("Pista: Usa las palabras 'añadir', 'remover', o 'terminar'")

		accion = input("> ")
	
		if "añadir" in accion:
			prototipo_inventario.sumar_objeto(inventario)
			objetos += 1
		elif "remover" in accion:
			prototipo_inventario.remover_objeto(inventario)
		elif "ver" and "mochila" in accion:
			prototipo_inventario.mostrar_inventario(inventario)
		elif "terminar" in accion:
			if objetos > 5:
				print("¡Llevas demasiados objetos!")
				continue
			else:
				print("Ya esta todo listo, ¡a trabajar!")
				exit(0)
		else:
			print("No entendi, ¿puedes repetirlo?")

print("Estas organizando tu mochila para salir de excursion")
print("Puedes llevar un maximo de 5 objetos")
print("¿Qué vas a hacer?")

inventario = []

control_acciones(inventario)