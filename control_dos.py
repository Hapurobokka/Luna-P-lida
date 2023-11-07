from sys import exit

def movimiento(cadena, inventario):

    global posicion

    if posicion == cadena:
        print("Ya estas ahí tonto")

    elif "primera" in cadena:
        posicion = "primera"
    elif "segunda" in cadena:
        posicion = "segunda"
    elif "tercera" in cadena:
        posicion = "tercera"
    elif "cuarta" in cadena:
        posicion = "cuarta"
    elif "centro" in cadena:
        posicion = "centro"

def inspecciones(cadena, inventario):

    file = open("descripcion_dos.txt", "r")

    match cadena:
        case "habitacion":
            if posicion == "centro":
                file.seek(23)
                for x in range(0, 12):
                    print(file.readline(), end="")
            else:
                print("Esa habitacion aun no existe jaja")

    file.close()


def recolecciones(cadena, inventario):
    pass


def miscelaneos(cadena, inventario):
    pass

posicion = "centro"

introduccion_laberinto = False

inicio_laberinto = """
Caminas a traves de largos y desgastados pasillos de piedra, unicamente
acompañado por la extraña luz azul que emite la estatuilla de oro. Eventualmente
llegas a una gran habitación en la que brilla un cristal azul gigante. 

Su luz es cegadora como la del sol, pero haces lo que puedes por cubrirte los
ojos.

Hay mucho que INSPECCIONAR aqui, asi que deberias comenzar revisando la
HABITACIÓN por completo.
"""