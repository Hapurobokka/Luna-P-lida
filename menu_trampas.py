from control_uno import d_lista, d_bool, cueva_terminada
from control_dos import objetos_lab

def obtener_input():
    try:
        variable = int(input())
        return variable
    except ValueError:
        print("Solo numeros por favor")
        return

def recibir_objeto(lista_obj, objeto, inventario):
        try:
            lista_obj.remove(objeto)
            inventario.append(objeto)
        except ValueError:
            return print("Objeto no disponible")

def trampas_uno(inventario):
    terminar = False
    print(cueva_terminada)

    print("""
Selecciona una variable para modificar:

Objetos:
    1. Estuatuilla de oro
    2. Trozo de tela
    3. Mapa de la Isla

Eventos:
    4. Animal furioso
    5. Pierna herida

6. Terminar trampas
        """)
    seleccion = obtener_input()

    match seleccion:
        case 1:
            recibir_objeto(d_lista["Objetos cueva"], "Estatuilla de oro", inventario)
        case 2:
            recibir_objeto(d_lista["Objetos cueva"], "Trozo de tela", inventario)
        case 3:
            recibir_objeto(d_lista["Objetos cueva"], "Mapa de la Isla", inventario)
        case 4:
            d_bool["Animal furioso"] = False
        case 5:
            d_bool["Pierna herida"] = False
        case 6:
            terminar = True

    if terminar is False:
        trampas_uno(inventario)
    else:
        return

def trampas_dos(inventario):
    terminar = False
    print("Selecciona una variable para modificar: ")
    print("""
Objetos:
    1. Monoculo raro
    2. Collar con forma de ojo
    3. Llave calavera
    4. Emblema calavera

5. Terminar trampas
        """)

    seleccion = obtener_input()

    match seleccion:
        case 1:
            recibir_objeto(objetos_lab, "Monoculo raro", inventario)
        case 2:
            recibir_objeto(objetos_lab, "Collar con forma de ojo", inventario)
        case 3:
            recibir_objeto(objetos_lab, "Llave calavera", inventario)
        case 4:
            recibir_objeto(objetos_lab, "Emblema calavera", inventario)
        case 5:
            terminar = True
    
    if terminar is False:
        trampas_dos(inventario)
    else:
        return

def control_trampas(inventario):
    print("Elija una habitación que trampear: ")
    print("1. Cueva submarina")
    print("2. Laberinto")

    habitacion = obtener_input()

    if habitacion == 1:
        trampas_uno(inventario)
    elif habitacion == 2:
        trampas_dos(inventario)
    else:
        print("Ingresa un numero valido")

    return
