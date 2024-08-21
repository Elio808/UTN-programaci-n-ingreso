# Elio Yilali
# Comición 101
# Ejercicio: 05

# Realizar un programa que permita el ingreso de dos números. Calcular la suma, resta, multiplicación y división de los mismos. 
# Mostrar los resultados por pantalla. Utilizar una variable para mostrar el resultado (concatenar).
print("\n")
print("♦--------------------------------------------------------------♦","\n")

numero_a = input("• Por favor, ingrese un número: ")
numero_a = float(numero_a)
print("\n")

numero_b = input("• Por favor, ingrese nuevamente otro número: ")
numero_b = float(numero_b)
print("\n")
#suma
suma = numero_a + numero_b
#resta
resta = numero_a - numero_b
#multiplicación
multiplicacion = numero_a * numero_b
#divición
divicion = numero_a / numero_b
#resultado

print(f"• Suma: {suma}\n• Resta: {resta}\n• Multiplicación: {multiplicacion}\n• Divición: {divicion}\n")

print("♦--------------------------------------------------------------♦","\n")