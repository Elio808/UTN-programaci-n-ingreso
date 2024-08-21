# Elio Yilali
# Comición 101
# Ejercicio: 09

# Realizar un programa que a partir del ingreso del importe de una compra, aplique un 25% de descuento. 
# Mostrar por pantalla cuánto es el total a pagar y cuánto fue el descuento obtenido.

inporte = input("• Por favor ingrese el importe de su compre: ")
inporte = float(inporte)

descuento = inporte/100*25

inporte_con_descuento = inporte - descuento
print("• Importe con descuento.")
print(inporte_con_descuento)
print("• Descuento.")
print(descuento)
