# Elio Yilali
# Comición 101
# Ejercicio: 08 tercera clase
#Ingresar 10 números enteros. Determinar el máximo y el mínimo.
numero_max = 0
numero_min = 0
i = 0

while i < 10:
    numero = input('Ingrese un numero :')
    numero = int(numero)
    if numero > numero_max or i== 0:
        numero_max = numero
    if numero < numero_min or i== 0:
        numero_min = numero
    i+= 1

print(f'El numero maximo es: {numero_max} \nEl numero minimo es: {numero_min}')