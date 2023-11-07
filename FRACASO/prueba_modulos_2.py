import prototipo_inventario
from sys import exit

def control_acciones(inventario):

	objetos = 0

	while True:
		print("¿Qué es lo que vas a hacer?")
		print("Pista: Usa las palabras 'añadir', 'remover' o 'terminar'")

		accion = input("> ")

		clave, argumento = accion.split(" ", 1)

		if clave == "añadir":
			prototipo_inventario.sumar_objeto(argumento, inventario)
			objetos += 1

		elif clave == "remover":
			prototipo_inventario.remover_objeto(argumento, inventario)
			objetos -= 1

		elif clave == "mostrar" and argumento == "mochila":
			prototipo_inventario.mostrar_inventario(inventario)

		elif clave == "terminar" and argumento == "programa":
			if objetos > 5:
				print("¡Llevas demasiados objetos!")
				continue
			else:
				exit(0)


print("Estas organizando tu mochila para salir de excursion")
print("Puedes llevar un maximo de 5 objetos")
print("¿Qué vas a hacer?")

inventario = []

control_acciones(inventario)