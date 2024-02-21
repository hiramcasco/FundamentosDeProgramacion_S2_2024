
#Ejercicio 1: Hallar la sumatoria y el promedio de los multiplos de 3 menores que un  numero n ingresado
"""n = int(input("Ingrese un numero: "))
print()

sumatoria = 0
multiplos = 0
for index in range(3,n,3):
    sumatoria += index
    multiplos += 1
    print(f"multiplo {multiplos} detectado: {index}")

print()
print(f"La sumatoria de los {multiplos} multiplos de 3 menores que {n} es {sumatoria}")
print(f"El promedio de los {multiplos} multiplos de 3 menores que {n} es {sumatoria/multiplos}")
"""
#Ejercicio 2: Hallar el factorial de un numero ingresado por teclado
"""n = int(input("Ingrese un numero: "))
print()

fact = 1
for index in range (1,n+1):
    tfact = fact
    fact = index*fact
    print(f"{tfact} * {index} = {fact}")
print()
print(f"El factorial de {n} es {fact}")"""

#Ejercicio 3: Imprimir en pantalla los numeros comprendidos entre 1 y 100
#pero para los multiplos de 3 imprimir "Fizz" los de 5 "Buzz" y los de ambos "FizzBuzz"
"""for index in range(1,101):
    if (index%5 == 0) or (index%3 == 0) :
            if index%3 == 0: print("Fizz",end="")
            if index%5 == 0: print("Buzz",end="")
            print()
    else: print(index)"""

#Ejercicio 4: Mostrar los primeros p numeros de una sucesión: n**2 +1
"""n = int(input("Ingresar n:"))
p = int(input("Ingresar p:"))
print(f"primeros {p} sucesion n**2 +1 son:")

for index in range(1,p+1):
    termino = index*index + 1
    print(termino,end=" ")"""