# Elio Yilali
# Comición 101
# Ejercicio: 06

# Realizar un programa que pida dos números enteros.
# Calcular y mostrar el resto de la división entre ambos números. Ej: "El resto de dividir 7 por 2 es: 1" .
print("\n")
print("♦--------------------------------------------------------------♦","\n")

numero_a = input("• Por favor, ingrese un número entero: ")
numero_a = int(numero_a)

numero_b = input("• Por favor, ingrese otro número entero: ")
numero_b = int(numero_b)
print("\n")
print("♦--------------------------------------------------------------♦","\n")

resto = numero_a % numero_b
print(f"• El resto de su divición es: {resto}\n")

print("♦--------------------------------------------------------------♦","\n")