def imprimir_descripcion(file, inicio, cantidad):
    file.seek(inicio)
    for _ in range(cantidad):
        print(file.readline(), end="")

def imprimir_inventario(inventario):
    for objeto in inventario:
        print(" - ", objeto)

def mostrar_alucionaciones():
    file = open("descripcion_dos_2.txt", "r")
    if maldicion_collar is False:
        return

    match posicion:
        case "segunda":
            imprimir_descripcion(file, 4932, 10)
        case "tercera":
            imprimir_descripcion(file, 5151, 8)
        case "centro" if puerta_abierta is True:
            imprimir_descripcion(file, 6702, 3)
        case "centro":
            imprimir_descripcion(file, 5402, 9)
        case "buceando":
            imprimir_descripcion(file, 5698, 9)
        case "meditando":
            imprimir_descripcion(file, 5937, 18)    
        case "leyendo":
            imprimir_descripcion(file, 6481, 5)
        case _:
            print("Si lees esto, ocurrio un error")

    file.close()

def inspecciones_centro(cadena, inventario):
    file = open("descripcion_dos.txt", "r")
    match cadena:
        case "habitacion":
            imprimir_descripcion(file, 23, 18)
        case "inscripcion" | "inscripcion de la puerta":
            imprimir_descripcion(file, 712, 4)
        case "restos" | "restos extraños":
            imprimir_descripcion(file, 904, 12)
        case "mural":
            imprimir_descripcion(file, 1417, 8)
        case "inventario":
            imprimir_inventario(inventario)
        case _:
            print("¿Qué estas mirando?")

    file.close()

def inspecciones_primera(cadena, inventario):
    file = open("descripcion_dos.txt", "r")
    match cadena:
        case "habitacion":
            imprimir_descripcion(file, 1740, 10)
        case "inventario":
            imprimir_inventario(inventario)
        case _:
            print("¿Qué estas mirando?")

    file.close()

def inspecciones_segunda(cadena, inventario):
    file = open("descripcion_dos.txt", "r")
    match cadena:
        case "habitacion":
            imprimir_descripcion(file, 2094, 10)
        case "estatua":
            imprimir_descripcion(file, 2571, 9)
        case "grietas":
            imprimir_descripcion(file, 2971, 15)
        case "luz":
            imprimir_descripcion(file, 3729, 10)
        case "inventario":
            imprimir_inventario(inventario)
        case _:
            print("¿Qué estas mirando?")

    file.close()

def inspecciones_tercera(cadena, inventario):
    file = open("descripcion_dos.txt", "r")
    match cadena:
        case "habitacion":
            imprimir_descripcion(file, 4046, 13)
        case "tapices":
            imprimir_descripcion(file, 4761, 9)
        case "escritorio":
            imprimir_descripcion(file, 5207, 5)
        case "fuente":
            imprimir_descripcion(file, 5453, 11)
        case "inventario":
            imprimir_inventario(inventario)
        case _:
            print("¿Qué estas mirando?")

    file.close()


def descifrar_monoculo(cadena, inventario):
    global posicion

    file = open("descripcion_dos_2.txt", "r")   
    if not ("Monoculo raro" in inventario):
        print("¿Y como vas a hacer eso?")
        return

    match cadena:
        case "inscripcion" if posicion == "centro":
            imprimir_descripcion(file, 880, 8)
        case "papeles" if posicion == "tercera":
            posicion = "leyendo"
            imprimir_descripcion(file, 1122, 10)
            mostrar_alucionaciones()
            posicion = "tercera"
        case _:
            print("¿Qué estas tratando de descifrar?")

    file.close()

def colocar_objetos(cadena, inventario):
    global puerta_abierta
    file = open("descripcion_dos_2.txt", "r")
    file2 = open("descripcion_dos.txt", "r")

    habitaciones_permitidas = ["segunda", "tercera", "centro"]

    if not posicion in habitaciones_permitidas:
        print("¿Qué estas haciendo?")
        return

    permitir_estatuilla = "Estatuilla de oro" in inventario
    permitir_emblema_C = "Emblema calavera" in inventario

    match posicion:
        case "segunda" if "estatuilla" in cadena and permitir_estatuilla:
            imprimir_descripcion(file, 1639, 14)
        case "tercera" if "estatuilla" in cadena and permitir_estatuilla:
            imprimir_descripcion(file, 2316, 15)
        case "centro" if "emblema calavera" in cadena and permitir_emblema_C:
            imprimir_descripcion(file2, 5896, 4)
            inventario.remove("Emblema calavera")
            puerta_abierta = True
        case _:
            print("Ups, algo fallo")

    file.close()
    file2.close()


def apertura_dorado(cadena_b, inventario):
    file = open("descripcion_dos_2.txt", "r")
    if not cadena_b == "dorado":
        print("¿Qué tratas de abrir?")
        return
    elif not "Emblema calavera" in objetos_lab:
        print("Ya tomaste todo lo que habia aqui")
        return
    elif not "Llave calavera" in inventario:
        print("¿Como lo vas a abrir?")
        return

    imprimir_descripcion(file, 768, 5)
    inventario.append("Emblema calavera")
    objetos_lab.remove("Emblema calavera")
    inventario.remove("Llave calavera")

def tablillas(inventario):
    file = open("descripcion_dos_2.txt", "r")
    if not "Llave calavera" in objetos_lab:
        print("Ya tienes la llave, ¿qué mas quieres?")
        return

    comb = input("Introduce la combinación\n>   ")
    if comb == tablilla_comb:
        imprimir_descripcion(file, 576, 6)
        inventario.append("Llave calavera")
        objetos_lab.remove("Llave calavera")
    else:
        print("No paso nada. Tal vez te equivocaste.")

def inspecciones_buceo(cadena_b, inventario):
    file = open("descripcion_dos_2.txt", "r")
    match cadena_b:
        case "coral":
            imprimir_descripcion(file, 3430, 8)
        case "tablilla" | "tablillas":
            imprimir_descripcion(file, 3683, 12)
            tablillas(inventario)
        case "cadaver":
            imprimir_descripcion(file, 3985, 10)
            mostrar_alucionaciones()
        case "dorado":
            imprimir_descripcion(file, 4371, 8)
        case _:
            print("¿Qué estas mirando?")

    file.close()

def recolecciones_buceo(cadena_b, inventario):
    file = open("descripcion_dos_2.txt", "r")
    if cadena_b == "collar":
        imprimir_descripcion(file, 393, 7)
        inventario.append("Collar con forma de ojo")
        objetos_lab.remove("Collar con forma de ojo")
    else:
        print("¿Qué tratas de recoger?")

def bucear(inventario):
    global posicion
    file = open("descripcion_dos_2.txt", "r")
    oxigeno = 3

    imprimir_descripcion(file, 2984, 13)

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
            print("Sales inmediatamente a la superficie.")
            posicion = "primera"
            break

        else:
            print("Comando no reconocido")

        oxigeno = oxigeno - 1

        if oxigeno == 0:
            print("¡Necesitas repirar! Sales inmediatamente a la superficie\n")
            break

    file.close()
    return


def movimiento_lab(cadena, inventario):
    global posicion

    match cadena:
        case "primera":
            posicion = "primera"    
            print(l_texto["Corto buceo"])
        case "segunda":
            posicion = "segunda"
            mostrar_alucionaciones()
            print(l_texto["Corto ruinas"])
        case "tercera":
            posicion = "tercera"
            mostrar_alucionaciones()
            print(l_texto["Corto santuario"])
        case "cuarta":
            print("No implementado")
        case "centro":
            posicion = "centro"
            mostrar_alucionaciones()
            print(l_texto["Corto cristal"]) 
        case _:
            print("¿A donde vas?")

    if "Emblema calavera" in inventario and posicion == "centro":
        print(l_texto["Corto emblema calavera"])


def inspecciones_lab(cadena, inventario):
    match posicion:
        case "centro":
            inspecciones_centro(cadena, inventario)
        case "primera":
            inspecciones_primera(cadena, inventario)
        case "segunda":
            inspecciones_segunda(cadena, inventario)
        case "tercera":
            inspecciones_tercera(cadena, inventario)


def recolecciones_lab(cadena, inventario):
    file = open("descripcion_dos_2.txt", "r")
    if posicion == "centro":
        if "monoculo" in cadena and "Monoculo raro" in objetos_lab:
            imprimir_descripcion(file, 23, 7)
            inventario.append("Monoculo raro")
            objetos_lab.remove("Monoculo raro")
        else:
            print("Eso ya lo recogiste")

    file.close()


def miscelaneos_lab(clave, cadena, inventario):
    file = open("descripcion_dos_2.txt", "r")
    global maldicion_collar, posicion

    match clave:
        case "descifrar":
            descifrar_monoculo(cadena, inventario)
        case "bucear" if posicion == "primera":
            posicion = "buceando"
            bucear(inventario)
        case "entrar" if posicion == "segunda":
            inspecciones_segunda("luz", inventario)
        case "colocar":
            colocar_objetos(cadena, inventario)
        case "ponerse" if cadena == "collar":
            imprimir_descripcion(file, 4628, 6)
            maldicion_collar = True
        case "meditar" if posicion == "tercera":
            posicion = "meditando"
            mostrar_alucionaciones()
            posicion = "tercera"
        case _:
            print("¿Qué tratas de hacer?")

    file.close()


laberinto_terminado = False
maldicion_collar = False

posicion = "centro"

claves_misc = ["bucear", "descifrar", "entrar", "colocar", "ponerse", "meditar"]
objetos_lab = [
    "Monoculo raro",
    "Collar con forma de ojo",
    "Llave calavera",
    "Emblema calavera"
]
tablilla_comb = "hasaf racta"

introduccion_laberinto = False
puerta_abierta = False

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

    "Corto emblema calavera": """
El emblema calavera que cargas contigo brilla ligeramente cuando entras a la
habitación central. Tal vez puedas COLOCARLO en alguna parte.
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
}
