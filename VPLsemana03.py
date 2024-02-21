#Ejercicio 4: Elemento central de tres números
"""Escribir un programa que lea tres números enteros, y muestre en pantalla el valor central.
Por ejemplo, si los números ingresados son 4, 1 y 3 (en cualquier orden), debe mostrarse en pantalla el 3.
Obs: se puede suponer que siempre se cargarán números enteros."""

"""a = int(input())
b = int(input())
c = int(input())

if ((a<=b) and (b<=c)) or ((a>=b) and (b>=c)):
    central = b
if ((b<=c) and (c<=a)) or ((b>=c) and (c>=a)):
    central = c
    joya = True
if ((c<=a) and (a<=b)) or ((c>=a) and (a>=b)):
    central = a

print(central)"""

#Ejercicio 5: Cuadrado de un número
"""Escribir un programa que reciba un número (el cual debería ser entero y positivo), y muestre en pantalla el
valor del cuadrado de dicho número. Si el número no es entero y positivo, debe indicarse con mensajes en pantalla
(dependiendo del caso). Si el número ingresado sobrepasa el valor de 10000, también se debe indicar con un mensaje
en pantalla."""

"""numero = float(input())

if numero < 10000:
    if numero > 0:
        if numero == round(numero):
            print(int(numero*numero))
        else: print("Error, el numero ingresado no es entero")
    else:
        if numero == round(numero): print("Error, el numero ingresado no es positivo")
        else: print("Error, el numero ingresado no es entero ni positivo")
else: print("Error, el numero ingresado es muy grande")"""
