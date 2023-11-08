import control_uno as c1
import control_dos as c2
import menu_trampas as t

from sys import exit

def laberinto_oculto(inventario):
    """
    Aqui va el contenido de la segunda habitación del juego
    """

    # Esto muestra la descripción inicial del laberinto
    if not c2.introduccion_laberinto:
        print(c2.inicio_laberinto)
        c2.introduccion_laberinto = True

    # Recoge la acción del jugador
    accion = input("> ")

    # Dividimos la acción en la palabra "clave" y la "cadena" que brinda el 
    # contexto
    try:
        clave, cadena = accion.split(" ", 1)
    except ValueError:
        print("Escribelo bien wey")
        return

    # Cambia la posición del jugador
    if clave == "moverse":
        c2.movimiento(cadena, inventario)

    # Invoca la descripción de los elementos de las habitacion(es)
    elif clave == "inspeccionar":
        c2.inspecciones(cadena, inventario)
    
    elif clave == "recoger":
        c2.recolecciones(cadena, inventario)
    
    elif clave in c2.claves_miscelaneas:
        c2.miscelaneos(cadena, inventario)

    # Termina el programa
    elif clave == "terminar" and cadena == "programa":
        exit(0)

    else:
        print("Comando no reconocido")


def cueva_submarina(inventario):
    """
    Aqui va el contenido de la primera habitación del juego
    """
    global cueva_terminada

    # Esto muestra la descripción inicial de la cueva
    if not c1.introduccion_cueva:
        print(c1.inicio_cueva)
        c1.introduccion_cueva = True

    # Muestra el dialogo que indica el final de la cueva
    if "Mapa de la Isla" in inventario and not c1.mensaje_mostrado:
        print(c1.final_uno)
        c1.mensaje_mostrado = True

    # Recoge la acción del jugador
    accion = input("> ")

    # Dividimos la acción en la palabra "clave" y la "cadena" que brinda el 
    # contexto
    try:
        clave, cadena = accion.split(" ", 1)
    except ValueError:
        print("Escribelo bien wey")
        return

    # Invoca las descripciones de los elementos de la habitación
    if clave == "inspeccionar":
        c1.inspecciones(cadena, inventario)

    # Elimina los objetos del inventario de la habitación y lo añade al del
    # jugador
    elif clave == "recoger":
        c1.recolecciones(cadena, inventario)

    # Revisa si la clave esta en la lista de claves miscelaneas, y si es True,
    # pasa la clave y la cadena para una posterior confirmación
    elif clave in c1.claves_miscelaneas:
        c1.miscelaneos(clave, cadena, inventario)

    # En caso de ser True, permite terminar la seccion de la cueva
    elif clave == "moverse" and "salida":
        if "Mapa de la Isla" in inventario:
            cueva_terminada = True
        else:
            print("¿A donde vas a salir?")

    # Activar menu de trampas
    elif clave == "activar" and "trampas" in cadena:
        t.control_trampas(inventario)
    
    # Termina el programa
    elif clave == "terminar" and "programa" in cadena:
        exit(0)
    
    else:
        print("Comando no reconocido")


# Invenvatario del jugador, inicializado vacio
inventario = []

# Variable que determina el final del juego
juego_terminado = False

# Variables que determinan el final de las habitaciones
cueva_terminada = False
laberinto_terminado = False

# Bucle que hace que continue el juego
while not juego_terminado:
    if not cueva_terminada:
        cueva_submarina(inventario)
    elif not laberinto_terminado:
        laberinto_oculto(inventario)