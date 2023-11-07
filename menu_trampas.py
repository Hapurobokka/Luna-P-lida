import comienzo as c0
import control_uno as c1

def control_trampas():
    final = False

    while not final:
        
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

        seleccion = int(input("> "))

        match seleccion:
            case 1:
                c0.inventario.append("Estatuilla de oro")
                c1.objetos_cueva.remove("Estatuilla de oro")
            case 2:
                c0.inventario.append("Trozo de tela")
                c1.objetos_cueva.remove("Trozo de tela")
            case 3:
                c0.inventario.append("Mapa de la Isla")
                c1.objetos_cueva.remove("Mapa de la Isla")
            case 4:
                c1.animal_furioso = False
            case 5:
                c1.pierna_herida = False
            case 6:
                c0.cueva_terminada = True
            case 7:
                final = True