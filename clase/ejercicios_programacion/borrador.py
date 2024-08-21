
print("\n")
print("♦--------------------------------------------------------------------------------------------------------------------------♦","\n")

PRECIO_LAMPARITAS = 800

cantidad_lamparas = input("• Por favor,  ingrese la cantidad de lámparas que quiere comprar: ")
cantidad_lamparas = int(cantidad_lamparas)
marca = input("• Por favor, ngrese la marca (ArgentinaLuz o FelipeLamparas): ")

print("\n")
print("♦--------------------------------------------------------------------------------------------------------------------------♦","\n")

precio_total = PRECIO_LAMPARITAS * cantidad_lamparas
precio_total = float(precio_total)
        
if cantidad_lamparas >= 6:
    descuento = 50

elif cantidad_lamparas == 5:
    if marca == "ArgentinaLuz":
        descuento = 40
    else:
        descuento = 30

elif cantidad_lamparas == 4:
    if marca == "ArgentinaLuz" or marca == "FelipeLamparas":
        descuento = 25
    else:
        descuento = 20

elif cantidad_lamparas == 3:
    if marca == "ArgentinaLuz":
        descuento = 15
    elif marca == "FelipeLamparas":
        descuento = 10
    else:
        descuento = 5

else:
    descuento = 0

precio_descuento = precio_total - precio_total * descuento / 100

if precio_descuento > 4000:
    descuento_adicional = 5
    precio_descuento -= precio_descuento * descuento_adicional / 100
    mensaje = f"• Con la compra de {cantidad_lamparas} lampara/s, de la marca {marca}, obtienes un {descuento}% de descuento más un descuento adicional del {descuento_adicional}%.\n\n• Precio final: ${precio_descuento:.2f}\n\n• Precio final sin descuento: ${precio_total:.2f}"

else:
    mensaje = f"• Con la compra de {cantidad_lamparas} lampara/s, de la marca {marca} obtienes un {descuento}% de descuento.\n\n• Precio final: ${precio_descuento:.2f}\n\n• Precio final sin descuento: ${precio_total:.2f}"

print(mensaje)

print("\n")
print("♦--------------------------------------------------------------------------------------------------------------------------♦","\n")



