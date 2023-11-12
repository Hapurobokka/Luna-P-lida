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
    elif "tercera" in cadena:
        posicion = "tercera"
    elif "cuarta" in cadena:
        posicion = "cuarta"
    elif "centro" in cadena:
        posicion = "centro"
        print(l_texto["Corto cristal"])


def inspecciones(cadena, inventario):

    file = open("descripcion_dos.txt", "r")

    match posicion:
        case "centro":
            if "habitacion" in cadena:
                file.seek(23)
                for _ in range(0, 21):
                    print(file.readline(), end="") 
            elif "restos" in cadena:
                file.seek(860)
                for _ in range(0, 12):
                    print(file.readline(), end="")
            elif "mural" in cadena:
                file.seek(1339)
                for _ in range(0, 11):
                    print(file.readline(), end="")
            else:
                print("¿Qué estas mirando?")

        case "primera":
            if "habitacion" in cadena:
                file.seek(853)
                for _ in range(0, 10):
                    print(file.readline(), end="")
            else:
                print("¿Qué estas mirando?")

    file.close()


def recolecciones(cadena, inventario):

    match posicion:
        case "centro":
            if "monoculo" in cadena and "Monoculo raro" in l_listas[
            "Objetos laberinto"]:
                print(l_texto["Descripcion monoculo"])
                inventario.append("Monoculo raro")
                l_listas["Objetos laberinto"].remove("Monoculo raro")
            else:
                print("Eso ya lo recogiste")


def miscelaneos(clave, cadena, inventario):

    match posicion:
        case "primera":
            if clave == "bucear":
                bucear(inventario)


def bucear(inventario):

    oxigeno = 3
    llave_encontrada = False
    tesoro_obtenido = False

    print(l_texto["Inicio buceo"])

    while True:
        accion = input("> ")

        if accion == "inspeccionar coral":
            print(l_texto["Buceo coral"])
        elif accion == "inspeccionar tablilla":
            print(l_texto["Buceo tablillas"])
            tablillas()
        elif accion == "inspeccionar cadaver":
            print(l_texto["Buceo cadaver"])
        elif accion == "inspeccionar dorado":
            print(l_texto["Buceo dorado"])
        elif accion == "emerger":
            print("Sales inmediatamente a la superficie")
            break

        elif accion == "recoger colgante":
            print(l_texto["Descripcion colgante"])
            inventario.append("Colgante con forma de ojo")
            l_listas["Objetos laberinto"].remove("Colgante con forma de ojo")

        else:
            print("No deberias gastar tu aire en cosas que no estan aqui")

        oxigeno = oxigeno - 1

        if oxigeno == 0:
            print("¡Necesitas repirar! Sales inmediatamente a la superficie.")
            break

def tablillas():
    comb = input("Introduce la combinación\n>   ")
    print(comb)
    print("Esto es todo lo que hace esta función xd")


posicion = "centro"

l_listas = {
    "Claves miscelaneas": ["bucear"],
    "Objetos laberinto": [
                        "Monoculo raro",
                        "Colgante con forma de ojo"
                        ]
}

l_bool = {
    "Introduccion laberinto": False
}

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

A B W S F   I S A M S
F S O S M   M S L W S
S F W S M   K F W S I
D K M L C   N W E A N
C O I F N   L X C B Z

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
    """
}
