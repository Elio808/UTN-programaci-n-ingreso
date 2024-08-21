# Elio Yilali
# Comición 101
# Ejercicio: 07

#Realizar un programa que a partir del ingreso de un sueldo (valor flotante) muestre dicho valor con un incremento del 15%.
sueldo_a = input("• Por favor, ingrese un dueldo: ")
sueldo_a = float(sueldo_a)
incremento = sueldo_a/100*15
sueldo_incrementado = sueldo_a + incremento
print(sueldo_incrementado)
