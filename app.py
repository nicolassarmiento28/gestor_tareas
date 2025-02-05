# IMPORTAMOS LAS FUNCIONES AL ARCHIVO APP

import funciones
# BUCLE INFINITO PARA QUE SE EJECUTE EL MENU DE  -PCIONES SIEMPRE HAY QUE DECIDAMOS SALIR
while True:

#MENU DE OPCIONESS
    print("\n ---- BIENVENIDO AL GESTOR DE TAREAS POR CONSOLA ---- \n ")
    print("1. Añadir tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

  



    opcion = input("Introduzca una opcion:")
    

# MENU DE OPCIONES 2
    if opcion == "1":
        funciones.agregar_tarea(funciones.tareas)
        

    elif opcion == "2":
        funciones.ver_tareas(funciones.tareas)
        
    
    elif opcion == "3":
        funciones.tarea_completada(funciones.tareas)
        

    elif opcion == "4":
        funciones.eliminar_tarea(funciones.tareas)
        

    elif opcion == "5":
        print("Gracias por utilizar el gestor de tareas, nos vemos pronto")
        break

    else:
        print( "Opcion no valida, intente nuevamente con una opción del 1 al 5.")


