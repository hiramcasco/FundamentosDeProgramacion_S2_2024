# Ejercicio 1: Escriba una función para generar una serie de números primos comprendidos entres 2 y N

# def primo(n):
#     serie = ""
#     for numero in range(2,n+1):
#         primo = True
#         for divisor in range (2,numero):
#             if (numero % divisor == 0):
#                 primo = False
#                 break
#         if primo:
#             serie += f"{numero} "
#     return serie

# m = int(input())
# print(primo(m))

# Ejercicio 2: Contar Números Primos

# def esPrimo(num):
#     if num == 1 or num == 0: return False
#     for div in range(2,num):
#         if num%div == 0: return False
#     return True

# def Organizar(num,grup):
#     num = str(num)
#     floor = 0
#     respuesta = []
#     while grup <= len(num):
#         item = ""
#         for i in range(floor,grup,1):
#             item += num[i]
#         respuesta.append(int(item))
#         floor += 1
#         grup += 1
#     respuesta = list(set(respuesta))
#     return respuesta

# def Contador_no_primos(n,c):
#     contador = 0
#     if c > len(str(n)):
#         return -1
#     else:
#         for item in Organizar(n,c):
#             if not esPrimo(item): contador +=1
#     return contador

# n = int(input())
# c = int(input())
# print(f"Cantidad de no-primos de {c} digitos: {Contador_no_primos(n,c)}")

# Ejercicio 3: Calculo de Combinaciones

# def Factorial(n):
#     fact = 1
#     for a in range(1,n+1):
#         fact *= a
#     return fact

# def Combinacion(n,p):
#     comb = Factorial(n)/(Factorial(p)*Factorial(n-p))
#     return int(comb)

# opcion = input()
# if opcion == "1":
#     n = int(input())
#     print(Factorial(n))
# if opcion == "2":
#     n = int(input())
#     m = int(input())
#     print(Combinacion(n,m))

# Ejercicio 4: Cifrado de un Número
# def Validar():
#     n = m = o = 0
#     while n < 1 or n != int(n) or m != o:
#         n = input()
#         m = len(n)
#         n = float(n)
#         o = len(str(int(n)))
#     n = int(n)
#     return n

# def cifrar(num):
#     pin = str(num)
#     cifrado = ""
#     for digit in pin:
#         cifrado += str((int(digit)+7) % 10)
#     return int(cifrado)

# print(cifrar(Validar()))

# Ejercicio 5: Números amigos
# def Validar():
#     n = 0
#     while not 100 < n < 32000 or n != int(n):
#         n = float(input())
#     return int(n)

# def DivisoresPropios(n):
#     divisores = []
#     for div in range(1,n):
#         if n % div == 0: divisores.append(div)
#     return divisores

# def SonAmigos(a,b):
#     sumA = sumB = 0
#     DivA = DivisoresPropios(a)
#     DivB = DivisoresPropios(b)
#     for item in DivA: sumA += item
#     for item in DivB: sumB += item
#     if sumA == b and sumB == a: return True
#     else: return False

# a = Validar()
# b = Validar()
# if SonAmigos(a,b): print("Son numeros amigos")
# else: print("No son numeros amigos")

# Ejercicio 6: Impresión Triangulo Isósceles

# def TriISO(n):
#     arbol = """"""
#     for m in range(1,2*n,2):
#         guion = int(n - (m+1)/2)
#         if m != 2*n-1 : arbol += (guion*"_"+m*"*"+"\n")
#         else: arbol += (guion*"_"+m*"*")
#     return(arbol)

# n = int(input())
# print(TriISO(n))

#Ejercicio 7: Impresión Diamante
# def diamante(n):
#     di = """"""
#     for fila in range(1,2*n,2):
#         renglones = int(n - (fila+1)/2)
#         if fila != 2*n-1: di += renglones*"-" + fila*"*" + "\n"
#         else: di += renglones*"-" + fila*"*"
#     for renglones in range(1,n):
#         fila = 2*(n-renglones)-1
#         di += "\n" + renglones*"-" + fila*"*"
#     return di

# variable = int(input())
# print(diamante(variable))

#Ejercicio 8: Cantidad de números de Armstrong y de números perfectos
# def chArmstrong(n):
#     n = str(int(n))
#     suma = 0
#     for digit in n:
#         suma += int(digit)**len(n)
#     return suma == n

# def chPerfecto(n):
#     suma = 0
#     for div in range(2,n):
#         if n%div == 0: suma += div
#     return suma == n

# n=1
# cArm = cPerf = 0
# while n>=1 and n<1000:
#     n = int(input())
#     if chArmstrong(n): cArm +=1
#     if chPerfecto(n): cPerf +=1
# print(cArm,cPerf)