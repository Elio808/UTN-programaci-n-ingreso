
# El dueño de una tienda dedicada a la compra/venta de cartas de Yu-Gi-Oh, 
# desea ingresar en el sistema las ventas realizadas en el día de la fecha y a partir de ello, conocer ciertos datos en base a las cartas que se vendieron.

# Deberemos desarrollar un sistema para que el dueño pueda ingresar la siguiente información hasta que él lo decida.

# Nombre de carta
# Precio (número positivo, no puede ser mayor a 200000)
# Tipo (Mágica, Monstruo, Trampa)
# Rareza (Rara, Super Rara, Ultra Rara)

# Una vez finalizado el ingreso de datos se desea conocer:

# a.Cantidad de cartas de rareza Ultra raras cuyo precio oscile en 50000 y 80000 y sea de tipo Mágica o Trampa.
# b.El nombre y tipo de la carta con menor precio de la rareza Rara.
# c.El porcentaje de rara, super rara y ultra rara hay sobre el total
# d.Determinar el precio promedio por cada tipo de carta
# e.Determinar cuál fue el tipo de carta mas vendida

nombre_carta = 0
precio = 0
tipo = 0
rareza = 0

nombre_carta_menor_precio = 0
tipo_carta_menor_precio = 0

menor_precio = 0

contador_carta_rara = 0
contador_carta_super_rara = 0
contador_carta_ultra_rara = 0
contador_oscila_ultrararo = 0

contador_carta_magica = 0
contador_carta_monstruo = 0
contador_carta_trampa = 0

acumulador_carta_magica = 0
acumulador_carta_monstruo = 0
acumulador_carta_trampa = 0

tipo_carta_mas_vendida = 0

contador_general = 0
bandera_menor_precio = False
flag = 'si'

while flag == 'si':
    #region ingreso de datos y validación
    nombre_carta = input('ingrese nombre de la carta: ')
    precio = input('ingrese precio de la carta: ')
    precio = float(precio)
    while precio < 0 or precio > 200000:
        precio = input('el precio debe ser positivo y no mayor a 200000: ')
        precio = float(precio)

    tipo = input('ingrese tipo de carta (Mágica, Monstruo, Trampa): ')
    while tipo != 'Mágica' and tipo != 'Monstruo' and tipo != 'Trampa':
        tipo = input('porfavor ingrese uno de los siguientes tipos (Mágica, Monstruo, Trampa): ')
    rareza = input('ingrese rareza de la carta (Rara, Super Rara, Ultra Rara): ')
    while rareza != 'Rara' and rareza != 'Super Rara' and rareza != 'Ultra Rara':
        rareza = input('porfavor ingrese una de las siguientes rarezas (Rara, Super Rara, Ultra Rara): ')
    #endregion

    #region a.Cantidad de cartas de rareza Ultra raras cuyo precio oscile en 50000 y 80000 y sea de tipo Mágica o Trampa.
    if rareza == 'Ultra Rara':
        if precio > 50000 and precio < 80000 and (tipo == 'Mágica' or tipo == 'Trampa'):
            contador_oscila_ultrararo += 1
        contador_carta_ultra_rara += 1
    elif rareza == 'Super Rara':
        contador_carta_super_rara += 1
    #endregion
    #region b.El nombre y tipo de la carta con menor precio de la rareza Rara.
    else:
        if precio < menor_precio or bandera_menor_precio == False:
            menor_precio = precio
            nombre_carta_menor_precio = nombre_carta
            tipo_carta_menor_precio = tipo
            bandera_menor_precio == True
        contador_carta_rara += 1
    #endregion
    
    #region d.Determinar el precio promedio por cada tipo de carta
    if tipo == 'Mágica':
        acumulador_carta_magica += precio
        contador_carta_magica += 1
    elif tipo == 'Monstruo':
        acumulador_carta_monstruo += precio
        contador_carta_monstruo += 1
    elif tipo == 'Trampa':
        acumulador_carta_trampa += precio
        contador_carta_trampa += 1
    #endregion

    contador_general += 1
    flag = input('desea continuar si/no: ')

#a.Cantidad de cartas de rareza Ultra raras cuyo precio oscile en 50000 y 80000 y sea de tipo Mágica o Trampa.
mensaje = f'cantidad de cartas que Ultra raras cuyo precio \noscilen en 50000 y 80000 de tipo Mágica o Trampa es: {contador_oscila_ultrararo}\n'

 
 
 
 
# El dueño de una tienda dedicada a la compra/venta de cartas de Yu-Gi-Oh, 
# desea ingresar en el sistema las ventas realizadas en el día de la fecha y a partir de ello, conocer ciertos datos en base a las cartas que se vendieron.

# Deberemos desarrollar un sistema para que el dueño pueda ingresar la siguiente información hasta que él lo decida.

# Nombre de carta
# Precio (número positivo, no puede ser mayor a 200000)
# Tipo (Mágica, Monstruo, Trampa)
# Rareza (Rara, Super Rara, Ultra Rara)

# Una vez finalizado el ingreso de datos se desea conocer:

# a.Cantidad de cartas de rareza Ultra raras cuyo precio oscile en 50000 y 80000 y sea de tipo Mágica o Trampa.
# b.El nombre y tipo de la carta con menor precio de la rareza Rara.
# c.El porcentaje de rara, super rara y ultra rara hay sobre el total
# d.Determinar el precio promedio por cada tipo de carta
# e.Determinar cuál fue el tipo de carta mas vendida

nombre_carta = 0
precio = 0
tipo = 0
rareza = 0

nombre_carta_menor_precio = 0
tipo_carta_menor_precio = 0

menor_precio = 0

contador_carta_rara = 0
contador_carta_super_rara = 0
contador_carta_ultra_rara = 0
contador_oscila_ultrararo = 0

contador_carta_magica = 0
contador_carta_monstruo = 0
contador_carta_trampa = 0

acumulador_carta_magica = 0
acumulador_carta_monstruo = 0
acumulador_carta_trampa = 0

tipo_carta_mas_vendida = 0

contador_general = 0
bandera_menor_precio = False
flag = 'si'

while flag == 'si':
    #region ingreso de datos y validación
    nombre_carta = input('ingrese nombre de la carta: ')
    precio = input('ingrese precio de la carta: ')
    precio = float(precio)
    while precio < 0 or precio > 200000:
        precio = input('el precio debe ser positivo y no mayor a 200000: ')
        precio = float(precio)

    tipo = input('ingrese tipo de carta (Mágica, Monstruo, Trampa): ')
    while tipo != 'Mágica' and tipo != 'Monstruo' and tipo != 'Trampa':
        tipo = input('porfavor ingrese uno de los siguientes tipos (Mágica, Monstruo, Trampa): ')
    rareza = input('ingrese rareza de la carta (Rara, Super Rara, Ultra Rara): ')
    while rareza != 'Rara' and rareza != 'Super Rara' and rareza != 'Ultra Rara':
        rareza = input('porfavor ingrese una de las siguientes rarezas (Rara, Super Rara, Ultra Rara): ')
    #endregion

    #region a.Cantidad de cartas de rareza Ultra raras cuyo precio oscile en 50000 y 80000 y sea de tipo Mágica o Trampa.
    if rareza == 'Ultra Rara':
        if precio > 50000 and precio < 80000 and (tipo == 'Mágica' or tipo == 'Trampa'):
            contador_oscila_ultrararo += 1
        contador_carta_ultra_rara += 1
    elif rareza == 'Super Rara':
        contador_carta_super_rara += 1
    #endregion
    #region b.El nombre y tipo de la carta con menor precio de la rareza Rara.
    else:
        if precio < menor_precio or bandera_menor_precio == False:
            menor_precio = precio
            nombre_carta_menor_precio = nombre_carta
            tipo_carta_menor_precio = tipo
            bandera_menor_precio == True
        contador_carta_rara += 1
    #endregion
    
    #region d.Determinar el precio promedio por cada tipo de carta
    if tipo == 'Mágica':
        acumulador_carta_magica += precio
        contador_carta_magica += 1
    elif tipo == 'Monstruo':
        acumulador_carta_monstruo += precio
        contador_carta_monstruo += 1
    elif tipo == 'Trampa':
        acumulador_carta_trampa += precio
        contador_carta_trampa += 1
    #endregion

    contador_general += 1
    flag = input('desea continuar si/no: ')

#a.Cantidad de cartas de rareza Ultra raras cuyo precio oscile en 50000 y 80000 y sea de tipo Mágica o Trampa.
mensaje = f'cantidad de cartas que Ultra raras cuyo precio \noscilen en 50000 y 80000 de tipo Mágica o Trampa es: {contador_oscila_ultrararo}\n'

#b.El nombre y tipo de la carta con menor precio de la rareza Rara.
if bandera_menor_precio == True:
    mensaje += f'carta Rara con menor precio: {nombre_carta_menor_precio}\n'
    mensaje += f'tipo de carta rara con menor precio: {tipo_carta_menor_precio}\n'
else:
    mensaje += 'no se ingresó ninguna carta Rara para calcular el minimo'

# c.El porcentaje de rara, super rara y ultra rara hay sobre el total
if contador_carta_rara > 0:
    porcentaje_carta_rara = contador_carta_rara * 100 / contador_general
    mensaje += f'el porcentaje de cartas raras es: {round(porcentaje_carta_rara)}%\n'
if contador_carta_super_rara > 0:
    porcentaje_carta_super_rara = contador_carta_super_rara * 100 / contador_general
    mensaje += f'el porcentaje de cartas super raras es: {round(porcentaje_carta_super_rara)}%\n'
if contador_carta_ultra_rara > 0:
    porcentaje_carta_ultra_rara = contador_carta_ultra_rara * 100 / contador_general
    mensaje += f'el porcentaje de cartas ultra raras es: {round(porcentaje_carta_ultra_rara)}%\n'

#d.Determinar el precio promedio por cada tipo de carta
if acumulador_carta_magica > 0:
    promedio_carta_magica = acumulador_carta_magica / contador_carta_magica
    mensaje += f'el precio promedio de cartas tipo magica: {promedio_carta_magica}\n'
if acumulador_carta_monstruo > 0:
    promedio_carta_monstruo = acumulador_carta_monstruo / contador_carta_monstruo
    mensaje += f'el precio promedio de cartas tipo monstruo: {promedio_carta_monstruo}\n'
if acumulador_carta_trampa > 0:
    promedio_carta_trampa = acumulador_carta_trampa / contador_carta_trampa
    mensaje += f'el precio promedio de cartas tipo trampa: {promedio_carta_trampa}\n'

#e.Determinar cuál fue el tipo de carta mas vendida

if contador_carta_magica > contador_carta_monstruo and contador_carta_magica > contador_carta_trampa:
    tipo_carta_mas_vendida = 'Mágica'
elif contador_carta_monstruo > contador_carta_magica and contador_carta_monstruo > contador_carta_trampa:
    tipo_carta_mas_vendida = 'Monstruo'
elif contador_carta_trampa > contador_carta_magica and contador_carta_trampa > contador_carta_monstruo:
    tipo_carta_mas_vendida = 'Trampa'
mensaje += f'el tipo de carta mas vendida fue {tipo_carta_mas_vendida}'

print(mensaje)