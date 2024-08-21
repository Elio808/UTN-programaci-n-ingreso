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

cntador_masculino_ikea = 0

menor_edad_apple = 999

nombre_minimo = 0
genero_minimo = 0

contador_general = 0

contador_femenino_ikea = 0


i = True

while i == True:
    contador_general += 1

    nombre = input("ingrese su nombre: ")

    edad = input("ingrese su edad: ")
    edad = int(edad)
    while edad < 18:
     edad = input("no puede votar siendo menor de edad, intentelo cuando cumpla los 18: ")
     edad = int(edad) 

    empleado = input("¿tine chamba?(si/no): ")
    while empleado != "si" and empleado != "no":
     empleado = input("respuesta no valida, vuelva a intentar: ")     

    genero = input("ingrese su genero (Masculino / Femenino / Otro):")
    while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
     genero = input("genero no valida, vuelva a intentar: ")    

    voto = input("ingrese su voto (APPLE / DUNKIN / IKEA):")
    while voto != "APPLE" and voto != "DUNKIN" and voto != "IKEA":
     voto = input("voto no valida, vuelva a intentar: ")

    if genero == "Masculino" and ((18 <= edad <= 25) or (36 <= edad <= 49) or voto == "IKEA"):
      cntador_masculino_ikea += 1      

    if voto == "APPLE":
      if edad < menor_edad_apple:
        menor_edad_apple = edad
        nombre_minimo = nombre
        genero_minimo = genero

    if genero == "Femenino" and edad > 25 and voto == "IKEA":
        contador_femenino_ikea +=1


    i = input("desa ingresar otro voto?(si/no): ")
    while i != "si" and i != "no":
       i = input("LA RESPUESTA ES SI O NO CRABRON! NO SEA BRUTO!(si/no): ")

    if i == "si":
      i = True
    else:
      i = False



# 1. Cantidad de encuestados de género Masculino, cuya edad esté entre 18 y
# 25 o entre 36 y 49 o que votaron por IKEA.
mensaje = f"la cantidad de encuestados de género Masculino, cuya edad esté entre 18 y 25 o entre 36 y 49 o que votaron por IKEA es {cntador_masculino_ikea}"
print(mensaje)


# 2. Nombre y género del encuestado de menor edad que votó por APPLE.
if menor_edad_apple == 999:
  mensaje = f"nadie voto por APPLE    T_T"
  print(mensaje)
else:
  mensaje = f"el nombre y género del encuestado de menor edad que votó por APPLE se llama {nombre_minimo} y su genero es {genero_minimo}."
  print(mensaje)

# 3. Porcentaje de encuestados de género Femenino que votaron por IKEA con edad mayor a 25 años.

if contador_femenino_ikea > 0:
  porcentaje = contador_femenino_ikea * 100 / contador_general
  mensaje = f"el porcentaje de encuestados de género Femenino que votaron por IKEA con edad mayor a 25 años es {round(porcentaje)}%"
  print (mensaje)
else:
  mensaje = "no hay votantes de genero femenico que votaran por IKEA con edad mayor a 25 años"
  print (mensaje)