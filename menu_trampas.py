import control_uno as c1

def control_trampas(inventario):
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

        if seleccion == 1:
            inventario.append("Estatuilla de oro")
            c1.d_lista["Objetos cueva"].remove("Estatuilla de oro")
        elif seleccion == 2:
            inventario.append("Trozo de tela")
            c1.d_lista["Objetos cueva"].remove("Trozo de tela")
        elif seleccion == 3:
            inventario.append("Mapa de la Isla")
            c1.d_lista["Objetos cueva"].remove("Mapa de la Isla")
        elif seleccion == 4:
            c1.d_bool["Animal furioso"] = False
        elif seleccion == 5:
            c1.d_bool["Pierna herida"] = False
        elif seleccion == 6:
            c1.cueva_terminada = True
        elif seleccion == 7:
            final = True