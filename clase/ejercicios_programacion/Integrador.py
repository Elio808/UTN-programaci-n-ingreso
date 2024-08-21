# Elio Yilali
# Comición 101
# Ejercicio: integrador primera clase
print("\n")
print("♦--------------------------------------------------------------------------------------------------------------------------♦","\n")
c_triangulo_superior = input("• Por favor, ingrese la medida de los centimetros del diágonal mayor (B,C): ")#ingreción de datos↓
c_triangulo_superior = float(c_triangulo_superior)
print("\n")
ancho = input("• Por favor, ingrese la medida de los centimetros de la varilla orizontal (D,C): ") #varilla orisontal
ancho = float(ancho)
print("\n")
c_triangulo_inferior = input("• Por favor, ingrese la medida de los centimetros del diágonal menor (D,A): ")
c_triangulo_inferior = float(c_triangulo_inferior)
print("\n")
print("♦--------------------------------------------------------------------------------------------------------------------------♦","\n")
#triángulo superior
c_triangulo_superior
b_triangulo_superior = ancho/2
a_triangulo_superior = ((c_triangulo_superior ** 2) - (b_triangulo_superior ** 2))** 0.5
#area triángulo superior
area_triangulo_superior = (b_triangulo_superior * a_triangulo_superior / 2) ** 2
area_total_triangulo_superior = area_triangulo_superior * 2
#triángulo inferior
c_triangulo_inferior
b_triangulo_inferior = ancho/2
a_triangulo_inferior = ((c_triangulo_inferior ** 2) - (b_triangulo_inferior ** 2))** 0.5
#area triángulo inferior
area_triangulo_inferior = (b_triangulo_inferior * a_triangulo_inferior / 2) ** 2
area_total_triangulo_inferior = area_triangulo_inferior * 2
#area de el cometa
area_cometa  =  area_total_triangulo_inferior + area_total_triangulo_superior       
#varilla vertical
varilla_vertical = a_triangulo_inferior + a_triangulo_superior      
#cola
porcentaje_cola = area_cometa / 100 * 10        
#area totla de el cometa
area_total_cometa = area_cometa + porcentaje_cola       
#producción en masa
produccion_masa_varilla = (ancho + varilla_vertical) * 10       
producion_masa_papel = area_total_cometa * 10
#de centimetos a metros
produccion_masa_varilla_metros = produccion_masa_varilla / 100     
producion_masa_papel_metros = producion_masa_papel / 100
#redodondeo
produccion_masa_varilla_metros = round(produccion_masa_varilla_metros, 2)
producion_masa_papel_metros = round(producion_masa_papel_metros, 2)
#resultado
print(f"• Se nesecitan {produccion_masa_varilla_metros} m de varillas para la producción en masa de 10 comentas.\n\n• Se nesecitan {producion_masa_papel_metros} m de papel para la producción en masa de 10 cometas.")
print("\n")
print("♦--------------------------------------------------------------------------------------------------------------------------♦","\n")
# La juguetería El MUNDO DE CHARLY nos encarga un programa para conocer qué cantidad de materiales 
# se necesita para la fabricación de distintos juguetes.

# CONFECCIÓN DE UN COMETA: 

# Medidas:
# AB = Diágonal mayor                                                               B
# DC = Diágonal menor                                                            D     C
# BD y BC = lados menores
# AD y AC = lados mayores                                                           A

# El usuario ingresará las medidas  BC, CD y DA.

# Detalles de construcción

# Debemos tener en cuenta que la estructura del cometa estará dada por un perímetro de varillas de plástico y los correspondientes entrecruces (DC y AB) del mismo material para mantener la forma del cometa.
# El cometa estará construido con papel de alta resistencia. La cola del mismo se construirá con el mismo papel que el cuerpo y representará un 10% adicional del necesario para el cuerpo.
# Necesitamos saber cuántos Mts de varillas de plástico y cuántos de papel son necesarios para la construcción en masa de 10 cometas. Tener en cuenta que los valores de entrada están expresados en Cms.