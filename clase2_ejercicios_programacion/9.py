# Elio Yilali
# Comición 101
# Ejercicio: 09 segunda clase
#Los argentinos nativos y por opción desde los dieciséis (16) años y los argentinos naturalizados desde los dieciocho (18) años 
# están habilitados a votar. A partir del ingreso de la edad del usuario y el estado (si es naturalizado o nativo), se deberá
# informar si es o no posible que la persona concurra a votar en base a la información suministrada.
print("\n")
print("♦-----------------------------------------------------------------------------♦","\n")
edad = input("• Por favor ingrese su edad: ")
edad = int(edad)
estado = input("• Por favor ingrese su estado (si es naturalizado o nativo):")
print("\n")
if edad >= 16 and estado == "Nativo":
    print("• Usted puede votar.")
elif edad >=18 and estado == "Naturalizado":
    print("• Usted puede votar.")
else:
    print("• Usted NO puede votar.")

print("\n")
print("♦-----------------------------------------------------------------------------♦","\n")