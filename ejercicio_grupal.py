#Calcular e informar:    


#d_Porcentaje de usuarios que invirtieron en MEP, siempre y cuando el monto se encuentre entre $20000 y $50000.


#De los inversionistas, no se sabe cuántos, registrar:
#Nombre
#Monto en pesos de la operación (no menor a $10000)
#Cantidad de instrumentos
#Tipo (CEDEAR, BONOS, MEP)

#datos usuario
nombre = 0
monto = 0
tipo = 0

#acumuladores
acumular_cedear = 0
acumular_bonos = 0
acumular_mep = 0

#instrumentos
cantidad_instrumentos = 0
instrumentos_max = 0

menor_monto = 0
instrumentos_menor_inversor = 0

flag = "S"

cantidad_bonos = 0

i = 0

while flag == "S":

    nombre = input("\nNombre: ")

    monto = input("monto: ")
    monto = int(monto)

    while monto < 10000:
        print("\nMonto no valido. No debe ser menor a 10000")
        monto = input ("Ingrese otro monto: ")
        monto = int(monto)


    cantidad_instrumentos = input("\nCantidad de instrumentos: ")
    cantidad_instrumentos = int(cantidad_instrumentos)

    tipo = input("Ingrese el tipo: ")

    while tipo != "CEDEAR" and tipo != "BONOS" and tipo != "MEP":
        tipo = input("\nTipo no valido. Reingrese el dato: ")

    if tipo == "CEDEAR":
        acumular_cedear += cantidad_instrumentos

    elif tipo == "BONOS":
        acumular_bonos += cantidad_instrumentos
        if cantidad_instrumentos >= 150 and cantidad_instrumentos <= 200 and monto > 50000:
            cantidad_bonos += 1

    elif tipo == "MEP":
        acumular_mep += cantidad_instrumentos

#punto C
    if tipo == "BONOS" or tipo == "MEP":
        if monto < menor_monto or i == 0:
            menor_inversor = nombre
            menor_monto = monto
            instrumentos_menor_inversor = cantidad_instrumentos
            i += 1

    flag = input("\nDesea ingresar mas datos (S o N): ")

#a_Tipo de instrumento que más se operó.

if acumular_cedear > acumular_bonos and acumular_cedear > acumular_mep:
    instrumentos_max = "CEDEAR"
elif acumular_bonos > acumular_cedear and acumular_bonos > acumular_mep:
    instrumentos_max = "BONOS"
else:
    instrumentos_max = "MEP"

print(f"Instrumento mas operado: {instrumentos_max}")

#b_Cantidad de usuarios que compraron entre 150 y 200 BONOS y que invirtieron más de $50000.

print(f"Usuarios que compraron +150 BONOS: {cantidad_bonos}")

#c_Nombre y cantidad de instrumentos del usuario que compró BONOS o MEP, que menos dinero invirtió.
if i >= 1:
    mensaje_inversor = f"\nNombre menor inversor {menor_inversor}"
    mensaje_inversor += f"\n y cantidad de instrumentos: {instrumentos_menor_inversor}"