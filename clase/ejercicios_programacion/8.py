# Elio Yilali
# Comición 101
# Ejercicio: 08

# Realizar un programa que a partir 
# del ingreso de un sueldo y de un porcentaje de aumento, calcule y muestre el sueldo con el aumento porcentual ingresado por el usuario.

print("\n")
print("♦--------------------------------------------------------------♦","\n")

sueldo = input("• Por favor, ingrese un sueldo: ")
sueldo = float(sueldo)

porcentual = input("• Por favor, ingrese un número para el porcentaje de aumento: ")
porcentual = float(porcentual)

print("\n")
print("♦--------------------------------------------------------------♦","\n")

porcentaje = sueldo / 100 * porcentual

sueldo_aumentado = sueldo + porcentaje

print(f"• El sueldo más un {porcentual} % de aumento es: {sueldo_aumentado}")

print("\n")
print("♦--------------------------------------------------------------♦","\n")