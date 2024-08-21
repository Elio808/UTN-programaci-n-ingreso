# Elio Yilali
# Comición 101
# Ejercicio: ejercicio 10

# Ingresar el sueldo, estado civil (casado o soltero) y cantidad de hijos de un empleado.
# Determinar si el empleado debe o no pagar el impuesto a las ganancias.
# El mismo no se pagará si el empleado es casado con hijos y sus ingresos son menores a $2200000.

print("\n")
print("♦-----------------------------------------------------------------------------♦","\n")


#variables.

sueldo = input("• Por favor, ingrese el sueldo del empliado: ")
sueldo = float(sueldo)

estado_civil = input("• Por favor, ingrese el estado civil del empliado (Solter@ o Casad@): ")

hijos_cantidad = input("• Por favor, ingrese la cantidad de hijos del empliado: ")
hijos_cantidad = int(hijos_cantidad)

print("\n")
print("♦------------------------------------------------------------------------------♦","\n")


#operaciones

if sueldo < 2200000 and hijos_cantidad > 0 and estado_civil == ("Casado" or "Casada"):
    print("• El empliado no debe pagar el impuesto de las ganacias.")

else:
    print("• El empliado debe pagar el impuesto de las ganancias.")

print("\n")
print("♦------------------------------------------------------------------------------♦","\n")