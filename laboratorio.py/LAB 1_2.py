#1

"""num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Realizar las operaciones básicas
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

# Verificación de la división por cero
if num2 != 0:
    division = num1 / num2
else:
    division = "No es posible dividir por cero."

# Mostrar resultados
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")"""


#2
"""numero = int(input("Ingrese un número: "))


if numero % 2 == 0:
    print(f"{numero} es un número par.")
else:
    print(f"{numero} es un número impar.")"""

#3
"""base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

# Calcular el área del triángulo
area_triangulo = 0.5 * base * altura

# Mostrar el resultado
print(f"El área del triángulo con base {base} y altura {altura} es: {area_triangulo}")
"""

#4
"""numero_factorial = int(input("Ingrese un número para calcular su factorial: "))
#c_factorial
resultado = 1
for i in range(1, numero_factorial + 1):
    resultado *= i

# Mostrar el resultado
print(f"El factorial de {numero_factorial} es: {resultado}")
"""
#5
"""def es_primo(n):
   if n < 2:
       return False
   for i in range(2, int(n**0.5) + 1):
       if n % i == 0:
           return False
   return True

numero = int(input("Ingrese un número: "))
print(f"{numero} es {'primo' if es_primo(numero) else 'no primo'}")"""


#6
#inversion de cadena

"""def invertir_cadena(cadena):
    return cadena[::-1]

texto_inicial = "buenos dias"
texto_invertido = invertir_cadena(texto_inicial)

print("texto inicial :", texto_inicial)
print("texto invertir:",texto_invertido)"""

#7
"""def suma_numeros_pares(inicio, fin):
    suma = 0
    for numero in range(inicio, fin + 1):
        if numero % 2 == 0:
            suma += numero
    return suma

# Solicitar al usuario el rango
inicio_rango = int(input("Ingrese el número inicial del rango: "))
fin_rango = int(input("Ingrese el número final del rango: "))

# Calcular la suma de los números pares en el rango especificado
resultado = suma_numeros_pares(inicio_rango, fin_rango)
print(f"La suma de los números pares en el rango de {inicio_rango} a {fin_rango} es: {resultado}")
"""

#8
"""# Generar una lista de los cuadrados de los primeros 10 números naturales
lista_cuadrados = [numero ** 2 for numero in range(1, 11)]

# Mostrar la lista resultante
print("Lista de los cuadrados de los primeros 10 números naturales:")
print(lista_cuadrados)"""


#9
"""def contar_vocales(cadena):
    # Inicializamos un contador para las vocales
    contador = 0

    # Recorremos cada carácter en la cadena
    for caracter in cadena:
        # Convertimos el carácter a minúscula para hacer la comparación
        caracter = caracter.lower()

        # Verificamos si el carácter es una vocal y aumentamos el contador
        if caracter in 'aeiou':
            contador += 1

    return contador

# Solicitar al usuario una cadena de texto
texto = input("Ingrese una cadena de texto: ")

# Llamar a la función para contar vocales y mostrar el resultado
cantidad_vocales = contar_vocales(texto)
print(f"El número de vocales en '{texto}' es: {cantidad_vocales}")
"""

#10
"""def generar_fibonacci(n):
   # Inicializa los dos primeros números de la serie
   fibonacci = [0, 1]
   
   # Genera los números restantes de la serie
   for i in range(2, n):
       fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
       
   return fibonacci

# Genera e imprime los primeros 10 números de la serie Fibonacci
print(generar_fibonacci(10))"""


#11
"""numeros = input("Ingrese una serie de números separados por comas: ")

numeros = [int(num) for num in numeros.split(",")]

numeros.sort()

print(numeros)"""

#12

"""palabra = input("Ingrese una palabra: ").lower().replace(" ", "")
print(f"¿'{palabra}' es un palíndromo? {palabra == palabra[::-1]}")"""

#13

"""numero = int(input("Ingrese el número para generar su tabla de multiplicar: "))

for i in range(1, 13):
    print(f"{numero} x {i} = {numero * i}")"""

#14
"""import math

radio = float(input("Introduce el radio del círculo: "))

area = math.pi * radio**2

print("El área del círculo es:", area)
  
#otra manera sin importar mas lametaticas

radio = float(input("Ingrese el radio del círculo: "))
pi = 3.14159
area = pi * radio ** 2

print("El área del círculo es:", area)
"""
#15

"""numero = input("Ingrese un número entero: ")

suma_digitos = sum(int(digito) for digito in numero)

print(f"La suma de los dígitos es: {suma_digitos}")"""


import numpy as np

# Crear dos matrices de diferentes tamaños
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8], [9, 10]])

# Redimensionar las matrices para que tengan la misma forma
matriz1 = np.resize(matriz1, matriz2.shape)

# Sumar las matrices
suma_matrices = matriz1 + matriz2

print(suma_matrices)



