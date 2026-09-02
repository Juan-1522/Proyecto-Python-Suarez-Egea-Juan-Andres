#El nombre es porque mi compañera Angie me dió la idea y me ayudó
#Por eso la llamé así xddd

import json

def registrar_horario():
    print("\n ========= Registrar Materia =========== \n")
    
    with open("Horario.json", "r", encoding="utf-8") as archivo:
        horario = json.load(archivo)
    
        materia = input("Ingrese la materia o actividad: ")
        dia = input("Ingrese el dia de la semana: ")
        hora_inicio = input("Ingrese la hora de inicio (24h): ")
        hora_salida = input("Ingrese la hora de salida (24h): ")
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
                  print("Dia", evento["dia"])
                  print("Hora de inicio", evento["hora_inicio"])
                  print("Hora de salida", evento["hora_salida"])
                  print("Ubicacion", evento["ubicacion"])
                  print("-------------------------------------")

def modificar_horario():
     with open("Horario.json", "r", encoding="utf-8") as archivo:
          horario = json.load(archivo)

          if len(horario) == 0:
               print("No hay un horario registrado")
               return

          if i, evento in enumerate(horario):
            print(i + 1, "-", evento["materia"], "-", evento["dia"])

            opcion = int(input("Ingrese el numero de materias que desea modificar: "))

            if opcion >= 1 and opcion <= len(horario):
                 evento = horario[opcion - 1]

                 print("\n Ingrese los nuevos datos: ")

                 evento["materia"] = input("Materia o actividad?: ")
                 evento["dia"] = input("Dia de la semana: ")
                 evento["hora_inicio"] = input("Hora de inicio?: ")
                 evento["hora_salida"] = input("Hora de salida?: ")
                 evento["ubicacion"] = input("Donde se realizara?: ")

                 with open("Horario.json", "w", encoding="utf-8") as archivo:
                      json.dump(horario, archivo, indent=4, ensure_ascii=False)

                 print("\n Materia o actividad modificada con exito :D")

            else:
                 print("Opcion inválida")