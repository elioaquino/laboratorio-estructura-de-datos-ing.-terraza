#PARTE 1°
def num_primo(primo):
    if primo == 1:
        return False
    for i in range (2, int(primo**0.5)+1):
        if primo % i==0:
            return False
    return True

def conjuntos_primos(conjunto):
    primos = {numero for numero in conjunto_numeros if num_primo(numero)}
    return primos

conjunto_numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}

resultado_primos = conjuntos_primos(conjunto_numeros)

print("Números primos en el conjunto:", resultado_primos)

#########################2###################################################

def palabrasinicial(conjunto_palabras):
    return {palabra for palabra in conjunto_palabras if palabra.startswith('c')}

conjunto_palabras = {"casa", "zapato", "auto", "cienpies", "laptop"}

resultado = palabrasinicial(conjunto_palabras)
print("Palabras que comienzan con 'c':", resultado)

################################3##############################################
def numeros_divisibles_por(conjunto, divisor):
    return {numero for numero in conjunto if numero % divisor == 0}

conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
divisor = 2

resultado = numeros_divisibles_por(conjunto, divisor)

print(f"Números divisibles por {divisor}:", resultado)

#############################4############################################
def interseccion_entre_conjuntos(conjunto1, conjunto2):
    conjunto1 = set(conjunto1)
    conjunto2 = set(conjunto2)

    interseccion = conjunto1.intersection(conjunto2)
    
    return interseccion

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {3, 4, 5, 6, 7}

resultado = interseccion_entre_conjuntos(conjunto_a, conjunto_b)

print("Conjunto resultante:", resultado)

#############################5###############################
def diferenciadeconjuntos1(conjunto1, conjunto2):
    conjunto1 = set(conjunto1)
    conjunto2 = set(conjunto2)
    
    diferencia = conjunto1 - conjunto2
    
    return diferencia

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {3, 4, 5, 6, 7}

resultado = diferenciadeconjuntos1(conjunto_a, conjunto_b)

print("Conjunto resultante:", resultado)
################################6################################
def diferenciadeconjuntos2(conjunto1, conjunto2):
    
    conjunto1 = set(conjunto1)
    conjunto2 = set(conjunto2)
    
    diferencia = conjunto2 - conjunto1
    
    return diferencia

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {3, 4, 5, 6, 7}

resultado = diferenciadeconjuntos2(conjunto_a, conjunto_b)

print("Conjunto resultante:", resultado)
 
###############################7#########################################
def anagramas(palabra1, palabra2):
    return sorted(palabra1) == sorted(palabra2)
def anagramas_conjunto(conjunto_palabras):
    
    lista_palabras = list(conjunto_palabras)
    resultado = set()

    for i in range(len(lista_palabras)):
        for j in range(i + 1, len(lista_palabras)):
            primera = lista_palabras[i]
            segunda = lista_palabras[j]

            if anagramas(primera, segunda):
                resultado.add(primera)
                resultado.add(segunda)

    return resultado
conjunto_palabras = {"roma", "amor", "perro", "rrope","alcohol","gato"}

resultanagramas = anagramas_conjunto(conjunto_palabras)

print("Conjunto de anagramas:", resultanagramas)

#############################8######################################

def palindromo(palabra):
    return palabra == palabra[::-1]

def palindromos_en_conjunto(conjunto_palabras):
    
    palindromos = {palabra for palabra in conjunto_palabras if palindromo(palabra)}
    return palindromos

conjunto_palabras = {"oso", "reconocer", "hola", "radar", "python", "civic"}

resultado_palindromos = palindromos_en_conjunto(conjunto_palabras)

print("Conjunto de palíndromos:", resultado_palindromos)

###################################9#################################

def palabras_con_longitud(conjunto_palabras, longitud_deseada):
    palabras_seleccionadas = {palabra for palabra in conjunto_palabras if len(palabra) == longitud_deseada}
    return palabras_seleccionadas

conjunto_palabras = {"oso", "reconocer", "hola", "radar", "python", "civic"}
longitud_deseada = 4

resultado_palabras = palabras_con_longitud(conjunto_palabras, longitud_deseada)

print(f"Palabras con longitud {longitud_deseada}:", resultado_palabras)

###################################10#######################################

def palabras_con_letra(conjunto_palabras, letra_deseada):
    palabras_seleccionadas = {palabra for palabra in conjunto_palabras if letra_deseada in palabra}
    return palabras_seleccionadas

conjunto_palabras = {"oso", "reconocer", "hola", "radar", "python", "civic"}
letra_deseada = "o"

resultado_palabras = palabras_con_letra(conjunto_palabras, letra_deseada)

print(f"Palabras que contienen la letra '{letra_deseada}':", resultado_palabras)


#PARTE 2°

#1
def numeros_ordenados(conjunto_numeros):
    conjunto_ordenado = set(sorted(conjunto_numeros))
    return conjunto_ordenado

conjunto_ejemplo = {5, 2, 8, 3, 1, 7}
resultado = numeros_ordenados(conjunto_ejemplo)
print("Números ordenados de menor a mayor: ",resultado)


#2
def numeros_ordenados_descendente(conjunto_numeros):
    conjunto_ordenado_descendente = set(sorted(conjunto_numeros, reverse=True))
    return conjunto_ordenado_descendente

conjunto_ejemplo = {5, 2, 8, 3, 1, 7}
resultado = numeros_ordenados_descendente(conjunto_ejemplo)
print("Números ordenados de mayor a menor: ",resultado)


#3
def numeros_duplicados(conjunto_numeros):
    numeros_set = set()
    duplicados_set = set()

    for numero in conjunto_numeros:
        if numero in numeros_set:
            duplicados_set.add(numero)
        else:
            numeros_set.add(numero)

    return duplicados_set

conjunto_ejemplo = {1, 2, 3, 2, 4, 5, 3, 6}
resultado = numeros_duplicados(conjunto_ejemplo)
print("Números duplicados en el conjunto: ", resultado)


#4
def numeros_no_duplicados(conjunto_numeros):
    numeros_set = set()
    duplicados_set = set()

    for numero in conjunto_numeros:
        if numero in numeros_set:
            duplicados_set.add(numero)
        else:
            numeros_set.add(numero)

    numeros_no_duplicados_set = numeros_set - duplicados_set
    return numeros_no_duplicados_set

conjunto_ejemplo = {1, 2, 3, 2, 4, 5, 3, 6}
resultado = numeros_no_duplicados(conjunto_ejemplo)
print("Números no duplicados en el conjunto: ", resultado)


#5
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def primos_ordenados(conjunto_numeros):
    primos_set = {numero for numero in conjunto_numeros if es_primo(numero)}
    primos_ordenados_set = set(sorted(primos_set))
    return primos_ordenados_set

conjunto_ejemplo = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
resultado = primos_ordenados(conjunto_ejemplo)
print("Números primos ordenados de menor a mayor: ", resultado)


#6
def es_palindromo(palabra):
    return palabra == palabra[::-1]

def palindromos_ordenados(conjunto_palabras):
    palindromos_set = {palabra for palabra in conjunto_palabras if es_palindromo(palabra)}
    palindromos_ordenados_set = set(sorted(palindromos_set))
    return palindromos_ordenados_set

conjunto_ejemplo = {"radar", "python", "level", "Scratch", "Java"}
resultado = palindromos_ordenados(conjunto_ejemplo)
print("Palíndromos ordenados de menor a mayor: ", resultado)


#7
def palabras_longitud_ordenadas(conjunto_palabras, longitud):
    palabras_f = {palabra for palabra in conjunto_palabras if len(palabra) == longitud}
    palabras_ordenadas_set = set(sorted(palabras_f))
    return palabras_ordenadas_set

conjunto_ejemplo = {"python", "java", "shard", "javascript", "level"}
longitud_deseada = 5
resultado = palabras_longitud_ordenadas(conjunto_ejemplo, longitud_deseada)
print("Palabras de longitud ", longitud_deseada, "ordenadas de menor a mayor: ", resultado)


#8
def palabras_con_letra_ordenadas(conjunto_palabras, letra):
    palabras_filtradas = {palabra for palabra in conjunto_palabras if letra in palabra}
    palabras_ordenadas_set = set(sorted(palabras_filtradas, reverse=True))
    return palabras_ordenadas_set

conjunto_ejemplo = {"python", "java", "shard", "javascript", "level"}
letra_deseada = "a"
resultado = palabras_con_letra_ordenadas(conjunto_ejemplo, letra_deseada)
print("Palabras con la letra ", letra_deseada, " ordenadas de mayor a menor: ",resultado)


#9
def numeros_ordenados_sin_duplicados(conjunto_numeros):
    numeros_ordenados_set = set(sorted(conjunto_numeros))
    return numeros_ordenados_set

conjunto_ejemplo = {5, 2, 8, 3, 1, 7, 2, 8}
resultado = numeros_ordenados_sin_duplicados(conjunto_ejemplo)
print("Números ordenados de menor a mayor sin duplicados: ",resultado)


#10
def es_palindromo(palabra):
    return palabra == palabra[::-1]

def palindromos_longitud_ordenados(conjunto_palabras, longitud):
    palindromos_set = {palabra for palabra in conjunto_palabras if es_palindromo(palabra) and len(palabra) == longitud}
    palindromos_ordenados_set = set(sorted(palindromos_set))
    return palindromos_ordenados_set

conjunto_ejemplo = {"level", "radar", "python", "deified", "hello"}
longitud_deseada = 5
resultado = palindromos_longitud_ordenados(conjunto_ejemplo, longitud_deseada)
print("Palíndromos de longitud ",longitud_deseada, "ordenados de menor a mayor: ",resultado)