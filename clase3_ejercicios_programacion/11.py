# Elio Yilali
# Comición 101
# Ejercicio: 11 tercera clase
#Pedir al usuario el ingreso de una nota. La misma debe estar comprendida entre 1 y 10 inclusive.
nota = input("ingrese una nota: ")
nota = float(nota)

if nota >= 1 and nota <=10:
    print("nota valida")
else:
    print("nota NO valida")