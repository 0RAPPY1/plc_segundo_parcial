https://replit.com/join/bvrsmqrdbz-julian-emilian1 
while (True):
  nombre = input("Coloca tu nombre: ")
  print(f"Hola! {nombre}")
  print(" ")
  print("Coloca lo que se te pide")
  
  print("Dias:")
  print("1) Lunes")
  print("2) Martes")
  print("3) Miercoles")
  print("4) Jueves")
  print("5) Viernes")
  print("6) Sábado")
  print("7) Domingo")
  Dia = int(input("Dia de la semana: "))
  
  print(" ")
  
  Hora = int(input("Coloca la hora en formato de 24h: "))
  
  print("") 
  
  print("Tipo de tareas: ")
  print("1) Estudio")
  print("2) Deportes")
  print("3) Descanso")
  print("4) Trabajo")
  Tarea = float(input("Tipo de tarea a realizar: "))
  print(" ")
  
  if Hora > 1 and Hora <= 5: 
    print(f"Debes de estar dormido {nombre}")
  elif Hora > 5 and Hora <= 14:
    print(f"Debes de estar en clase {nombre}")
  elif Hora > 14 and Hora <= 22:
    print(f"Puedes hacer tarea {nombre}")
  elif Hora > 18 and Hora <= 22 and Tarea == "3":
    print(f"Además de tomar una siesta puedes comenzar a realizar tus tareas {nombre}")
  elif Hora > 18 and Hora <= 22 and Dia == 6 or Dia == 7:
    print(f"Puedes ver una peli {nombre}")
  elif Hora > 14 and Hora <= 20 and Dia == 3 or Dia == 4 or Dia == 1:
    print(f"Puedes ir al gim {nombre}")
  elif Hora > 13 and Hora <= 15 and Dia == 2 or Dia == 4:
    print(f"Espero estés comiendo algo muy nutritivo {nombre}")
  else: 
    print(f"No se que pusiste mal {nombre}")
  m = input("¿Quieres empezar de nuevo? ").lower().strip()
  if m != "si":
    break
  else:
    print("Aqui vamos de nuevo")
    print(" ")
