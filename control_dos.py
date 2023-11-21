from sys import exit

def movimiento(cadena, inventario):
	global posicion

	if posicion == cadena:
		print("Ya estas ahí tonto")

	elif "primera" in cadena:
		posicion = "primera"
		print(l_texto["Corto buceo"])
	elif "segunda" in cadena:
		posicion = "segunda"
		print(l_texto["Corto ruinas"])
	elif "tercera" in cadena:
		posicion = "tercera"
		print(l_texto["Corto santuario"])
	elif "cuarta" in cadena:
		posicion = "cuarta"
	elif "centro" in cadena:
		posicion = "centro"
		print(l_texto["Corto cristal"])


def inspecciones_centro(cadena, inventario):
	with open("descripcion_dos.txt", "r") as file:
		if "habitacion" in cadena:
			imprimir_descripcion(file, 23, 18)
		elif "inscripcion" in cadena:
			imprimir_descripcion(file, 712, 4)
		elif "restos" in cadena:
			imprimir_descripcion(file, 904, 12)
		elif "mural" in cadena:
			imprimir_descripcion(file, 1417, 8)
		elif "inventario" in cadena:
			imprimir_inventario(inventario)
		else:
			print("¿Qué estas mirando?")

def inspecciones_primera(cadena, inventario):
	with open("descripcion_dos.txt", "r") as file:
		if "habitacion" in cadena:
			imprimir_descripcion(file, 1740, 11)
		elif "inventario" in cadena:
			imprimir_inventario(inventario)
		else:
			print("¿Qué estas mirando?")

def inspecciones_segunda(cadena, inventario):
	with open("descripcion_dos.txt", "r") as file:
		if "habitacion" in cadena:
			imprimir_descripcion(file, 2094, 10)
		elif "estatua" in cadena:
			imprimir_descripcion(file, 2571, 9)	
		elif "grietas" in cadena:
			imprimir_descripcion(file, 2971, 15)
		elif "luz" in cadena:
			imprimir_descripcion(file, 3729, 11)
		elif "inventario" in cadena:
			imprimir_inventario(inventario)

def inspecciones_tercera(cadena, inventario):
	with open("descripcion_dos.txt", "r") as file:
		if "habitacion" in cadena:
			imprimir_descripcion(file, 4046, 13)
		elif "tapices" in cadena:
			imprimir_descripcion(file, 4761, 9)
		elif "fuente" in cadena:
			imprimir_descripcion(file, 5453, 11)
		elif "inventario" in cadena:
			imprimir_inventario(inventario)

def imprimir_descripcion(file, inicio, cantidad):
	file.seek(inicio)
	for _ in range(cantidad):
		print(file.readline(), end="")

def imprimir_inventario(inventario):
	for objeto in inventario:
		print(" - ", objeto)

def inspecciones(cadena, inventario):
		if posicion == "centro":
			inspecciones_centro(cadena, inventario)
		elif posicion == "primera":
			inspecciones_primera(cadena, inventario)
		elif posicion == "segunda":
			inspecciones_segunda(cadena, inventario)
		elif posicion == "tercera":
			inspecciones_tercera(cadena, inventario)


def recolecciones(cadena, inventario):
	if posicion == "centro":
		if "monoculo" in cadena and "Monoculo raro" in objetos_lab:
			print(l_texto["Descripcion monoculo"])
			inventario.append("Monoculo raro")
			objetos_lab.remove("Monoculo raro")
		else:
			print("Eso ya lo recogiste")


def miscelaneos(clave, cadena, inventario):
	if posicion == "centro" and clave == "descifrar":
		if "Monoculo raro" in inventario and "inscripcion" in cadena:
			print(l_texto["Inscripcion puerta"])
		else:
			print("¿Y como vas a hacer eso?")
	elif posicion == "primera" and clave == "bucear":
		bucear(inventario)
	elif posicion == "segunda" and clave == "entrar":
		inspecciones_segunda("luz", inventario)
	elif posicion == "segunda" and clave == "colocar":
		if "estatuilla" in cadena and "Estatuilla de oro" in inventario:
			print(l_texto["Vision estatuilla uno"])
		else:
			print("Parece que el pedestal necesita algo mas.")
	elif posicion == "tercera" and clave == "colocar":
		if "estatuilla" in cadena and "Estatuilla de oro" in inventario:
			print(l_texto["Vision estatuilla dos"])
		else:
			print("Parece que el pedestal necesita algo mas.")
	elif posicion == "tercera" and clave == "descifrar":
		if "Monoculo raro" in inventario and "papeles" in cadena:
			print(l_texto["Texto papeles"])
		else:
			print("¿Y como haras eso?")
	else:
		print("¿Que tratas de hacer?")


def inspecciones_buceo(cadena_b, inventario):
	if cadena_b == "coral":
		print(l_texto["Buceo coral"])
	elif cadena_b == "tablilla" or cadena_b == "tablillas":
		print(l_texto["Buceo tablillas"])
		if "Llave calavera" in objetos_lab:
			tablillas(inventario)
		else:
			print("Ya tienes la llave, ¿qué más quieres?")
	elif cadena_b == "cadaver":
		print(l_texto["Buceo cadaver"])
	elif cadena_b == "dorado":
		print(l_texto["Buceo dorado"])
	else:
		print("¿Qué estas mirando?")

def recolecciones_buceo(cadena_b, inventario):
	if cadena_b == "colgante":
		print(l_texto["Descripcion colgante"])
		inventario.append("Colgante con forma de ojo")
		objetos_lab.remove("Colgante con forma de ojo")
	else:
		print("¿Qué tratas de recoger?")

def apertura_dorado(cadena_b, inventario):
	if cadena_b == "dorado":
		if "Llave calavera" in inventario:
			print(l_texto["Descripcion emblema calavera"])
			inventario.append("Emblema calavera")
			objetos_lab.remove("Emblema calavera")
			inventario.remove("Llave calavera")
		elif not ("Llave calavera" in inventario) and (
			"Emblema calavera" in objetos_lab):
			print("¿Y como lo vas a abrir?")
		else:
			print("Ya tomaste todo lo habia aqui.")

def tablillas(inventario):
	comb = input("Introduce la combinación\n>   ")
	# La combinacion es hasaf racta
	comb1, comb2 = comb.split(" ", 1)

	if comb1 == tab_1 and comb2 == tab_2:
		print(l_texto["Descripcion llave"])
		inventario.append("Llave calavera")
		objetos_lab.remove("Llave calavera")
		return
	else:
		return print("No paso nada. Tal vez te equivocaste.")

def bucear(inventario):
	oxigeno = 3

	print(l_texto["Inicio buceo"])

	while True:
		accion = input("> ")
		try:
			clave_b, cadena_b = accion.split(" ", 1)
		except ValueError:
			print("Un comando tiene que tener al menos dos palabras")
			continue

		if clave_b == "inspeccionar":
			inspecciones_buceo(cadena_b, inventario)

		elif clave_b == "recoger":
			recolecciones_buceo(cadena_b, inventario)

		elif clave_b == "abrir":
			apertura_dorado(cadena_b, inventario)

		elif clave_b == "emerger":
			print("Sales inmediatamente a la superficie")
			break

		oxigeno = oxigeno - 1

		if oxigeno == 0:
			print("¡Necesitas repirar! Sales inmediatamente a la superficie\n.")
			break


laberinto_terminado = False

posicion = "centro"

claves_misc = ["bucear", "descifrar", "entrar", "colocar"]
objetos_lab = [
	"Monoculo raro",
	"Colgante con forma de ojo",
	"Llave calavera",
	"Emblema calavera"
]
tab_1 = "hasaf"
tab_2 = "racta"

introduccion_laberinto = False

l_texto = {
	"Inicio laberinto": """
Caminas a traves de largos y desgastados pasillos de piedra, unicamente
acompañado por la extraña luz azul que emite la estatuilla de oro. Eventualmente
llegas a una gran habitación en la que brilla un cristal azul gigante. 

Su luz es cegadora como la del sol, pero haces lo que puedes por cubrirte los
ojos.

Hay mucho que INSPECCIONAR aqui, asi que deberias comenzar revisando la
HABITACIÓN por completo.
""",

	"Corto cristal": """
El brillo del cristal te sigue esperando en la habitación central.
""",

	"Corto buceo": """
Un estanque azulado te da una tetrica bienvenida.
""",

	"Corto ruinas": """
El silencio sepulcral de unas inmensas ruinas te saluda.
""",

	"Corto santuario": """
El rumor relajante del agua te indica que puedes bajar tu guardia un momento.
	""",

	"Descripcion monoculo": """
Jamas habias tenido algo tan elegante en tus manos. O bueno, no de esta manera.
Te cargaste a un riquillo o dos a lo largo de tus años en altamar, arrancando
de sus lisas y elegantes manos cosas igual de valiosas que estas.

Sin embargo, las circunstancias son diferentes.

Este monoculo puede que marque la diferencia entre la vida y la muerte.
""",

	"Descripcion colgante": """
Jurarias haber visto la forma de ese ojo antes...

¿Por qué subitamente todo esto se te hace tan familiar?

Un poco perturbado, te llevas el collar contigo.
	""",

	"Descripcion llave": """
Una de las tablillas se abre como una pequeña puerta, revelando lo que parece
ser una muy cuidada llave con forma de calavera.

¿Quizás abre algo importante?
	""",

	"Descripcion emblema calavera": """
Un emblema con forma de calavera.

Tal vez sirva para activar un mecanismo importante...
	""",

	"Inscripcion puerta": """
A traves del monoculo raro, puedes descifrar la inscripción de la puerta:

"Para abrir la puerta, debes encontrar el simbolo que representa el equilibrio
de la vida y la muerte."

Ahora tienes una pista de que debes hacer.
	""",

	"Texto papeles": """
A traves del monoculo raro, el texto se vuelve comprensible:

"He fallado. A todas. No fui capaz de encontrarla. Ni siquiera las paredes de
este divino lugar pueden aliviar el peso que ahora se asienta en mi corazón.
La magia de este lugar, siento que me esta llamando. En algún momento vendra
por mi. Si alguien llega a encontrar mi cuerpo o este escrito, por favor
vayase de aqui, porque ni siquiera yo, que me considero una experta en el
HASAF RACTA, se que terminara pasando conmigo."
	""",

	"Vision estatuilla uno": """
La tormenta lo esta devorando todo. Sus poderosos vientos arrancan las casas
desde sus cimientos como si fueran hojas de arboles que salen volando ante la
menor brisa. Tus hermanas siguen exigiendote que las acompañes para buscar un
refugio, pero incluso en una situación de desastre, no puede abandonar tu
oficio. 

Como suma sacerdotisa del HASAF, tienes que velar por la seguridad de madre, y
es por eso que incluso con el huracan debes encontrarla. Te diriges al interior
del gran templo, y entonces...

Despiertas despues de ese potente trance. ¿Qué fue eso? Sin embargo, se sintio
demasiado cercano. Demasiado real... Recoges la estatuilla.
	""",

	"Vision estatuilla dos": """
La pequeña corona hecha de conchas marinas es colocada ceremonialmente en tu
cabeza por la antigua suma sacerdotisa de la aldea. Por el ritual de la RACTA
ahora tu seras su sucesora. Te arrodillas ante ella, y comienzas a recitar las
palabras que desde tu niñez tienes grabadas a fuego en tu memoria. 

Hoy te conviertes en la mujer mas importante de la aldea, con excepción de
Madre, y ahora tienes que cuidar a todas tus hermanas como tu destino siempre
te ha indicado.

¿Pero estas satisfecha con eso?

Despiertas despues de ese potente trance. ¿Qué fue eso? Sin embargo, se sintio
demasiado cercano. Demasiado real... Recoges la estatuilla.
	""",

	"Inicio buceo": """
El agua es extremadamente fria al tacto, y resulta que si es mucho mas profunda
de lo que esperabas. 

Un extraño CORAL azulado ilumina la fosa, lo suficiente como para que puedas
dislumbrar

Una extraño par de TABLILLAS reposa en el fondo, junto con lo que parece ser
otro CADAVER (¿por qué hay tantos?).

Y finalmente, algo DORADO resplandece en la pared de la izquierda. Se ve que
esta incrustado ahí. ¿Qué podría ser?
""",

	"Buceo coral": """
El coral brilla con la misma intensidad que el gran cristal de la habitación
central. Ese azul hipnotico, mistico, magico.

Recuerdas a tu capitan sujetando un pedazo de roca similar al coral. 

¿Acaso el sabia algo de este lugar?
	""",

	"Buceo tablillas": """
Dos tablillas de piedra descansan hasta el fondo de la fosa.

H B W S F   I R A M S
F A O S M   M S L A S
S F W N M   C F W S E
D A M L C   N W E T N
C O I F N   L X A B Z

Parece que puedes pulsar algunos de los simbolos, uno por cada fila.
Podrias intentar escribir algo con ellas.
	""",

	"Buceo cadaver": """
Otro cadaver de una mujer, esta vez esta viscoso y cubierto de algas.
Los trozos de tela adheridos a sus huesos ya no pueden ser considerados
ropa, y faltan muchos huesos de su torax y parte inferior.

Sin embargo, posee un objeto que no ha decaido como los demas. Un COLGANTE
con forma de ojo refleja la luz del coral.

Tal vez sea otro artefacto que deberias RECOGER.
	""",

	"Buceo dorado": """
Una placa dorada esta incrustada en la pared de la fosa. Sus hermosos relieves
hechos en oro no parecen haber envejecido un solo día.

Notas una pequeña ranura para insertar algo en ella. ¿Quizás una llave?

Tal vez se pueda ABRIR.
	"""
}