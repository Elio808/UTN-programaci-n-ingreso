# Elio Yilali
# Comición 101
# Ejercicio: integrador tercera clase
#Permitir que el usuario ingrese todos los números que desee. Los mismos deben estar comprendidos entre -10000 y 10000, y deben ser distintos de 0. Determinar:
# La suma acumulada de los números negativos.
# La suma acumulada de los números positivos.
# La cantidad de números negativos ingresados.
# El promedio de los números positivos.
# El número positivo más grande.
# El porcentaje de números negativos ingresados, respecto del total de ingresos.

contador_positivo = 0
contador_negativo = 0

acumulador_positivo = 0
acumulador_negativo = 0

mayor_positivo = 0

contador_general = 0

i = "si"

while i == "si":
    numero = input("ingrese un numero: ")
    numero = float(numero)
    while numero <= -10000 or numero >= 10000 or numero == 0:
        numero = input("numero no valido, igrese otro: ")
        numero = float(numero)
    if numero < 0:
         contador_negativo += 1
         acumulador_negativo += numero
    else:  
        contador_positivo += 1
        acumulador_positivo += numero
        if mayor_positivo < numero or contador_positivo == 1:
            mayor_positivo = numero
    contador_general += 1
    i = input("desea continuar (si/no)")


print(f"acumulador_negativo{acumulador_negativo}")
print(f"acumulador_positivo{acumulador_positivo}")
print(f"contador_negativo{contador_negativo}")

if contador_positivo > 0:
    promedio_positivo = acumulador_positivo / contador_positivo
    print(f"promedio_positivo{promedio_positivo}")
else:
    print("no se a igresado ningun numero positivo para sacar el promedio.")

print(f"mayor_positivo{mayor_positivo}")

if contador_negativo > 0:
   porcetaje_negetivo = (contador_negativo / contador_general) * 100
   print(f"porcetaje_negetivo{porcetaje_negetivo}")
else:
    print("no se a igresado ningun numero negativo para sacar el porcentaje.")