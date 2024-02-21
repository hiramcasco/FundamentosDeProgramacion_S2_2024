#Ejercicio 4: Elemento central de tres números

"""Escribir un programa que lea tres números enteros, y muestre en pantalla el valor central.
Por ejemplo, si los números ingresados son 4, 1 y 3 (en cualquier orden), debe mostrarse en pantalla el 3.
Obs: se puede suponer que siempre se cargarán números enteros."""

a = int(input())
b = int(input())
c = int(input())

if ((a<=b) and (b<=c)) or ((a>=b) and (b>=c)):
    central = b
if ((b<=c) and (c<=a)) or ((b>=c) and (c>=a)):
    central = c
    joya = True
if ((c<=a) and (a<=b)) or ((c>=a) and (a>=b)):
    central = a

print(central)