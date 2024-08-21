# Elio Yilali
# Comición 101
# Ejercicio: 05 tercera clase
#Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla.
print("\n")
print("♦-----------------------------------------------------------------------------♦","\n")
seguir = "si"
acmulador = 0
i = 0
while seguir == "si":
    numero = input("ingrece un numero: ")
    numero = float(numero)
    acmulador += numero
    seguir = input("desea continuar si/no: ")
    i += 1
promedio = acmulador / i
print(f"la suma acumulada es:{acmulador}")
print(f"el promedio es:{promedio}")