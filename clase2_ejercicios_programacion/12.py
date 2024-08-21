# Elio Yilali
# Comición 101
# Ejercicio: 12 segunda clase
#Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
# 6, 7, 8, 9 y 10  ---> Promoción directa, la nota es ...
# 4 y 5                ---> Aprobado, la nota es ...
print("\n")
print("♦-----------------------------------------------------------------------------♦","\n")
import random
numero_aleatorio = random.randint (1, 10)
if numero_aleatorio >= 6 and numero_aleatorio <= 10:
    print(f"• Promoción directa, la nota es {numero_aleatorio}")
elif numero_aleatorio  == 4 or numero_aleatorio == 5:
    print(f"• Aprobado, la not es {numero_aleatorio}")
else:
    print(f"• Desaprobado, la nota es {numero_aleatorio}")
print("\n")
print("♦-----------------------------------------------------------------------------♦","\n")