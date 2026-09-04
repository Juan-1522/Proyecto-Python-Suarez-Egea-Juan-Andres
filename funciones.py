#Tengo que hacerle honor a mi compañera Angie que me ayudó a hacerlo más práctico xd

import json
from datetime import datetime

def validar_hora(hora):
     try:
          datetime.strptime(hora, "%H:%M")
          return True
     except ValueError:
          try:
               datetime.strptime(hora, "%I:%M %p")
               return True
          except ValueError:
               return False

def convertir_hora(hora):
     try:
          tiempo = datetime.strptime(hora, "%H:%M")
     except ValueError:
          tiempo = datetime.strptime(hora, "%I:%M %p")

     return tiempo.hour * 60 + tiempo.minute


def normalizar_dia(dia):
     dia = dia.strip().lower()

     equivalencias = {
          "lunes": "Lunes",
          "martes": "Martes",
          "miercoles": "Miercoles",
          "miércoles": "Miércoles",
          "jueves": "Jueves",
          "viernes": "Viernes",
     }

     return equivalencias.get(dia)


def conflicto(horario, nuevo_dia, nueva_hora_inicio, nueva_hora_salida, indice_excluir=None):
     nueva_hora_inicio = convertir_hora(nueva_hora_inicio)
     nueva_hora_salida = convertir_hora(nueva_hora_salida)

     for i, evento in enumerate(horario):

          if indice_excluir is not None and i == indice_excluir:
               continue

          dia_evento = normalizar_dia(evento["dia"])
          nuevo_dia = normalizar_dia(nuevo_dia)

          if dia_evento != nuevo_dia:
               continue

          inicio_evento = convertir_hora(evento["hora_inicio"])
          salida_evento = convertir_hora(evento["hora_salida"])

          if nueva_hora_inicio < salida_evento and nueva_hora_salida > inicio_evento:
               return True
     return False


def registrar_horario():
    print("=============== Registrar Materia ================")
    
    with open("Horario.json", "r", encoding="utf-8") as archivo:
        horario = json.load(archivo)
    
        materia = input("\nIngrese la materia o actividad: ")
        
        while True:
             dia = input("Ingrese el dia de la semana: ")

             if normalizar_dia(dia) is not None:
                  break
             else:
                  print("Dia inválido. Ingrese un día de lunes a viernes")

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

        inicio = convertir_hora(hora_inicio)
        salida = convertir_hora(hora_salida)

        if salida <= inicio:
             print("\nNo se puedo registrar la materia")
             print("\nLa hora de salida debe ser posterior a la hora de inicio")
             return

        if conflicto(horario, dia, hora_inicio, hora_salida):
             print("\nNo se puedo registrar la materia")
             print("El horario se cruza con una materia o actividad")
             return
        

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

                print("\n----------------------------------------------------\n")
                print("Materia o actividad registrada con exito :D")

def ver_horario():
     with open("Horario.json", "r", encoding="utf-8") as archivo:
        horario = json.load(archivo)

        print("=========== Horario de clase ============")

        if len(horario) == 0:
             print("No hay horario registrado")
        else:
             orden_dias = {
                  "lunes": 1,
                  "martes": 2,
                  "miercoles": 3,
                  "miércoles": 3,
                  "jueves": 4,
                  "viernes": 5
             }

             horario.sort(
                  key=lambda evento: (
                       orden_dias.get(evento["dia"].lower(), 6), 
                         convertir_hora(evento["hora_inicio"])
                    )
               )

             for evento in horario:
                  print("Materia o actividad: ", evento["materia"])
                  print("Dia: ", evento["dia"])
                  print("Hora de inicio: ", evento["hora_inicio"])
                  print("Hora de salida: ", evento["hora_salida"])
                  print("Ubicacion: ", evento.get("ubicacion", ""))
                  print("-------------------------------------")

def modificar_horario():
     with open("Horario.json", "r", encoding="utf-8") as archivo:
          horario = json.load(archivo)

          if len(horario) == 0:
               print("No hay un horario registrado")
               return

          for i, evento in enumerate(horario):
               print(i + 1, "-", evento["materia"], "-", evento["dia"])

          try:
               opcion = int(input("Ingrese el numero de la materia que desea modificar: "))
          except ValueError:
               print("Debe ingresar un numero")
               return

          if opcion < 1 or opcion > len(horario):
               print("Opcion inválida")
               return

          indice = opcion - 1
          print("\nIngrese los nuevos datos: ")

          nueva_materia = input("Materia o actividad: ")

          while True:
               nuevo_dia = input("Dia de la semana: ")

               if normalizar_dia(nuevo_dia) is not None:
                    break
               else:
                    print("Dia inválido. Ingrese un día de lunes a viernes")

          while True:
               nueva_hora_inicio = input("Hora de inicio: ")

               if validar_hora(nueva_hora_inicio):
                    break
               else:
                    print("Hora de inicio inválida")

          while True:
               nueva_hora_salida = input("Hora de salida: ")

               if validar_hora(nueva_hora_salida):
                    break
               else:
                    print("Hora de salida inválida")

          inicio = convertir_hora(nueva_hora_inicio)
          salida = convertir_hora(nueva_hora_salida)

          if salida <= inicio:
               print("\nLa hora de salida debe ser posterior a la hora de inicio")
               return

          if conflicto(horario, nuevo_dia, nueva_hora_inicio, nueva_hora_salida, indice):
               print("\nNo se puede modificar la materia")
               print("El nuevo horario se cruza con otra materia o actividad")
               return

          nueva_ubicacion = input("Dónde se realizará?: ")

          horario[indice] = {
          "materia": nueva_materia,
          "dia": nuevo_dia,
          "hora_inicio": nueva_hora_inicio,
          "hora_salida": nueva_hora_salida,
          "ubicacion": nueva_ubicacion
     }

     with open("Horario.json", "w", encoding="utf-8") as archivo:
          json.dump(horario, archivo, indent=4, ensure_ascii=False)
          print("\n----------------------------------------------------\n")
          print("Materia o actividad modificada con exito :D")

def eliminar_horario():
     with open("Horario.json", "r", encoding="utf-8") as archivo:
          horario = json.load(archivo)

          if len(horario) == 0:
               print("No hay horario o materias registradas")
               return

          for i, evento in enumerate(horario):
               print(i + 1, "-", evento["materia"], "-", evento["dia"])

          try:
               opcion = int(input("Ingrese la materia o actividad que quiera eliminar: "))
          except ValueError:
               print("Debe ingresar un número")
               return

          if opcion >= 1 and opcion <= len(horario):
               horario.pop(opcion - 1)

               with open("Horario.json", "w", encoding="utf-8") as archivo:
                    json.dump(horario, archivo, indent=4, ensure_ascii=False)
          
                    print("\n-------------------------------------------------\n")
                    print("Materia eliminada con exito")

          else:
               print("Opcion inválida")

def generar_reporte():
     print("\n================ Reporte Semanal ===================\n")

     with open("Horario.json", "r", encoding="utf-8") as archivo:
          horario = json.load(archivo)

          #print("\nDEBUG:")
          #for evento in horario:
               #print(evento["materia"], "->", evento["dia"])

          dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

          reporte = []

          for dia in dias:
               eventos_dia = []

               for evento in horario:
                    if evento["dia"].strip().lower() == dia.lower():
                         eventos_dia.append({
                              "materia": evento["materia"],
                              "hora_inicio": evento["hora_inicio"],
                              "hora_salida": evento["hora_salida"],
                              "ubicacion": evento.get("ubicacion", "")  
                         })

               eventos_dia.sort(key=lambda evento: convertir_hora(evento["hora_inicio"]))

               reporte.append({
                    "dia": dia,
                    "eventos": eventos_dia
                         })

          for dia in reporte:
               print(dia["dia"] + ":")

               if len(dia["eventos"]) == 0:
                    print("- Libre")
                    print("\n-------------------------------------------------\n")

               else: 
                    for evento in dia["eventos"]:
                         print("-", evento["materia"], 
                              "(" + evento["hora_inicio"] + " - " + evento["hora_salida"] + ")", "en", evento["ubicacion"])

                    print("\n-------------------------------------------------\n")

          with open("Reporte_horario.json", "w", encoding="utf-8") as archivo:
               json.dump(reporte, archivo, indent=4, ensure_ascii=False)

               print("\n============= Reporte generado con exito ===============\n")
               print("\nPresione ENTER para continuar\n")
               input()