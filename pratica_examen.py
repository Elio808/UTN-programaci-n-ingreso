# El dueño de una tienda dedicada a la compra/venta de cartas de Yu-Gi-Oh, 
# desea ingresar en el sistema las ventas realizadas en el día de la fecha y a partir de ello, conocer ciertos datos en base a las cartas que se vendieron.

# Deberemos desarrollar un sistema para que el dueño pueda ingresar la siguiente información hasta que él lo decida.

# Nombre de carta
# Precio (número positivo, no puede ser mayor a 200000)
# Tipo (Mágica, Monstruo, Trampa)
# Rareza (Rara, Super Rara, Ultra Rara)

# Una vez finalizado el ingreso de datos se desea conocer:
# 1.Cantidad de cartas de rareza Ultra raras cuyo precio oscile en 50000 y 80000 y sea de tipo Mágica o Trampa.
# 2.El nombre y tipo de la carta con menor precio de la rareza Rara.
# 3.El porcentaje de rara, super rara y ultra rara hay sobre el total
# 4.Determinar el precio promedio por cada tipo de carta
# 5.Determinar cuál fue el tipo de carta mas vendida


bandera_menor_precio = True
menor_precio_rara = 0
menor_nombre_rara = 0
menor_tipo_rara= 0

contador_ultrarara_5080_MoT = 0

contador_rara = 0
contador_super_rara = 0
contador_ultra_rara = 0

contador_general = 0

total_precio_rara = 0
total_precio_SP_rara = 0
total_precio_mosntruo = 0

i = True

while i == True:
   contador_general += 1
   nombre = input("ingrese el nombre de la carta: ")

   precio = input("ingrese el precio de la carta: ")
   precio = float(precio)

   while precio < 0 or precio > 200000:
    precio = input("precio no valido, vuelva a intantar: ")
    precio = float(precio)      

   tipo = input("ingrese el tipo de la carta (Mágica, Monstruo, Trampa): ")
   while tipo != "Mágica" and tipo != "Monstruo" and tipo != "Trampa":
    tipo = input("tipo no valido, vuelva a intantar: ")     

   rareza = input("ingrese la rareza de la carta (Rara, Super Rara, Ultra Rara): ")
   while rareza != "Rara" and rareza != "Super Rara" and rareza != "Ultra Rara":
    rareza = input("rareza no valida, vuelva a intantar: ")

   if rareza == "Ultra Rara":
     contador_ultra_rara += 1
     if precio >= 50000 and precio <=80000 and tipo == "Mágica" or tipo == "Trampa":
      contador_ultrarara_5080_MoT += 1

   elif rareza == "Rara":
     contador_rara += 1
     
     if precio < menor_precio_rara or bandera_menor_precio == True:
         menor_precio_rara = precio
         menor_nombre_rara = nombre
         menor_tipo_rara= tipo
         bandera_menor_precio = False

   else:
     contador_super_rara +=1
     

   if tipo == "Monstruo":
    total_precio_mosntruo += precio
   elif tipo == "Mágica":
     total_precio_rara += precio
   else:
     total_precio_SP_rara += precio

   i = input("desa ingesar otra carta(si/no)?: ")
   if i != "si":
      i = False
   else:
      i = True



# 1.Cantidad de cartas de rareza Ultra raras cuyo precio oscile en 50000 y 80000 y sea de tipo Mágica o Trampa.
mensaje = f"Cantidad de cartas de rareza Ultra raras cuyo precio oscile en 50000 y 80000 y sea de tipo Mágica o Trampa es {contador_ultrarara_5080_MoT}"
print(mensaje)

# 2.El nombre y tipo de la carta con menor precio de la rareza Rara.
if menor_precio_rara != 0: 
 mensaje = f"El nombre y tipo de la carta con menor precio de la rareza Rara se llama {menor_nombre_rara} y su tipo es {menor_tipo_rara}"
else:
  mensaje = "no se ingreso ninguna carta de rareza Rara."
print(mensaje)

#3.El porcentaje de rara, super rara y ultra rara hay sobre el total
if contador_rara > 0:
  porcentaje_rara = contador_rara * 100 / contador_general
else:
  porcentaje_rara = 0

if contador_super_rara > 0:
  porcentaje_super_rara = contador_super_rara * 100 / contador_general
else:
  porcentaje_super_rara = 0

if contador_ultra_rara > 0:
  porcentaje_ultra_rara = contador_ultra_rara * 100 / contador_general
else:
  porcentaje_ultra_rara = 0

mensaje = f"los porcentajes de las cartas son\n Rara: {round(porcentaje_rara)}%\n Super rara: {round(porcentaje_super_rara)}%\n Ultra rara: {round(porcentaje_ultra_rara)}%"
print(mensaje)

# 4.Determinar el precio promedio por cada tipo de carta
if total_precio_rara > 0:
  promedio_rara = total_precio_rara / contador_general
else:
  promedio_rara = 0

if total_precio_SP_rara > 0:
  promedio_SP_rara = total_precio_SP_rara / contador_general
else:
  promedio_SP_rara = 0

if total_precio_monstruo > 0:
  promedio_UT_rara = total_precio_monstruo / contador_general
else:
  promedio_UT_rara = 0

mensaje = f"el precio promedio por cada tipo de carta es:\n Rara: {promedio_rara}\n Super rara: {promedio_SP_rara}\n Ultra rara: {promedio_UT_rara}"
print(mensaje)