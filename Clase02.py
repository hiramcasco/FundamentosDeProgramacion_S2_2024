#Ejercicio 01
"""nombre = "Marcos Jara"
print ("Hola",nombre+"!")
"""
#Ejercicio 02
"""_nombre = input("Ingrese su nombre: ")
print ("Hola",_nombre+"!")
"""
#Ejercicio 03
"""name = "Alex"
lastname = "Ferreira"
print("Hola, ",name,lastname+"!","Tres tristes tigres tragan trigo en un trigal")
"""
#Ejercicio 04
"""a = 7
b = 5
_res = float(3*a-4*b/(a**2))
print(f"El valor es: {_res:.2f}")
"""
#Ejercicio 05
"""pi = 3.14
_radio = float(input("Ingrese el radio de una cia: "))
print(f"la longitud de tu cia es: {(2*pi*_radio):.2f}")
"""
#Ejercicio 06
"""temp_c = float(input("Ingrese temperatura en celsius: "))
_temp_f = 9*_temp_c/5 + 32
_texto = f"su equivalente en farenheit es: {_temp_f:.3f}°F"

print(_texto)
"""
#Ejercicio 07 (como cadena)
"""_5cifras = input("Introduzca un n'umero de 5 cifras:")
_centena = _5cifras[2]
print(_centena,"es la centena de",_5cifras)
"""
#Ejercicio 07 (como entero)
"""_5cifras = int(input("Introduzca un n'umero de 5 cifras:"))
_centena = int(_5cifras/100)%10
print("La centena es:",_centena)
"""
#Ejercicio 08
"""_a = float(input("Ingrese un numero:"))
_b = float(input("Ingrese otro numero:"))
_c = float(input("Ingrese otro numero más:"))

print("El promedio de los numeros es:",(_a+_b+_c)/3)
"""
#Ejercicio 09
"""_cateto0 = float(input("Ingrese el valor de de un cateto: "))
_cateto1 = float(input("Ingrese el valor de de otro cateto: "))
_hipotenusa = (_cateto0**2+_cateto1**2)**(1/2)
print(f"El valor de la himpotenusa es: {_hipotenusa:.3f}")
"""
#Ejercicio 10
"""lista = ["Hola","que","tal","amigo?"]
oracion = " ".join(lista)
print(oracion)
"""
#Ejercicio 11

#Ejercicio 12

#Ejercicio Extra
"""print("Experimentar con la impresion de strings:")
_cadena =input("Cadena:")
_inicio = int(input("Inicio:"))
_fin = int(input("Fin:"))
_paso = int(input("Paso:"))
print(_cadena[_inicio:_fin:_paso])
"""