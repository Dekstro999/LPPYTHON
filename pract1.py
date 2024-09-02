import random


def intEntero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Entrada invalida")

def calcular_promedio():
    saltos=1
    while True:
        try:
            cal1 = float(input("Ingrese la primera calificacion: "))
            cal2 = float(input("Ingrese la segunda calificacion: "))
            cal3 = float(input("Ingrese la tercera calificacion: "))

            promedio = (cal1 + cal2 + cal3) / 3

            if promedio < 0 or promedio > 100:
                print("Error en el promedio. Intente de nuevo.")
            else:
                break 

        except ValueError:
            print("Entrada no valida. Por favor, ingrese numeros.")
    saltos+=1        
    if promedio >=80:
        saltos+=1
        if promedio>=98:
            saltos+=1
            if promedio>100:
                saltos+=1
                print("error")
            else:
                
                print("Excelente")
        elif promedio >=90:
            print("Muy bien")
        else:
            saltos+=1
            print("Bien")
            
    elif promedio >=60:
        saltos+=1
        if promedio>=70:
            saltos+=1
            print("Regular")
        else:
            saltos+=1
            print("Sufivciente")
    elif promedio>=30:
        saltos+=1
        print("Extraordinario")
    else:
        saltos+=1
        print("Repetir")
    print(promedio," saltos  ",saltos)





def salario():
    horas_trabajadas = float(input("Ingrese las horas trabajadas en la semana: "))
    salario_por_hora = float(input("Ingrese el salario por hora: "))

    jornada_normal = 40
    salario_normal = 0
    salario_extra = 0

    if horas_trabajadas <= jornada_normal:
        salario_normal = horas_trabajadas * salario_por_hora
    else:
        salario_normal = jornada_normal * salario_por_hora

        horas_extra = horas_trabajadas - jornada_normal
        if horas_extra <= 9:
            salario_extra = horas_extra * salario_por_hora * 2
        else:
            salario_extra = (9 * salario_por_hora * 2) + ((horas_extra - 9) * salario_por_hora * 3)

    salario_total = salario_normal + salario_extra

    print(f"\nSalario por hora: ${salario_por_hora:.2f}")
    print(f"Horas trabajadas: {horas_trabajadas}")
    print(f"Salario normal: ${salario_normal:.2f}")
    print(f"Salario extra: ${salario_extra:.2f}")
    print(f"Salario total: ${salario_total:.2f}")

def llamada_telefonica():
    minutos = float(input("Ingrese la duracion de la llamada en minutos: "))
    print("\nTipo de llamada:")
    print("1. Llamada Local")
    print("2. Llamada Nacional")
    print("3. Llamada Internacional")
    tipo_llamada = intEntero("Seleccione el tipo de llamada (1-3): ")

    subtotal = 0

    if tipo_llamada == 1:
        # Llamada Local
        subtotal = 3.00
    elif tipo_llamada == 2:
        # Llamada Nacional
        if minutos <= 3:
            subtotal = 7.00
        else:
            subtotal = 7.00 + (minutos - 3) * 2.00
    elif tipo_llamada == 3:
        # Llamada Internacional
        if minutos <= 2:
            subtotal = 9.00
        else:
            subtotal = 9.00 + (minutos - 2) * 4.00
    else:
        print("Tipo de llamada no valido.")
        return

    iva = subtotal * 0.16
    total = subtotal + iva

    print(f"\nSubtotal: ${subtotal:.2f}")
    print(f"IVA (16%): ${iva:.2f}")
    print(f"Total: ${total:.2f}")

def consumo_agua():
    consumidos = float(input("Ingrese la cantidad de M3 de agua consumidos: "))

    subtotal = 0

    if consumidos <= 4:
        subtotal = 50.00  # Rango 1
    elif consumidos <= 15:
        subtotal = 50.00 + (consumidos - 4) * 8.00  # Rango 2
    elif consumidos <= 50:
        subtotal = 50.00 + (15 - 4) * 8.00 + (consumidos - 15) * 10.00  # Rango 3
    else:
        subtotal = 50.00 + (15 - 4) * 8.00 + (50 - 15) * 10.00 + (consumidos - 50) * 11.00  # Rango 4

    iva = subtotal * 0.16
    total = subtotal + iva

    print(f"\nSubtotal: ${subtotal:.2f}")
    print(f"IVA (16%): ${iva:.2f}")
    print(f"Total a pagar: ${total:.2f}")

def promedio_examenes():
    examenes = []
    for i in range(5):
        calificacion = float(input(f"Ingrese la calificacion del examen {i + 1}: "))
        examenes.append(calificacion)

    # Anular mas bajA
    menor = min(examenes)
    examenes.remove(menor)

    promedio_final = sum(examenes) / len(examenes)

    print(f"\nmenor({menor})") #depuracion 
    print(f"El promedio final de la materia es: {promedio_final:.2f}")

def eleccionChinchanpu():
    print("Color de etiqueta:")
    print("1. Roja")
    print("2. Verde")
    print("3. Amarilla")
    etiqueta=intEntero("")
    return etiqueta

def chinchampuAnidada():
    opc = ["Piedra", "Papel", "Tijera"]
    
    jugador = input("Elige: Piedra, Papel o Tijera: ").capitalize()
    
    pc = random.choice(opc)
    
    print(f"\nTu elegiste: {jugador}")
    print(f"La pc eligio: {pc}")
    
    if jugador == pc:
        print("¡Es un empate!")
    elif jugador == "Piedra":
        if pc == "Tijera":
            print("WIN!")
        else:
            print("LOSER")
    elif jugador == "Papel":
        if pc == "Piedra":
            print("WIN!")
        else:
            print("LOSER")
    elif jugador == "Tijera":
        if pc == "Papel":
            print("WIN!")
        else:
            print("LOSER")
    else:
        print("OPCION NO VALIDA***")


def chinchampuMultiple():
    opciones = ["Piedra", "Papel", "Tijera"]
    
    jugador = input("Elige: Piedra, Papel o Tijera: ").capitalize()
    
    pc = random.choice(opciones)
    
    print(f"\nTu elegiste: {jugador}")
    print(f"La pc eligio: {pc}")
    
    if jugador == pc:
        print("¡Es un empate!")
    elif (jugador == "Piedra" and pc == "Tijera") or \
            (jugador == "Papel" and pc == "Piedra") or \
            (jugador == "Tijera" and pc == "Papel"):
        print("¡Ganaste!")
    elif (jugador == "Piedra" and pc == "Papel") or \
            (jugador == "Papel" and pc == "Tijera") or \
            (jugador == "Tijera" and pc == "Piedra"):
        print("Perdiste.")
    else:
        print("Opcion no valida. Intenta de nuevo.")

def si_no():
    print("1. Si")
    print("2. No")
    opc=intEntero("")
    if opc==1:
        return True
    else:
        return False


def electronica():
    print("Seleccione el producto que desea comprar:")
    print("1. Computadora")
    print("2. Television")
    print("3. Consola de Videojuegos")
    opcion= intEntero("")
    
    precio_total = 0
    
    if opcion == 1:
        precio_computadora = float(input("Ingrese el precio de la computadora: $ "))
        precio_total += precio_computadora * 0.95  
        print("Descuento aplicado del 5%")
        
        print("¿Desea comprar una impresora junto con la computadora? ")
        if si_no():
            precio_impresora = float(input("Ingrese el precio de la impresora: $ "))
            precio_total += precio_impresora * 0.90  
            print("Descuento aplicado del 10%")
    
    elif opcion == 2:
        precio_television = float(input("Ingrese el precio de la television: $ "))
        precio_total += precio_television * 0.93 
        print("Descuento aplicado del 7%")
        
        print("¿Desea comprar una barra de sonido junto con la television? ")
        if si_no:
            precio_barra_sonido = float(input("Ingrese el precio de la barra de sonido: $ "))
            precio_total += precio_barra_sonido * 0.85  
            print("Descuento aplicado del 15%")
    
    elif opcion == 3:
        precio_consola = float(input("Ingrese el precio de la consola de videojuegos: $ "))
        precio_total += precio_consola * 0.90  
        print("Descuento aplicado del 10%")
        
        print("¿Desea comprar un juego junto con la consola? ")
        if si_no:
            precio_juego = float(input("Ingrese el precio del juego: $ "))
            precio_total += precio_juego * 0.80 
            print("Descuento aplicado del 20%")
    
    else:
        print("Opcion no valida. Intente de nuevo.")
        return

    print(f"\nEl precio total a pagar es: ${precio_total:.2f}")

def ropa():

    def etiquetaR():
        print("Color de etiqueta:")
        print("1. Roja")
        print("2. Verde")
        print("3. Amarilla")
        etiqueta=intEntero("")
        return etiqueta

    print("Seleccione la temporada:")
    print("1. Verano")
    print("2. Invierno")
    print("3. Primavera/Otoño")
    
    temporada= intEntero("")

    precio_original = float(input("Ingrese el precio del producto: $ "))
    
    descuento = 0

    if temporada == 1:  # Verano
        descuento = 0.20  # 20%
        print("Descuento del 20%")

    elif temporada == 2:  # Invierno
        etiqueta = etiquetaR()
        if etiqueta == 1:
            descuento = 0.30  # 30%
            print("Descuento del %")

        elif etiqueta == 2:
            descuento = 0.15  # 15%
            print("Descuento del 15%")


    elif temporada == 2:  # Primavera/Otoño
        etiqueta = etiquetaR()
        if etiqueta == 3:
            descuento = 0.10  # 10%
            print("Descuento del 10%")

    else:
        print("Temporada no valida.")
        descuento = 0

    total = precio_original * (1 - descuento)

    print(f"\nTotal a pagar: $ {total:.2f}")

def restaurante():

    def menuS():
        print("Menu a elegir")
        print("1. Menu del dia")
        print("2. Menu infantil")
        print("3. Menu vegetariano")
        print("4. Menu del chef")
        opMenu=intEntero("")
        return opMenu
    
    print("Seleccione el dia de la semana:")
    print("1. Lunes")
    print("2. Martes")
    print("3. Miercoles")
    print("4. Jueves")
    print("5. Viernes")
    print("6. Sabado")
    print("7. Domingo")
    
    dia = intEntero("")
    
    precio_original = float(input("Ingrese el precio del menu: $ "))
    
    descuento = 0

    if dia == 1:  # Lunes
        menu = menuS()
        if menu == 1:
            descuento = 0.10  # 10% de descuento
            print("Descuento del 10%")

    elif dia == 2:  # Martes
        menu = menuS()
        if menu == 2:
            descuento = 0.20  # 20% de descuento
            print("Descuento del 20%")

    elif dia == 3:  # Miercoles
        menu = menuS()
        if menu == 3:
            descuento = 0.15  # 15% de descuento
            print("Descuento del 15%")

    elif dia == 4:  # Jueves
        menu = menuS()
        if menu == 4:
            descuento = 0.05  # 5% de descuento
            print("Descuento del 5%")

    elif dia == 5:  # Viernes
        menu = menuS()
        if menu == 1:
            descuento = 0.05  # 5% de descuento
            print("Descuento del 5%")

    elif dia in [6,7]:  # Sabado y Domingo
        print("No hay descuentos disponibles durante el fin de semana.")
    else:
        print("Dia no valido")
        return

    total = precio_original * (1 - descuento)

    print(f"\nEl precio final a pagar es: ${total:.2f}")





while True:
    print("\nMenu:")
    print("1. Calificaciones")
    print("2. Salario")
    print("3. Llamada Telefonica")
    print("4. Consumo de Agua")
    print("5. Examenes")
    print("6. Chinchanpu (Anidadas)")
    print("7. Chinchanpu (Multiples)")
    print("8. Electronica")
    print("9. Ropa")
    print("10. Restaurante")
    print("11. Salir")

    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        calcular_promedio()
    elif opcion == "2":
        salario()
    elif opcion == "3":
        llamada_telefonica()
        pass
    elif opcion == "4":
        consumo_agua()
        pass
    elif opcion == "5":
        promedio_examenes()
        pass
    elif opcion == "6":
        chinchampuAnidada()
        pass
    elif opcion == "7":
        chinchampuMultiple()
        pass
    elif opcion == "8":
        electronica()
        pass
    elif opcion == "9":
        ropa()
        pass
    elif opcion == "10":
        restaurante()
        pass
    elif opcion == "11":
        break
    else:
        print("Opcion invalida. Intente de nuevo.")
