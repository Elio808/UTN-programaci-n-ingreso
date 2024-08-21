# Elio Yilali
# Comición 101
# Ejercicio: 09 tercera clase
#Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Tendrá intentos indeterminados.

i = "si"

clave = input("ingrese clave númerica: ")
clave = int ( clave)

while i == "si":
    ingreso = input("valifique la clave: ")
    ingreso = int(ingreso)
    if clave != ingreso:
        ingreso = input("clave no validad, vuelva a intentarlo: ")
    i = input("clave validad, ¿quire reiniciar? (si/no):")