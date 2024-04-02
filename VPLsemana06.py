# Ejercicio 1: Escriba una función para generar una serie de números primos comprendidos entres 2 y N

def primo(n):
    serie = ""
    for numero in range(2,n+1):
        primo = True
        for divisor in range (2,numero):
            if (numero % divisor == 0):
                primo = False
                break
        if primo:
            serie += f"{numero} "
    
    return serie

m = int(input())
print(primo(m))