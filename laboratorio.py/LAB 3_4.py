#Ejercicio 1: Escribe una función recursiva que imprima los números pares del 1 al 100.
"""
def imprimir_par(n=2):
    if n <= 100:  # Verifica si el número actual es menor o igual a 100
        print(n)  # Imprime el número par actual
        imprimir_par(n + 2)  # Llama a la función recursivamente con el siguiente número par

imprimir_par()  # Inicia la función con el primer número par"""

#Ejercicio 2: Escribe una función recursiva que imprima la suma de los números del 1 al n.
"""def suma_recursiva(n):
    if n == 0:
        return 0
    else:
        return n + suma_recursiva(n - 1)

n = int(input("Ingrese un número: "))

print("La suma de los números del 1 al", n, "es : ", suma_recursiva(n))"""
#Ejercicio 3: Escribe una función recursiva que imprima la pirámide de números del 1 al n.


"""def imprimir_piramide(n, current=1):
    if current > n:  # Condición de base
        return
    # Imprimir espacios necesarios para alinear los números
    print(' ' * (n - current) + ' '.join(str(i) for i in range(1, current + 1)))
    # Llamada recursiva para el siguiente nivel
    imprimir_piramide(n, current + 1)

# Solicitar al usuario que ingrese el número de niveles de la pirámide
n = int(input("Ingrese el número de niveles de la pirámide: "))
imprimir_piramide(n)"""


#Ejercicio 4: Escribe una función recursiva que imprima la pirámide de números invertidos del 1 al n
"""def piramide_invert(n, current=1):
   if current > n: # Condición de base para detener la recursión
       return
   # Imprimir los números del nivel actual
   print(' '.join(str(i) for i in range(current, 0, -1)))
   # Llamada recursiva para el siguiente nivel
   piramide_invert(n, current + 1)

# Solicitar al usuario que ingrese el número de niveles de la pirámide
n = int(input("Ingrese el número de niveles de la pirámide: "))
piramide_invert(n)"""

#Ejercicio 2: Escribe una función recursiva que imprima la tabla de multiplicar del n.

"""def imprimir_tabla_multiplicar(n, i=1):
 if i > 12: # Condición de base para detener la recursión
    return
 print(f"{n} x {i} = {n * i}") # Imprimir la multiplicación actual
 imprimir_tabla_multiplicar(n, i + 1) # Llamada recursiva para el siguiente número

# Solicitar al usuario que ingrese un número
n = int(input("Ingrese un número: "))
imprimir_tabla_multiplicar(n)"""



###

#
##
#
#
###

#
#










#ejercicio 6: Crear una matriz de números reales
import numpy as np

matriz_real = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("matriz de numero reales :",matriz_real)

# 2Crear una matriz de números complejos
matriz_compleja = np.array([[1+2j, 2+3j, 3+4j], [4+5j, 5+6j, 6+7j]])
print("matriz de numeros compleja: \n",matriz_compleja)


# 3 Crear una matriz de matrices

matriz_de_matrices = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("matriz de matrices:\n ",matriz_de_matrices)

# 4 Acceder al elemento central de una matriz

elemento_central = matriz_real[1, 1]
print("elemento central de una matriz: ",elemento_central)

# 5 Suma de dos matrices de diferentes tamaños

matriz1 = np.array([[1, 2,], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
suma_matrices = matriz1 + matriz2
print("suma de matrices de diferentes tamaños: ",suma_matrices)


# 6Multiplicar una matriz por un número

matriz_por_numero = matriz_real * 2
print("multiplicar una matriz por un numero: ",matriz_por_numero)

#7 Calcular la media de los elementos de una matriz
media_valores = np.mean(matriz_real)
print("media de elementos de una matriz: ",media_valores)








"""
#PARTE 2
#1 Cree una matriz de números aleatorios de tamaño 100x100:
import numpy as np

matriz_aleatoria = np.random.rand(100, 100)
print("esta es la matriz",matriz_aleatoria)

#2 Calcular la media de los elementos de la matriz
media = np.mean(matriz_aleatoria)
print("Media: ", media)

# 2 Calcular la mediana de los elementos de la matriz
mediana = np.median(matriz_aleatoria)
print("Mediana: ", mediana)


#2 Calcular la desviación estándar de los elementos de la matriz
desviacion_estandar = np.std(matriz_aleatoria)
print("Desviación estándar: ", desviacion_estandar)


#3 Escribir una función que encuentre el elemento máximo de una matriz:
def maximo(matriz):
 return np.max(matriz)

print("Elemento máximo: ", maximo(matriz_aleatoria))



# 4 Escribir una función que encuentre la submatriz de mayor suma de una matriz:
def submatriz_maxima(matriz):
 fila, columna = matriz.shape
 max_val = 0
 max_submatriz = None

 for i in range(fila):
     for j in range(columna):
         if i + 1 < fila and j + 1 < columna:
             submatriz = matriz[i:i+2, j:j+2]
             suma = np.sum(submatriz)
             if suma > max_val:
               max_val = suma
               max_submatriz = submatriz
 return max_submatriz

print("Submatriz de mayor suma: \n", submatriz_maxima(matriz_aleatoria))



# 5 Escribir una función que encuentre la matriz de covarianza de dos matrices:
def matriz_covarianza(matriz1, matriz2):
 return np.cov(matriz1, matriz2)

# Crear dos matrices para el ejemplo
matriz1 = np.random.rand(100, 100)
matriz2 = np.random.rand(100, 100)

print("Matriz de covarianza: \n", matriz_covarianza(matriz1, matriz2))"""


















