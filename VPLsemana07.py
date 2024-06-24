# Ejercicio 1: Factorial
# def factorial(n):
#     if n == 0: return 1
#     else: return n*factorial(n-1)
# print(factorial(n = int(input())))

# Ejercicio 2: Fibonacci
# def fibonacci(n):
#     if n == 0: return 1
#     if n == 1: return 1
#     else: return fibonacci(n-2)+fibonacci(n-1)
# def seriefib(n):
#     serie = "1"
#     for i in range(1,n+1):
#         serie += ", "+ str(fibonacci(i))
#     return serie
# print(seriefib(int(input())))

# Ejercicio 3: MCD Recursivo
# def MCD(n1, n2):
#     if n1%n2 == 0: return n2
#     else: return MCD(n2,n1%n2)
# pepe = int(input())
# juan = int(input())
# print(f"El MCD resultante es {MCD(pepe,juan)}")

# Ejercicio 4: Convertir un número a binario
# def validar():
#     x = -2.5
#     while x != round(x) or x < 0:
#         x = float(input())
#     return int(x)

# def binario(n):
#     if n<2: return int(n)
#     else:   return str(binario(n//2)) + str(n%2)

# print(binario(validar()))

# Ejercicio 4: Invertir un número
# def Invertir(n):
#     if n < 10: return n
#     else: return str(n%10) + str(Invertir(n//10))
    
# print(Invertir(int(input())))