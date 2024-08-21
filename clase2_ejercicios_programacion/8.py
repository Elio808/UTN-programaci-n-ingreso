# Elio Yilali
# Comición 101
# Ejercicio: 08 segunda clase
#A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parámetros:
# Menos de 160 cm: Base
# Entre 160 cm y 179 cm: Escolta
# Entre 180 cm y 199 cm: Alero
# 200 cm o más: Ala-Pívot o Pívot
print("\n")
print("♦-----------------------------------------------------------------------------♦","\n")
altura = input("• Por favor ingrese su altura en centimetros: ")
altura = float(altura)
print("\n")
if altura < 160:
    print("• Su posición a jugar es Base.")
elif altura >= 160 and altura <180:
    print("• Su posición a jugar es Escolta.")
elif altura >= 180 and altura < 200:
    print("• Su posición a jugar es Alero")
else:
    print("• Su posición a jugar es Ala-Pívot o Pívot.")
print("\n")
print("♦-----------------------------------------------------------------------------♦","\n")