#   Estudiante : Elio Yilali       Divición : 101       Fecha : 07 / agosto / 2024

# Dr. Gregory Cat (Diagnostico Veterinario)
# Para el hospital Universitario Princeton-Plainsboro de Nueva Jersey.
# Es necesario registrar el ingreso de las mascotas en la próxima hora (solo se pueden
# atender 15 mascotas), para esto hay que considerar los siguientes datos y
# encasillarlos en ciertos diagnósticos para poder derivarlos adecuadamente:

# ● Edad (Validar entre 1 y 20 años)
# ● Tipo: (Validar “gato”, “perro”, “hámster”)
# ● Peso: (Más de 0 kg)
# ● Diagnóstico: (Validar “problemas digestivos”, “parásitos”, “infección”)
# ● Vacuna antirrábica (validar “si”, ”no”)

# Tema C
# 1. Cantidad de mascotas con parásitos o infección, cuya edad se encuentre entre
# los 15 y 18 años con más de 15 kg de peso.
# 2. El diagnostico mas ingresado de mascotas tipo perro.
# 3. Tipo y vacuna de la mascota más menos pesada, cuyo diagnóstico sea
# problemas digestivos.
# 4. Porcentaje de mascotas que ingresaron por cada uno de los diagnósticos.
# 5. Promedio de edad de los hámster

candiada_mascotas_PoI_edad1518_pesomas15 = 0

perro_contador_paracios = 0
perro_contador_infeccion = 0
perro_contador_problemas_digestivos = 0

diagnostico_mayor_perro = 0

PD_mascota_mas_pesada= 0
tipo_mas_pesado = 0
vacuna_mas_pesada = 0
PD_mascota_menos_pesada = 0
tipo_menos_pedado = 0
vacuna_menos_pesada = 0

contador_problema_digestivo = 0

contador_hamster = 0
edad_hamster_maximo = 0


i = 0
bandera_inicio = True


while i  < 15 and bandera_inicio == True:
    i += 1



    edad = input("ingrese la edad de la mascota: ")
    edad = int(edad)
    while not(edad >= 1 and edad <= 20):
     edad = input("edad no valida, vuelva a intentar: ")
     edad = int(edad)      

    tipo = input("ingrese el tipo de mascota( gato / perro / hámster ): ")
    while tipo != "gato" and tipo != "perro" and tipo != "hámster":
     tipo = input("tipo no valido, vuelve a intentar: ")      

    peso = input("ingrese el peso de la mascota: ")
    peso = float(peso)
    while peso < 1:
     peso = input("peso no valido, vuelva a intentar: ") 
     peso = float(peso) 

    diagnostico = input("ingrese el diagnostico de la mascota( problemas digestivos / parásitos / infección ): ")
    while diagnostico != "problemas digestivos" and diagnostico != "parásitos" and diagnostico != "infección":
     diagnostico = input("diagnostico no valido, vuelve a intentar: ") 
    
    vacuna = input("tine la vacuna antirrábica(si/no)?: ")
    while vacuna != "si" and vacuna != "no":
      vacuna = input("respuesta no valida, vuelva a intantar: ")



    if edad >= 15 and edad <= 18 and peso >= 15:
      if diagnostico == "parásitos":
         candiada_mascotas_PoI_edad1518_pesomas15 +=1
          
      elif diagnostico == "infección":
         candiada_mascotas_PoI_edad1518_pesomas15 +=1
        

    if diagnostico == "parásitos" and tipo == "perro" :
      perro_contador_paracios += 1
    if diagnostico == "infección" and tipo == "perro" :
     perro_contador_infeccion += 1
    if diagnostico == "problemas digestivos":
      contador_problema_digestivo += 1

      if peso > PD_mascota_mas_pesada or contador_problema_digestivo == 1:
         PD_mascota_mas_pesada
         vacuna_mas_pesada = vacuna
         tipo_mas_pesado = peso
      if peso < PD_mascota_menos_pesada or contador_problema_digestivo == 1:
        PD_mascota_menos_pesada = peso
        vacuna_menos_pesada = vacuna
        tipo_menos_pedado = peso
      
      if tipo == "perro":
         perro_contador_problemas_digestivos += 1
    
    if perro_contador_paracios > perro_contador_infeccion and perro_contador_paracios > perro_contador_problemas_digestivos:
      diagnostico_mayor_perro = "paracitos"
    elif perro_contador_infeccion > perro_contador_paracios and perro_contador_infeccion > perro_contador_problemas_digestivos:
       diagnostico_mayor_perro= "infección"
    else:
      diagnostico_mayor_perro= "problemas digestivos"

    if tipo == "hámster":
      contador_hamster += 1
      edad_hamster_maximo += edad






    bandera_inicio = input("desea ingresar otra mascota(si/no)?: ")
    if bandera_inicio == "si":
      bandera_inicio = True
    else:
      bandera_inicio = False

# 1. Cantidad de mascotas con parásitos o infección, cuya edad se encuentre entre
# los 15 y 18 años con más de 15 kg de peso.
mendaje = f"Cantidad de mascotas con parásitos o infección, cuya edad se encuentre entre los 15 y 18 años con más de 15 kg de peso es de {candiada_mascotas_PoI_edad1518_pesomas15}"
print (mendaje)
# 2. El diagnostico mas ingresado de mascotas tipo perro.
mendaje = f"el mayor diagnostico tipo perro fue : {diagnostico_mayor_perro}"
print(mendaje)
# 3. Tipo y vacuna de la mascota más menos pesada, cuyo diagnóstico sea
# problemas digestivos.
mendaje = f"el tipo y vacuna de el mas pesado es {tipo_mas_pesado} y su vacuna es {vacuna_mas_pesada}\n el tipo y vacuna de el manos pesado es {tipo_menos_pedado} y su vacuna es {vacuna_menos_pesada}"
print(mendaje)
# 5. Promedio de edad de los hámster
if contador_hamster>0:
  promedio = edad_hamster_maximo/i
  mendaje=  f"el primedio de mascotas tipo hamster es {promedio}"
else:
  mensaje="no ahy mascotas tipo Hamster"
print(mendaje)
