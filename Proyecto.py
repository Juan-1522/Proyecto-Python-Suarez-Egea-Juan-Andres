import json
from funciones import *
while True:
    print("\n====================================================\n")
    print("   GENERADOR DE HORARIO PARA LOS ESTUDIANTES v.1.0   ")
    print("\n====================================================\n")
    print("1. Registrar una materia o actividad")
    print("2. Ver horario actual")
    print("3. Modificar el horario o actividad")
    print("4. Eliminar una materia del horario o actividad")
    print("5. Generar reporte del horario")
    print("6. Salir")
    print("\n=====================================================\n")

    opcion = input("Seleccione alguna de las opciones: ")
    print("\n---------------------------------------------------\n")

    if opcion == "1":
        registrar_horario()

    if opcion == "2":
        ver_horario()

    if opcion == "3":
        modificar_horario()

    if opcion == "4":
        eliminar_horario()

    if opcion == "5":
        generar_reporte()

    if opcion == "6":
        print("Horario finalizado, gracias por usar el programa")
        print("\n----------------------------------------------------\n")
        break

        