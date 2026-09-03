#El nombre es porque mi compañera Angie me dió la idea y me ayudó
#Por eso la llamé así xddd

import json
from datetime import datetime

def validar_hora(hora):
     try:
          datetime.strptime(hora, "%I:%M &p")
          return True
     except ValueError:
          return False

def registrar_horario():
    print("============ Registrar Materia ==============")
    
    with open("Horario.json", "r", encoding="utf-8") as archivo:
        horario = json.load(archivo)
    
        materia = input("Ingrese la materia o actividad: ")
        dia = input("Ingrese el dia de la semana: ")

        while True:
             hora_inicio = input("Ingrese la hora de inicio (24h): ")

             if validar_hora(hora_inicio):
                  break
             else:
                  print("Hora de inicio inválida. No se puede poner esa hora de clase")

        while True:
             hora_salida = input("Ingrese la hora de salida (24h): ")

             if validar_hora(hora_salida):
                  break
             else:
                  print("Hora de salida inválida. No se puede poner esa hora de clase")

        
        ubicacion = input("Ingrese la ubicacion (opcional): ")
    
        nuevo_evento = {
                    "materia": materia,
                    "dia": dia,
                    "hora_inicio": hora_inicio,
                    "hora_salida": hora_salida,
                    "ubicacion": ubicacion
                }
    
        horario.append(nuevo_evento)
    
        with open("Horario.json", "w", encoding="utf-8") as archivo:
                json.dump(horario, archivo, indent=4, ensure_ascii=False)
    
                print("\n")
                print("Materia o actividad registrada con exito :D")

def ver_horario():
     with open("Horario.json", "r", encoding="utf-8") as archivo:
        horario = json.load(archivo)

        if len(horario) == 0:
             print("No hay horario registrado")
        else:
             for evento in horario:
                  print("Materia o actividad: ", evento["materia"])
                  print("Dia: ", evento["dia"])
                  print("Hora de inicio: ", evento["hora_inicio"])
                  print("Hora de salida: ", evento["hora_salida"])
                  print("Ubicacion: ", evento["ubicacion"])
                  print("-------------------------------------")

def modificar_horario():
     with open("Horario.json", "r", encoding="utf-8") as archivo:
          horario = json.load(archivo)

          if len(horario) == 0:
               print("No hay un horario registrado")
               return

          for i, evento in enumerate(horario):
               print(i + 1, "-", evento["materia"], "-", evento["dia"])

          cantidad = int(input("\nIngrese la cantidad de materias que desea modificar: "))

          for x in range(cantidad):
               opcion = int(input("Ingrese el numero de la materia que desea modificar: "))

               if opcion >= 1 and opcion <= len(horario):
                    evento = horario[opcion - 1]

                    print("\nIngrese los nuevos datos: ")

                    evento["materia"] = input("Materia o actividad?: ")
                    evento["dia"] = input("Dia de la semana: ")
                    evento["hora_inicio"] = input("Hora de inicio?: ")
                    evento["hora_salida"] = input("Hora de salida?: ")
                    evento["ubicacion"] = input("Donde se realizara?: ")
               else:
                    print("Opcion inválida")
                    return

     with open("Horario.json", "w", encoding="utf-8") as archivo:
          json.dump(horario, archivo, indent=4, ensure_ascii=False)
          print("Materia o actividad modificada con exito :D")

def eliminar_horario():
     with open("Horario.json", "r", encoding="utf-8") as archivo:
          horario = json.load(archivo)

          if len(horario) == 0:
               print("No hay horario o materias registradas")
               return

          for i, evento in enumerate(horario):
               print(i + 1, "-", evento["materia"], "-", evento["dia"])

          opcion = int(input("Ingrese la materia o actividad que quiera eliminar: "))

          if opcion >= 1 and opcion <= len(horario):
               horario.pop(opcion - 1)
          else:
               print("Opcion invalida")

     with open("Horario.json", "w", encoding="utf-8") as archivo:
          json.dump(horario, archivo, indent=4, ensure_ascii=False)
          
          print("Materia eliminada con exito")

def generar_reporte():
     print("========= Reporte Semanal =========")

     with open("Horario.json", "r", encoding="utf-8") as archivo:
          horario = json.load(archivo)

          dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

          reporte = []

          for dia in dias:
               eventos_dia = []

               for evento in horario:
                    if evento ["dia"].lower() == dia.lower():
                         eventos_dia.append({
                              "materia": evento["materia"],
                              "hora_inicio": evento["hora_inicio"],
                              "hora_salida": evento["hora_salida"],
                              "ubicacion": evento["ubicacion"]  
                         })

               reporte.append({
                    "dia": dia,
                    "eventos": eventos_dia
                         })

          for dia in reporte:
               print(dia["dia"] + ":")

               if len(dia["eventos"]) == 0:
                    print("- Libre")
                    print("-------------------------------------------------")

               else: 
                    for evento in dia["eventos"]:
                         print("-", evento["materia"], 
                              "(" + evento["hora_inicio"] + " - " + evento["hora_salida"] + ")", "en", evento["ubicacion"])

                    print("-------------------------------------------------")

          with open("Reporte_horario.json", "w", encoding="utf-8") as archivo:
               json.dump(reporte, archivo, indent=4, ensure_ascii=False)

               print("\n===== Reporte generado con exito =====\n")
               print("\nPresione ENTER para continuar\n")
               input()