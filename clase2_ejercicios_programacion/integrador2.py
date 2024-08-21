# Elio Yilali
# Comición 101
# Ejercicio: integrador 2
print("\n")
print("♦--------------------------------------------------------------------------------------------------------------------------♦","\n")
#Valores.
PRECIO_LAMPARITAS = 800
cantidad_lamparas = input("• Por favor,  ingrese la cantidad de lámparas que quiere comprar: ")
cantidad_lamparas = int(cantidad_lamparas)
marca = input("• Por favor, ngrese la marca (ArgentinaLuz o FelipeLamparas): ")
print("\n")
print("♦--------------------------------------------------------------------------------------------------------------------------♦","\n")
precio_total = PRECIO_LAMPARITAS * cantidad_lamparas
precio_total = float(precio_total)
#Descarte de el descuento.
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
#Operaciones finales, pecio con porcentaje y salida en pantalla.
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
# Ferrete Lámparas

# En una ferretería se quiere implementar un sistema que permita a los usuarios saber cuánto deberán pagar por la compra de lámparas de bajo consumo. Se tiene en cuenta que todas las lámparas cuestan $800.
# A partir de la cantidad y marca de las lámparas compradas (solo se puede comprar una marca por vez) se aplicará el siguiente descuento:
# Si compra 6 o más  lámparas bajo consumo tiene un descuento del 50%. 
# Si compra 5  lámparas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
# Si compra 4  lámparas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
# Si compra 3  lámparas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
# Por otro lado, si el importe final con descuento suma más de $4000  se obtiene un descuento adicional de 5%.
# Mostrar por pantalla: 
# Marca, cantidad de lámparas, total a pagar sin descuento, el descuento obtenido si corresponde, el descuento adicional (si corresponde) y el total a pagar con descuento.