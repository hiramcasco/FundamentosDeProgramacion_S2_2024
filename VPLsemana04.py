# Ejercicio 1: Porcentaje de Edad
# Hacer un programa en Python que permita ingresar n edades de personas para luego hallar y mostrar
# el % de gente mayor de edad (≥ 18) y el % de menores de edad.

# n = int(input())
# mayores = 0
# menores = 0

# for _ in range(n):
#     edad = int(input())
#     if edad < 18: menores += 1
#     else: mayores += 1
# print(f"Mayores de edad: {(mayores/n*100):.0f}%    Menores de edad: {(menores/n*100):.0f}%")

# Ejercicio 2: La Ruleta
# Se ingresan por teclado 10 números cuyos valores corresponden a los de la ruleta (0,1,2,…,36),
# se pide hallar y mostrar por pantalla lo siguiente:
# a. Cantidad de números impares.     c. Cantidad de números que se encuentran en la 2º docena (13 al 24).
# b. Promedio de los números pares (no contar los ceros).         d. El número más grande.

# n_impares = 0
# n_pares = 0
# suma_pares = 0
# segunda_docena = 0
# mayor = 0

# for _ in range(10):
#     n = int(input())
#     if (n%2 == 0) and n != 0:
#         n_pares += 1
#         suma_pares += n
#     if n%2 != 0: n_impares += 1
#     if 13<=n and n<=24: segunda_docena += 1
#     if n > mayor: mayor = n

# print(f"a={n_impares}")
# print(f"b={(suma_pares/n_pares):.0f}")
# print(f"c={segunda_docena}")
# print(f"d={mayor}")

# Ejercicio 3: Contador de Vocales
# Hacer un programa en Python que solicite al usuario ingresar una palabra o frase y que imprima la
# cantidad de vocales de toda la cadena. (Considerar que se pueden ingresar vocales en mayúsculas o minúsculas)

# palabra = input()
# npalabra = 0
# for letter in palabra:
#     for vocal in "AaEeIiOoUu":
#         if letter == vocal: npalabra += 1
# print(f"La palabra ingresada contiene: {npalabra} vocales")

# Ejercicio 4: Es Primo
# Lea un numero n entero y positivo e imprima en pantalla si es o no un número primo. Si se ingresa un numero
# no positivo imprimir el mensaje: "El numero no es positivo"

# n = int(input())
# if n <= 0:
#     print("El numero no es positivo")
# else:
#     primo = "es"
#     if n==1:
#         primo = "no es"
#     for div in range(2,n):
#         if n%div == 0:
#             primo = "no es"
    
#     print(f"El {n} {primo} un numero primo")