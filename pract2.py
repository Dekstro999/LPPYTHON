# https://github.com/Dekstro999/LPPYTHON
import random

def intEntero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Entrada invalida")

def floatNumero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")


def si_no():
    print("1. Si")
    print("2. No")
    opc=intEntero("")  
    return opc==1


def numeros_aleatorios(cantidad, minimo, maximo):
    return [random.randint(minimo, maximo) for _ in range(cantidad)]

def par_o_impar(numeros):
    for numero in numeros:
        if numero % 2 == 0:
            print(f"{numero} es Par")
        else:
            print(f"{numero} es Impar")
def contar_sumar_par_impar(numeros):
    pares = [num for num in numeros if num % 2 == 0]
    impares = [num for num in numeros if num % 2 != 0]

    cantidad_pares = len(pares)
    cantidad_impares = len(impares)
    
    suma_pares = sum(pares)
    suma_impares = sum(impares)

    return cantidad_pares, cantidad_impares, suma_pares, suma_impares


def tabla_multiplicar(numero):
    if 1 <= numero <= 20:
        for i in range(1, 11):
            print(f"{numero} * {i} = {numero * i}")
    else:
        print("Número fuera de rango. Debe estar entre 1 y 20.")


def leer_calificacion():
    while True:
        try:
            calificacion = float(input("Ingrese la calificación (0-100): "))
            if 0 <= calificacion <= 100:
                if calificacion >= 60:
                    print("Aprobado")
                else:
                    print("Reprobado")
                break
            else:   
                print("Error: La calificación debe estar entre 0 y 100.")
        except ValueError:
            print("Error: Entrada inválida. Ingrese un número.")

def suma_media():
    numeros = []
    while True:
        numero = intEntero("Ingrese un número entero mayor que 0 (0 para terminar): ")
        if numero == 0:
            break
        elif numero > 0:
            numeros.append(numero)
        else:
            print("El número debe ser mayor que 0.")
    
    if numeros:
        suma = sum(numeros)
        media = suma / len(numeros)
        print(f"\nSuma de los números: {suma}")
        print(f"Media de los números: {media}")
    else:
        print("\nNo se ingresaron números válidos.")
        
def promedio_3op():
    intentos = 0
    max_intentos = 3
    while intentos < max_intentos:
            promedio = floatNumero("Ingrese el promedio de la materia (0-100): ")
            if 0 <= promedio <= 100:
                if promedio >= 60:
                    print("¡Felicidades! Has aprobado la materia. Puedes continuar al siguiente semestre.")
                    break
                else:
                    intentos += 1
                    if intentos < max_intentos:
                        print(f"Has reprobado. Te quedan {max_intentos - intentos} intentos.")
                    else:
                        print("Has reprobado 3 veces. Es baja académica.")
            else:
                print("Error: El promedio debe estar entre 0 y 100.")

def numeros_mayor_menor():
    numeros = []
    while True:
        numero = floatNumero("Ingrese un número (o '0' para detener): ")
        
        if numero == 0:
            break
        
        numeros.append(numero)

    if len(numeros) == 0:
        print("No se ingresaron números.")
        return


    print(f"Suma de los números: {sum(numeros)}")
    print(f"Media de los números: {sum(numeros)/ len(numeros)}")
    print(f"Mayor número: {max(numeros)}")
    print(f"Menor número: {min(numeros)}")

def generar_impares(cantidad_maxima=25, rango_minimo=10, rango_maximo=60):
    impares = [num for num in range(rango_minimo, rango_maximo + 1) if num % 2 != 0]
    if len(impares) < cantidad_maxima:
        cantidad_maxima = len(impares)
    
    numeros_seleccionados = random.sample(impares, cantidad_maxima)
    
    return numeros_seleccionados

def calcular_media(numeros):
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)

def leer_validar_rango():
    rango_min = floatNumero("Ingrese el límite inferior del rango: ")
    rango_max = floatNumero("Ingrese el límite superior del rango: ")
    
    if rango_min > rango_max:
        print("El límite inferior debe ser menor o igual al límite superior.")
        return

    numeros = []
    
    while True:
        numero = floatNumero(f"Ingrese un número dentro del rango [{rango_min}, {rango_max}] (o '0' para detener): ")
        
        if numero == 0:
            break
        elif rango_min <= numero <= rango_max:
            numeros.append(numero)
        else:
            print(f"El número debe estar dentro del rango [{rango_min}, {rango_max}].")
    
    if numeros:
        cantidad_numeros = len(numeros)
        promedio = sum(numeros) / cantidad_numeros
        print(f"\nCantidad de números ingresados: {cantidad_numeros}")
        print(f"Promedio de los números: {promedio}")
    else:
        print("\nNo se ingresaron números válidos.")

def obtener_base_altura():
    base = floatNumero("Ingrese la base del triángulo: ")
    altura = floatNumero("Ingrese la altura del triángulo: ")
    return base, altura

def numero_rango(minimo, maximo):
    while True:
        numero = floatNumero(f"Ingrese un numero entre {minimo} y {maximo}")
        if minimo <= numero <= maximo:
            print(f"El número {numero} está dentro del rango ({minimo}, {maximo}).")
            return numero
        else:
            print(f"El número {numero} no está dentro del rango ({minimo}, {maximo}).")





while True:
    print("\nMenu:")
    print(" 1. 40 numeros aleatorios (0-200)")
    print(" 2. Tabla de multiplicar (1-20)")
    print(" 3. Calificacion (0-100)")
    print(" 4. Leer n cantidad ")
    print(" 5. Promedio (3 oportunidades) ")
    print(" 6. Leer n cantidad (minimo/maximo)")
    print(" 7. impares y media")
    print(" 8. Leer y validar número en rango")
    print(" 9. Area Triangulo")
    print("10. Numero en rango")
    print("11. Salir")

    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        numeros = numeros_aleatorios(40, 0, 200)
        
        par_o_impar(numeros)
        
        cantidad_pares, cantidad_impares, suma_pares, suma_impares = contar_sumar_par_impar(numeros)
        
        # Desplegar resultados
        print("\nCantidad de números pares:", cantidad_pares)
        print("Cantidad de números impares:", cantidad_impares)
        print("Suma de números pares:", suma_pares)
        print("Suma de números impares:", suma_impares)
        print(numeros)
        
        
        pass
    elif opcion == "2":
        
        tabla_multiplicar(intEntero("Ingrese un número entre 1 y 20 para la tabla de multiplicar: "))
        pass
    elif opcion == "3":
        leer_calificacion()
        pass
    elif opcion == "4":
        suma_media()
        pass
    elif opcion == "5":
        promedio_3op()
        pass
    elif opcion == "6":
        numeros_mayor_menor()
        pass
    elif opcion == "7":
        numeros_impares = generar_impares()
        print(f"Números impares generados: {numeros_impares}")
                
        print(f"Media de los números impares: {calcular_media(numeros_impares)}")
        
        pass
    elif opcion == "8":
        leer_validar_rango()
        pass
    elif opcion == "9":
        base, altura = obtener_base_altura()
        area = (base*altura)/2
        if area is not None:
            print(f"\nEl área del triángulo es: {area}")
        pass
    elif opcion == "10":
        numero_rango(1,20)
        pass
    elif opcion == "11": #salir
        break
    else:
        print("Opcion invalida. Intente de nuevo.")
        
        