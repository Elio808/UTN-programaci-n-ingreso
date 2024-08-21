# Elio Yilali
# Comición 101
# Ejercicio: 10 tercera clase
#Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Solo tendrá 3 intentos.
intentos = 1
i = "si"

clave = input("ingrese clave númerica: ")
clave = int ( clave)
ingreso = input("valifique la clave: ")
ingreso = int(ingreso)

while i == "si":
    intentos += 1
    if clave != ingreso:
        ingreso = input("clave no validad, vuelva a intentarlo: ")
    if intentos == 3:
            i = "no"
            print("intentos aotados.")
   