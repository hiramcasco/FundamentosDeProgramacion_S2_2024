# Ejercicio 1: Árbol de navidad
# Lea un numero n e Imprime un árbol de navidad de n filas formado con *

# n = int(input())
# print(f"Arbol de {n} filas")
# for fila in range(1,n+1):
#     flores = (2*fila-1)*"*"
#     print(flores.center(2*n," "))

#Ejercicio 2: Fibonacci
#Lea un numero n e imprima la sucesión de Fibonacci menor o igual a n

# n = int(input())
# fibo = []
# a = 0
# while a <= n:
#     fibo.append(a)
#     if len(fibo) == 1: a = 1
#     else:
#         a = a + fibo[len(fibo)-2]

# for index in range(len(fibo)):
#     if index > 0:
#         answer += ", " + str(fibo[index])
#     else:
#         answer = str(fibo[index])

# print(answer)

# Ejercicio 3: MCD - Euclides
# Lea dos numeros a y b.  muestre en pantalla el MCD de a y b (usando el algoritmo de euclides)

# a = [int(input()),int(input())]
# r = 1
# while r != 0:
#     r = a[len(a)-2]%a[len(a)-1]
#     a.append(r)
# print(f"MCD={a[len(a)-2]}")

# Ejercicio 4: Escriba un programa que invierta los dígitos de un número entero introducido por teclado.

# num = int(input())
# if  num < 0:
#     mun = "-"
#     num = str(num)
#     for index in range(len(num)-1,0,-1):
#         mun += num[index]
# else:
#     mun = ""
#     num = str(num)
#     for index in range(len(num)-1,-1,-1):
#         mun += num[index]
# print(int(mun))