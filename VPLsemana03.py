# Ejercicio 1: Determinar signo de un número
# Escribir un programa que reciba un número y determine si es positivo, negativo o cero.

# n = float(input())
# if n == 0: print("El numero ingresado es cero")
# if n > 0: print("El numero ingresado es positivo")
# if n < 0: print("El numero ingresado es negativo")

# Ejercicio 2: Cálculo de jornal
# Los empleados de una fábrica trabajan en dos turnos: diurno y nocturno. Se desea calcular el jornal diario
# de acuerdo con los siguientes puntos:                   a)La tarifa de las horas diurnas es de 10.000 Gs
# b)La tarifa de las horas nocturnas es de 20.000 Gs      c)Si es un domingo, el jornal aumenta en un 25%.

# dia = int(input())
# turno_d = int(input())
# turno_n = int(input())

# sueldo = 10000*turno_d +20000*turno_n
# if dia == 7: sueldo = int(sueldo*1.25)
# print(sueldo)

# Ejercicio 3: Determinar si un carácter es una letra
# Escribir un programa en Python que reciba un caracter e indique en pantalla si corresponde o no
# a una letra (sea minúscula o mayúscula).

# c = input()
# if c.isalpha():
#     if c.isupper(): print("El caracter ingresado es una letra (mayuscula)")
#     else: print("El caracter ingresado es una letra (minuscula)")
# else: print("El caracter ingresado NO corresponde a una letra")

# Ejercicio 4: Elemento central de tres números
# Escribir un programa que lea tres números enteros, y muestre en pantalla el valor central.
# Por ejemplo, si los números ingresados son 4, 1 y 3 (en cualquier orden), debe mostrarse en pantalla el 3.
# Obs: se puede suponer que siempre se cargarán números enteros.

# a = int(input())
# b = int(input())
# c = int(input())

# if ((a<=b) and (b<=c)) or ((a>=b) and (b>=c)):
#     central = b
# if ((b<=c) and (c<=a)) or ((b>=c) and (c>=a)):
#     central = c
#     joya = True
# if ((c<=a) and (a<=b)) or ((c>=a) and (a>=b)):
#     central = a

# print(central)

# Ejercicio 5: Cuadrado de un número
# Escribir un programa que reciba un número (el cual debería ser entero y positivo), y muestre en pantalla el
# valor del cuadrado de dicho número. Si el número no es entero y positivo, debe indicarse con mensajes en pantalla
# (dependiendo del caso). Si el número ingresado sobrepasa el valor de 10000, también se debe indicar con un mensaje
# en pantalla.

# numero = float(input())

# if numero < 10000:
#     if numero > 0:
#         if numero == round(numero):
#             print(int(numero*numero))
#         else: print("Error, el numero ingresado no es entero")
#     else:
#         if numero == round(numero): print("Error, el numero ingresado no es positivo")
#         else: print("Error, el numero ingresado no es entero ni positivo")
# else: print("Error, el numero ingresado es muy grande")

# Ejercicio 6: Número Binario
# Para este ejercicio podemos suponer que el usuario siempre ingresará un número entero de tres dígitos.
# Se debe determinar (y mostrar un mensaje en pantalla) si el número cargado representa a un número binario
# (para ello, debe estar compuesto por unos y/o ceros).

# numero = input()
# a = int(numero[0])
# b = int(numero[1])
# c = int(numero[2])

# if a*a == a and b*b == b and c*c == c: print("Es un numero binario")
# else: print("No es un numero binario")

# Ejercicio 7 (DESAFIO): Fecha del siguiente día
# Implementar un programa en Python en el que se ingresan tres variables: dia, mes y anho (en forma númerica)
# y devuelva la fecha del día siguiente (en formato dia/mes/anho). Se deben considerar los años bisiestos, cantidad
# de días de cada mes, etc. En caso de insertar números reales o fechas inválidas, indicar con un mensajede error.

# dia = float(input())
# mes = float(input())
# anho = float(input())
# error = False
# max_dia = 0

# if anho < 1 or anho - round(anho) !=0: error = True
# else:
#     if mes < 1 or mes > 12 or mes - round(mes) != 0: error = True
#     else:
#         if mes == 2:
#             if anho%4 == 0: max_dia = 29
#             else: max_dia = 28
#         for index in [1,3,5,7,8,10,12]:
#             if mes == index: max_dia = 31
#         for index in [4,6,9,11]:
#             if mes == index: max_dia = 30

#     if dia < 1 or dia > max_dia or dia - round(dia) != 0: error = True
#     else:
#         if dia < max_dia: print(f"{(dia+1):.0f}/{(mes):.0f}/{(anho):.0f}")
#         if dia == max_dia:
#             if mes == 12: print(f"{1}/{1}/{(anho+1):.0f}")
#             if mes < 12: print(f"{1}/{(mes+1):.0f}/{(anho):.0f}")

# if error == True: print("No es una fecha valida!!")