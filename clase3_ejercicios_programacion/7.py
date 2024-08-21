# Elio Yilali
# Comición 101
# Ejercicio: 07 tercera clase
# Solicitar al usuario que ingrese números (hasta que no quiera ingresar más).
#  Calcular la suma de los números positivos y el producto de los negativos.

acumulador_pocitivo = 0
acumulador_negaticvo = 0

i = "si"
while i == "si":
    numero = input("ingrese un número: ")
    numero = float(numero)
    if numero >= 0:
        acumulador_pocitivo += numero
    else:
        acumulador_negaticvo += numero
    i = input("desa continuar (si/no): ")


print(f"la suma de los positivos es {acumulador_pocitivo} y el producto de los negativos es {acumulador_negaticvo}")