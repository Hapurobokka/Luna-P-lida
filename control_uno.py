from sys import exit

def inspecciones(cadena, inventario):

    file = open("descripcion_uno.txt", "r")

    match cadena:
        case "cueva":
            file.seek(21, 0)
            for x in range(0, 16):
                print(file.readline(), end="")

        case "balsa":
            file.seek(625, 0)
            for x in range(0, 8):
                print(file.readline(), end="")

        case "esqueleto":
            file.seek(1022, 0)
            for x in range(0, 10):
                print(file.readline(), end="")

        case "animal":
            file.seek(1441, 0)
            for x in range(0, 7):
                print(file.readline(), end="")

        case "inventario":
            print("\nTienes en tu inventario:")
            for x in inventario:
                print("-", x)
            print("\n")

        case _:
            print("Comando no reconocido")
        
    file.close()


def recolecciones(cadena, inventario):

    match cadena:
        case "estatuilla":
            if "Estatuilla de oro" in objetos_cueva:
                print(texto_estatuilla)
                inventario.append("Estatuilla de oro")
                objetos_cueva.remove("Estatuilla de oro")
            else:
                print("\nYa recogiste la estatuilla, merluzo\n")

        case "tela" |  "trozo de tela":
            if "Trozo de tela" in objetos_cueva:
                print(texto_tela)
                inventario.append("Trozo de tela")
                objetos_cueva.remove("Trozo de tela")
            else:
                print("\nHay que tener respeto por los muertos.\n")          

        case "papel" |  "pedazo de papel":
            if animal_furioso:
                print(texto_furia)
            elif not animal_furioso and "Mapa de la Isla" in objetos_cueva:
                print(texto_papel)
                inventario.append("Mapa de la Isla")
                objetos_cueva.remove("Mapa de la Isla")
            else:
                print("\nNo hay nada que tomar\n")

        case _:
            print("Comando no reconocido")


def miscelaneos(clave, cadena, inventario):

    global animal_furioso, pierna_herida

    requisitos_mapa = animal_furioso and not pierna_herida

    if clave == "vendar" and "pierna" in cadena:
        if "Trozo de tela" in inventario and pierna_herida:
            print(texto_pierna)
            pierna_herida = False
            inventario.remove("Trozo de tela")
        elif not "Trozo de tela" in inventario and not pierna_herida:
            print("Ya hiciste eso")
        else:
            print("No creo que aún puedas hacer eso.")

    elif clave == "asustar" and "animal" in cadena:
        if "Estatuilla de oro" in inventario and requisitos_mapa:
            print(texto_asustar)
            animal_furioso = False
        elif not "Estatuilla de oro" in inventario and requisitos_mapa: 
            print(muerte_animal2)
            exit(0)
        elif not "Estatuilla de oro" in inventario and not requisitos_mapa:
            print(muerte_animal)
            exit(0)
        else:
            print("¿A quien estas asustando?")

    else:
        print("Comando no reconocido")


# Lista de claves miscelaneas
claves_miscelaneas = ["vendar", "asustar"]

# Objetos
objetos_cueva = ["Estatuilla de oro", "Trozo de tela", "Mapa de la Isla"]

# Eventos
introduccion_cueva = False
mensaje_mostrado = False

animal_furioso = True 
pierna_herida = True

# Descripcion de objetos
texto_estatuilla = """
El frio metal dorado de la estatua te provoca un profundo escalofrio.
Sin embargo, su lujurioso cuerpo de alguna manera te mantiene en un
trance que no puedes definir. En contra de tu sentido común, decides
llevarla contigo.
"""

texto_tela = """
Esta manga de la camisa que vestia el esqueleto tendra un nuevo uso. Cuando la
arrancaste, lo hiciste con el mayor respeto que se puede tener por un camarada
caido.

...tu capitan se habria reido de ti.
"""

texto_papel = """
¡Quien lo diria! El papel era un mapa. Un mapa que no reconoces, pero que
jurarias que le pertenecio a tu capitan en algún momento. ¿Cómo es que esto
ha sobrevivido?

Sin embargo, su contenido te intriga. Apunta a una tal 'Isla de las Perdidas'.

Un escalofrio recorre tu espalda, ¿acaso terminaste ahí?
"""

# Descripciones de eventos
inicio_cueva = """
Estas atrapado en una cueva.
Tienes la pierna lastimada y esta sangrando mucho
no crees poder moverte mucho.
Sera mejor que te pongas a INSPECCIONAR la CUEVA.
"""

texto_pierna = """
Con cuidado usas la manga para vendar el corte que tienes en la pierna. No
ayuda mucho con el dolor, pero al menos así dejaras de perder tanta sangre.
Comienzas a pensar que vas a sobrevivir.
"""

texto_furia = """
Deberias haber sospechado que la mirada del animal significaba peligro. En el
momento en el que te acercas un poco a el, intenta arañarte con las garras
que no habias visto que tenia.

Tal vez tengas algo contigo que puedas usar para asustarlo...
"""

texto_asustar = """
La estatuilla brilla extrañamente en tus manos. 

Se siente... calida, casi familiar. 
¿Has visto a esta mujer antes, no es verdad?

¿Acaso no puedes recordarla..?

El animal chilla y salta, tratando de arrancarte el brazo con el que
sostienes la estatuilla, pero gracias a que te vendaste la pierna, reaccionas
a tiempo, y logras darle una patada. 

Suelta el PEDAZO DE PAPEL, y sale corriendo despavorido.

La estatuilla deja de brillar.
"""

muerte_animal = """
En el momento en el que el animal dislumbra tus intenciones, salta para
atacarte. Por desgracia, tu pierna lastimada te juega una mala pasada, 
provocando que te resbales y caigas contra el suelo.

El animal devora tus entrañas.
"""

muerte_animal2 = """
¿Con que estas intentando asustar al animal? El tiene filosas garras con las
que te acaba de abrir el estomago. 

El animal devora tus entrañas.
"""

final_uno = """
¡Eso es! El mapa indica una salida de esta cueva, o algo asi. No sabes como
lo comprendes, pero es una esperanza mejor que cualquier otra. Deberias ser
capaz de MOVERTE a la SALIDA de la CUEVA.
"""

