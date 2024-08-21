# Ingresar el sueldo, estado civil (casado o soltero) y cantidad de hijos de un empleado.
# Determinar si el empleado debe o no pagar el impuesto a las ganancias.
# El mismo no se pagará si el empleado es casado con hijos y sus ingresos son menores a $2200000.

#variables.

sueldo = input("• Por favor, ingrese el sueldo del empliado: ")
sueldo = float(sueldo)

estado_civil = input("• Por favor, ingrese el estado civil del empliado (Solter@ o Casad@): ")

hijos_cantidad = input("• Por favor, ingrese la cantidad de hijos del empliado: ")
hijos_cantidad = int(hijos_cantidad)

#operaciones

if sueldo < 2200000 and hijos_cantidad > 0 and estado_civil == ("Casado" or "Casada"):
    print("tranquilo menos, tu no pagas nada ;)")

else:
    print("usted tine que pagar el inpuesto mamahuvo >:(")