from sys import exit

def imprimir_descripcion(file, inicio, cantidad):
    file.seek(inicio)
    for _ in range(cantidad):
        print(file.readline(), end="")

def imprimir_inventario(inventario):
    for objeto in inventario:
        print(f" - {objeto}")

def inspecciones(cadena, inventario):
    with open("descripcion_uno.txt", "r") as file:
        if cadena == "cueva":
            imprimir_descripcion(file, 21, 16)

        elif cadena == "balsa":
            imprimir_descripcion(file, 625, 8)

        elif cadena == "esqueleto":
            imprimir_descripcion(file, 1022, 10)

        elif cadena == "animal":
            imprimir_descripcion(file, 1441, 7)

        elif cadena == "inventario":
            imprimir_inventario(inventario)

        else:
            print("Comando no reconocido")

        
def recolecciones(cadena, inventario):
    if cadena == "estatuilla":
        if "Estatuilla de oro" in d_lista["Objetos cueva"]:
            print(d_texto["Texto estatuilla"])
            inventario.append("Estatuilla de oro")
            d_lista["Objetos cueva"].remove("Estatuilla de oro")
        else:
            print("\nYa recogiste la estatuilla, merluzo\n")

    elif cadena == "tela" or cadena == "trozo de tela":
        if "Trozo de tela" in d_lista["Objetos cueva"]:
            print(d_texto["Texto tela"])
            inventario.append("Trozo de tela")
            d_lista["Objetos cueva"].remove("Trozo de tela")
        else:
            print("\nHay que tener respeto por los muertos.\n")          

    elif cadena == "papel" or cadena == "pedazo de papel":
        if d_bool["Animal furioso"]:
            print(d_texto["Texto furia"])
        elif not d_bool["Animal furioso"] and "Mapa de la Isla" in d_lista[
            "Objetos cueva"]:
            print(d_texto["Texto papel"])
            inventario.append("Mapa de la Isla")
            d_lista["Objetos cueva"].remove("Mapa de la Isla")
        else:
            print("\nNo hay nada que tomar\n")

    else:
        print("Comando no reconocido")


def miscelaneos(clave, cadena, inventario):
    requisitos_mapa = d_bool["Animal furioso"] and not d_bool["Pierna herida"] 

    if clave == "vendar" and "pierna" in cadena:
        if "Trozo de tela" in inventario and d_bool["Pierna herida"]:
            print(d_texto["Texto pierna"])
            d_bool["Pierna herida"]= False
            inventario.remove("Trozo de tela")
        elif not "Trozo de tela" in inventario and not d_bool["Pierna herida"]:
            print("Ya hiciste eso")
        else:
            print("No creo que aún puedas hacer eso.")

    elif clave == "asustar" and "animal" in cadena:
        if "Estatuilla de oro" in inventario and requisitos_mapa:
            print(d_texto["Texto asustar"])
            d_bool["Animal furioso"] = False
        elif "Estatuilla de oro" in inventario and not requisitos_mapa: 
            print(d_texto["Muerte animal herida"])
            exit(0)
        elif not "Estatuilla de oro" in inventario and not requisitos_mapa:
            print(d_texto["Muerte animal estatuilla"])
            exit(0)
        else:
            print("¿A quien estas asustando?")

    else:
        print("Comando no reconocido")


d_lista = {
    "Claves miscelaneas": ["vendar", "asustar"],
    "Objetos cueva": [
        "Estatuilla de oro", 
        "Trozo de tela", 
        "Mapa de la Isla"]
}

d_bool = {
    "Introduccion cueva": False,
    "Mensaje final": False,

    "Animal furioso": True,
    "Pierna herida": True,
}

d_texto = {
    "Texto estatuilla": """
El frio metal dorado de la estatua te provoca un profundo escalofrio.
Sin embargo, su lujurioso cuerpo de alguna manera te mantiene en un
trance que no puedes definir. En contra de tu sentido común, decides
llevarla contigo.
    """,
    
    "Texto tela": """
Esta manga de la camisa que vestia el esqueleto tendra un nuevo uso. Cuando la
arrancaste, lo hiciste con el mayor respeto que se puede tener por un camarada
caido.

...tu capitan se habria reido de ti.
""",

    "Texto papel": """
¡Quien lo diria! El papel era un mapa. Un mapa que no reconoces, pero que
jurarias que le pertenecio a tu capitan en algún momento. ¿Cómo es que esto
ha sobrevivido?

Sin embargo, su contenido te intriga. Apunta a una tal 'Isla de las Perdidas'.

Un escalofrio recorre tu espalda, ¿acaso terminaste ahí?
""",

    "Inicio cueva": """
Estas atrapado en una cueva.
Tienes la pierna lastimada y esta sangrando mucho
no crees poder moverte mucho.
Sera mejor que te pongas a INSPECCIONAR la CUEVA.
    """,

    "Texto pierna": """
Con cuidado usas la manga para vendar el corte que tienes en la pierna. No
ayuda mucho con el dolor, pero al menos así dejaras de perder tanta sangre.
omienzas a pensar que vas a sobrevivir.
    """,

    "Texto furia": """
Deberias haber sospechado que la mirada del animal significaba peligro. En el
momento en el que te acercas un poco a el, intenta arañarte con las garras
que no habias visto que tenia.

Tal vez tengas algo contigo que puedas usar para asustarlo...
    """,

    "Texto asustar": """
La estatuilla brilla extrañamente en tus manos. 

Se siente... calida, casi familiar. 
¿Has visto a esta mujer antes, no es verdad?

¿Acaso no puedes recordarla..?

El animal chilla y salta, tratando de arrancarte el brazo con el que
sostienes la estatuilla, pero gracias a que te vendaste la pierna, reaccionas
a tiempo, y logras darle una patada. 

Suelta el PEDAZO DE PAPEL, y sale corriendo despavorido.

La estatuilla deja de brillar.
    """,

    "Muerte animal herida": """
En el momento en el que el animal dislumbra tus intenciones, salta para
atacarte. Por desgracia, tu pierna lastimada te juega una mala pasada, 
provocando que te resbales y caigas contra el suelo.

El animal devora tus entrañas.
    """,

    "Muerte animal estatuilla": """
¿Con que estas intentando asustar al animal? El tiene filosas garras con las
que te acaba de abrir el estomago. 

El animal devora tus entrañas.
    """,

    "Final cueva": """
¡Eso es! El mapa indica una salida de esta cueva, o algo asi. No sabes como
lo comprendes, pero es una esperanza mejor que cualquier otra. Deberias ser
capaz de MOVERTE a la SALIDA de la CUEVA.
    """
}