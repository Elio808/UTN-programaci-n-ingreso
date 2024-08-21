#Estudiante: Elio Yilali        División: 101       Examen final

# UTN Inversiones, realiza un estudio de mercado para saber cuál será la nueva
# franquicia que se insertará en el mercado argentino y en la cual invertirán.
# Las posibles franquicias son las siguientes: Apple, Dunkin o Ikea.
# Para ello, se realizará una encuesta mediante un sistema de voto electrónico, con el
# propósito de conocer cuáles son los gustos de los encuestados (no se sabe cuántos):
# Se ingresa de cada encuestado:
# ● nombre
# ● edad (no menor a 18)
# ● está empleado (si-no)
# ● género (Masculino - Femenino - Otro)
# ● voto (APPLE, DUNKIN, IKEA)
# Se necesita saber:
# 1. Cantidad de encuestados de género Masculino, cuya edad esté entre 18 y
# 25 o entre 36 y 49 o que votaron por IKEA.
# 2. Nombre y género del encuestado de menor edad que votó por APPLE.
# 3. Porcentaje de encuestados de género Femenino que votaron por IKEA con
# edad mayor a 25 años.

encuestado_especificos = 0
minima_edad_voto_apple = 0

contador_apple = 0
contador_ikea = 0

contador_general = 0

porcentaje_votados_ikea = 0


i = "si"





while i == "si":
    nombre = input("ingrese su nombre:")

    edad = input("ingres su edad: ")
    edad = int(edad)
    while edad < 18:
     edad = input("tine que ser mayor de edad, vuelva a intentar: ")
     edad = int(edad)        

    empliado = input("esta empleado?(si/no): ")
    while empliado != "si" and empliado != "no":
       empliado = input("respuesta no valida, vuelva a intantar: ")

    genero = input("ingrese su genero (Masculino / Femenino / Otro): ")
    while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
        genero  = input("genero no valido, vuelva a intenter: ")
    
    voto = input("ingrese su voto (APPLE / DUNKIN / IKEA): ")
    while voto != "APPLE" and voto != "DUNKIN" and voto != "IKEA":
        voto  = input("voto no valido, vuelva a intenter: ")   
    if voto == "APPLE":
      if  edad < minima_edad_voto_apple or contador_apple == 0:
         minima_edad_voto_apple = edad
    if voto == "IKEA":
       contador_ikea += 1

    contador_general += 1

    i = input("desea ingresar otro voto? (si/no): ")

# 1. Cantidad de encuestados de género Masculino, cuya edad esté entre 18 y
# 25 o entre 36 y 49 o que votaron por IKEA.

if genero == "Masculino" and edad >= 18 and edad <= 25 or (edad >= 36 and edad <=49) or voto == "IKEA":
   encuestado_especificos += 1
   mensaje = (f"Cantidad de encuestados de género Masculino, cuya edad esté entre 18 y 25 o entre 36 y 49 o que votaron por IKEA son {encuestado_especificos}\n")

print(mensaje)
    
#2. Nombre y género del encuestado de menor edad que votó por APPLE.
if voto == "APPLE":
 print(f"Nombre y género del encuestado de menor edad que votó por APPLE sue {nombre} y su genero es {genero}\n")
else:
   print("nadie voto por APPLE\n")
# 3. Porcentaje de encuestados de género Femenino que votaron por IKEA con
# edad mayor a 25 años.

if genero == "Femenino" and voto == "IKEA" and edad > 25:
    if contador_ikea > 0:
       porcentaje_votados_ikea * 100 /  contador_general
    else:
      print("no hay votos para sacar un porcentaje.\n")
else:
    print("no hay votos que cumplan los requecitos para sacar un porcentaje.\n")