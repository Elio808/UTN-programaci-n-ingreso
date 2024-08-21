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
# 1. Cantidad de encuestados desempleados que votaron por DUNKIN o IKEA,
# cuya edad esté entre 25 y 50 años inclusive.
# 2. Nombre y voto del encuestado de género Masculino con menor edad.
# 3. Porcentaje de votos de cada género.
# 4. Promedio de edad de los encuestados de género Femenino que votaron
# IKEA.
# 5. Determinar cuál fue el género que tuvo más encuestados.

cantidad_desempleados_dunki_ikea = 0

minima_edad_masculina = 0
minimo_nombre_masculino = 0
minimo_voto_masculino = 0

contador_general = 0

contador_femenino = 0
contador_masculino = 0
contador_otro = 0

porcentaje_femenino = 0
porcentaje_masculino = 0
porcentaje_otro = 0

total_edad_femenina= 0
contador_femenino_ikea = 0

bandera_masculina = True

i = True

while i == True:
    contador_general += 1
    nombre = input("ingrese su nombre: ")

    edad = input("ingrese su edad: ")
    edad = int(edad)
    while edad < 18:
        edad = input("edad no valida, vuelva a intentar: ")
        edad = int(edad)        

    empleado = input("tine empleo(si/no)?: ")
    while empleado != "si" and empleado != "no":
        empleado = input("respuesta no valida, vuelva a intentar: ")     

    genero = input("ingrese su género (Masculino - Femenino - Otro): ")   
    while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
        genero = input("respuesta no valida, vuelva a intentar: ")      

    voto = input("ingrese su voto (APPLE - DUNKIN - IKEA): ")   
    while voto != "APPLE" and voto != "DUNKIN" and voto != "IKEA":
        voto = input("respuesta no valida, vuelva a intentar: ")  

    if empleado == "no" and (25<= edad <= 50) and voto == ("DUNKIN" or "IKEA"):

        cantidad_desempleados_dunki_ikea +=1

    if genero == "Masculino":
        contador_masculino += 1
        if edad < minima_edad_masculina or bandera_masculina == True:
            minima_edad_masculina = edad
            minimo_nombre_masculino = nombre
            minimo_voto_masculino = voto
            bandera_masculina = False

    elif genero == "Femenino":
        contador_femenino += 1
        total_edad_femenina += edad
        if voto == "IKEA":
            contador_femenino_ikea += 1
    else:
        contador_otro += 1
    
    i = input("desea continuar (si/no)?: ")
    if i == "si":
        i = True
    else:
        i = False

# 1. Cantidad de encuestados desempleados que votaron por DUNKIN o IKEA,
# cuya edad esté entre 25 y 50 años inclusive.
mensaje = f"Cantidad de encuestados desempleados que votaron por DUNKIN o IKEA, cuya edad esté entre 25 y 50 años inclusive es de {cantidad_desempleados_dunki_ikea}"
print(mensaje)

# 2. Nombre y voto del encuestado de género Masculino con menor edad.
if minima_edad_masculina == 0:
    mensaje = "no huvo votantes masculinos"
else:    
    mensaje = f"Nombre y voto del encuestado de género Masculino con menor edad se llama {minimo_nombre_masculino} y su voto fue para {minimo_voto_masculino}"
print (mensaje)

# 3. Porcentaje de votos de cada género.
if contador_femenino > 0:
    porcentaje_femenino = contador_femenino * 100 / contador_general
if contador_masculino > 0:
    porcentaje_masculino = contador_masculino * 100 / contador_general
if contador_otro > 0:
    porcentaje_otro = contador_otro * 100 / contador_general
mensaje = f"Porcentaje de votos de cada género:\n  femenino = {round(porcentaje_femenino)}%\n  masculino = {round(contador_masculino)}%\n  otro = {round(porcentaje_otro)}%\n"
print (mensaje)

# 4. Promedio de edad de los encuestados de género Femenino que votaron
# IKEA.
if contador_femenino_ikea > 0:
    promedio = total_edad_femenina / contador_femenino_ikea
    mensaje = f"Promedio de edad de los encuestados de género Femenino que votaron IKEA es de {promedio}"
else:
    promedio = 0
    mensaje = f"Promedio de edad de los encuestados de género Femenino que votaron IKEA es de {promedio}"

# 5. Determinar cuál fue el género que tuvo más encuestados.
if contador_femenino > contador_masculino and contador_femenino > contador_otro:
  
  
    mensaje = "el genero más encuestado fue femnino"
elif contador_masculino > contador_femenino and contador_masculino > contador_otro:
    mensaje = "el genero más encuestado fue masculino"
else:
    mensaje = "el genero más escuenstado fue otro"

print (mensaje)