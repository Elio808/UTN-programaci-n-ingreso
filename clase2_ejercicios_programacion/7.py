# Elio Yilali
# Comición 101
# Ejercicio: 07 segunda clase
#Pedirle al usuario su edad, determinar si es mayor (18 años o más), niño/a (menor de 10), pre-adolescente 
# (edad entre 10 y 13 años inclusive) o adolescente (edad entre 13 y 17 años).
print("\n")
print("♦-----------------------------------------------------------------------------♦","\n")
edad = input("• Por favor ingrese su edad: ")
edad = int(edad)
print("\n")
if edad >= 18:
    print("• Usted es mayor de edad.")
elif edad > 13 and edad < 18:
    print("• Usted es un adolecente.")
elif edad > 9 and edad <= 13:
    print("• Usted es un pre-adolecente.")
else:
    print("• Usted es un niño.")

print("\n")
print("♦-----------------------------------------------------------------------------♦","\n")