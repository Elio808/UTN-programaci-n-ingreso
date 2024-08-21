# Elio Yilali
# Comición 101
# Ejercicio: 06 tercera clase
#Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). 
#Calcular la suma de los números ingresados y el promedio de los mismos.
i = "si"
suma_total  =  0
while i == "si":
    numero = input("ingrese un número: ")
    numero = float(numero)
    suma_total += numero
    i = input("desea continuar? (si/no)")

print(f"la suma totoal es {suma_total}")
