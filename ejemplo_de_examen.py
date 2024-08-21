# Nombre de carta
# Precio (número positivo, no puede ser mayor a 200000)
# Tipo (Mágica, Monstruo, Trampa)
# Rareza (Rara, Super Rara, Ultra Rara)

# Una vez finalizado el ingreso de datos se desea conocer:
# Cantidad de cartas de rareza Ultra raras cuyo precio oscile en 50000 y 80000 y sea de tipo Mágica o Trampa.
# El nombre y tipo de la carta con menor precio de la rareza Rara.
# El porcentaje de rara, super rara y ultra rara hay sobre el total
# Determinar el precio promedio por cada tipo de carta
# Determinar cuál fue el tipo de carta mas vendida
bandera_minima = False
minimo_precio = 0
contador_ultra_rara5080 = 0
contador_rara = 0
contador_super_rara = 0
contador_ultra_rara = 0
contador_mostruo = 0
contador_magica = 0

seguir = "si"
while seguir == "si":
    nombre = input("ingrese nombre: ")
    precio = input("ingrece precio: ")
    precio = float(precio)
    while precio < 0 or precio > 200000:
        precio = input("error, reintente: ")
        precio = float(precio)

    tipo = input("ingrese el tipo de la carta: ")
    while tipo != "Mágica" and tipo != "Monstruo" and tipo != "Trampa":
        tiopo = input("error, reintente: ")

    rareza = input("ingrese el rareza de la carta: ")
    while rareza != "Rara" and rareza != "Super rara" and rareza != "Ultra rara":
        rareza = input("error, reintente: ")
    
    # A Cantidad de cartas de rareza Ultra raras cuyo precio oscile en 50000 y 80000 y sea de tipo Mágica o Trampa.
    if rareza == "Ultra rara":
        contador_ultra_rara += 1
        if precio >= 50000 and precio <= 80000 and (tipo == "Magica" or "Trampa" ):
            contador_ultra_rara5080 +=1       
    elif rareza == "Rarar":

        # B El nombre y tipo de la carta con menor precio de la rareza Rara.
        if precio < minimo_precio or contador_rara == 0:
            minimo_precio = precio
            minimo_nombre = nombre
            minimo_tipo = tipo
        contador_rara += 1
    else:
        contador_super_rara += 1
    seguir = input("desea segur?: ")
contador_general = contador_super_rara + contador_rara + contador_ultra_rara

    # A Cantidad de cartas de rareza Ultra raras cuyo precio oscile en 50000 y 80000 y sea de tipo Mágica o Trampa
print(f"{contador_ultra_rara}")
    # B El nombre y tipo de la carta con menor precio de la rareza Rara.
if bandera_minima == True:
     print(f"{minimo_nombre}-{minimo_tipo}")
else:
    print("no se ingreso ninguna carta Rara par alcular el minimo")


# El porcentaje de rara, super rara y ultra rara hay sobre el total
pocentaje_rara = (contador_rara * 100) / contador_general
contador_ultra_rara = (contador_ultra_rara * 100) / contador_general











