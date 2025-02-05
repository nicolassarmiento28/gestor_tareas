# LISTA TAREAS
tareas = [] # SE DEJA VACIA PARA QUE EL USUARIO LA LLENE CON TAREAS

def agregar_tarea(lista): # dentro del parentesis esta el parametro que se le va a pasar
    #ENTRADA PARA LA TAREA
    tarea = input("introduzca la descripcion de la tarea: ")

    # ANADIR LA TAREA A LA LISTA
    lista.append(tarea)

    #INFORME DE TAREA ANADIDA
    print("La tarea fue anadida correctamente")

    # INFORMAR CUAL FUE LA TAREA ANADIDA
    print(f"La tarea ingresada es : {tarea}. ")

    # INFORMAR EL NUMERO DE LA TAREA ANADIDA
    print(f"la tarea fue ingresada en la posicion : {len(lista)}") # len nos dice la longitud de la lista en este caso

def ver_tareas(lista):
    # CONDICIONAL QUE EVALUA SI HAY ALGO EN LA LISTA

    # SI HAY ALGO EN LA LISTA SE PRESENTA
    if lista:
        for indice, tarea in enumerate(lista):
            print(f"{indice + 1}. {tarea}")

    # SI LA LISTA ESTA VACIA AVISA DE ELLO
    else:
        print(" La lista esta vacía")

    # MENSAJE FIN DE LISTADO
    print("--FIN DEL LISTADO DE TAREAS--")

def tarea_completada(lista):
    #LLAMAMOS A LA FUNCION ver_tareas
    ver_tareas(lista)

    #ENTRADA DE USUARIO PARA INTRODUCIR UNA TAREA
    completada = int(input("Introduzca la tarea completada: "))

    # CONDICIONAL PARA EVUALUAR LA TAREA COMO COMPLETADA
    if completada > 0 and completada <= len(lista):
    # CONDICIONAL PARA EVALUAR SI LA TAREA YA ESTABA COMPLETADA
        if "(Completada)" in lista[completada - 1]:
            print("La tarea ya estaba marcada como completada")
    #   SI NO ESTA COMPLETADA
        else:
            lista[completada - 1] = "(Completada)" + lista[completada - 1]
            print("Se marco la tarea como completada")

    else:
        print(" La opción es imvalida")

        
def eliminar_tarea(lista):
    # SI LA LISTA CONTIENE ALGO
    if lista:
        ver_tareas(lista)

        tarea = int(input("Introduzca el numero de tarea a eliminar : "))

        # OPCION INVALIDA SI LA TAREA NO ESTA DENTRO DEL RANGO DE LA LISTA
        if tarea <= 0 or tarea > len(lista):
            print("Opcion invalida")
        
        else:
            del lista[tarea - 1]
            print("La tarea ha sido eliminada")
    
    # SI LA LISTA ESTA VACIA
    else:
        print("No hay tareas")




