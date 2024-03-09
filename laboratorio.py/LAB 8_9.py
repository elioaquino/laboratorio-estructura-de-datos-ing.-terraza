# 1 Validar la edad de un usuario.   
         
"""import getpass

def validar_edad():
    edad_str = getpass.getpass("Ingrese su edad: ")
    try:
        edad = int(edad_str)
        assert edad >=  18, "La edad debe ser mayor o igual a  18"
        print("La edad es válida.")
    except ValueError:
        print("Por favor, ingrese un número válido.")
    except AssertionError as e:
        print(e)  # Imprimirá "La edad debe ser mayor o igual a  18" si la edad es menor a  18

# Ejemplo de uso:
validar_edad()
"""



# 2 Verificar el tipo de dato de una variable.

"""def verificar_tipo(variable, tipo_esperado):
    assert type(variable) == tipo_esperado, f"El tipo de dato esperado es {tipo_esperado}, pero se recibió {type(variable)}"
    print(f"El tipo de dato de la variable es {tipo_esperado}.")

try:
    verificar_tipo(10, int)  # Esto es válido y no se lanzará ninguna excepción
    verificar_tipo("Hola", str)  # Esto también es válido
    verificar_tipo([1,  2,  3], list)  # Esto también es válido
    verificar_tipo(10, str)  # Esto lanzará un AssertionError
except AssertionError as e:
    print(e)  # Imprimirá el mensaje de error si el tipo de dato no es el esperado"""

# 3 Validar el rango de una calificación.

"""def validar_calificacion(calificacion):
    assert  0 <= calificacion <=  100, "La calificación debe estar entre  0 y  100"
    print("La calificación es válida.")

# Ejemplo de uso:
try:
    validar_calificacion(90)  
    validar_calificacion(110)  
except AssertionError as e:
    print(e) 
"""

# 4 Asegurar que una lista no esté vacía.
"""# Solicita al usuario que ingrese la masa en kilogramos
masa = float(input("Dígame su peso en kg: "))

# Constante de conversión de la masa a Julios
CONSTANTE_MASA_A_JULIOS = 1.660538921e-27

# Calcula el número de Julios
julios = masa * CONSTANTE_MASA_A_JULIOS

# Redondea el número de Julios al número entero más cercano
julios = round(julios)

# Imprime el número de Julios
print(f"El número de Julios equivalente a la masa ingresada es {julios}.")

# Ejemplo de verificación de una lista vacía
elementos = []

if not elementos:
    print("La lista está vacía.")
else:
    print("La lista no está vacía.")"""

# 5 Validar la igualdad de dos objetos.

"""def validar_igualdad(objeto1, objeto2):
    assert objeto1 == objeto2, "Los objetos no son iguales"
    print("Los objetos son iguales.")


try:
    validar_igualdad(10,  10)  
    validar_igualdad("Hola", "Hola")  
    validar_igualdad("Hola", "Adiós")  
except AssertionError as e:
    print(e) 
"""
# 6 Asegurar que un ciclo while se ejecuta al menos una vez.
"""class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

    def obtenerDato(self):
        return self.dato

    def obtenerSiguiente(self):
        return self.siguiente

    def asignarDato(self, nuevo_dato):
        self.dato = nuevo_dato

    def asignarSiguiente(self, nuevo_siguiente):
        self.siguiente = nuevo_siguiente

# Inicializar la lista enlazada
nodo_inicial = Nodo(1)
nodo_segundo = Nodo(2)
nodo_inicial.asignarSiguiente(nodo_segundo)

# Ejemplo de uso del ciclo do-while con lista enlazada
nodo_actual = nodo_inicial
ejecutar = True

while True:
    print(f"Nodo actual: {nodo_actual.obtenerDato()}")
    
    if ejecutar:
        ejecutar = False # Cambia la condición para salir en el próximo ciclo
    else:
        break # Salir del ciclo
    
    nodo_actual = nodo_actual.obtenerSiguiente()

print("Este bloque se ejecuta después del ciclo do-while.")
"""
#  7 Asegurar que una función retorna un valor específico.

"""def calcular_area_rectangulo(largo, ancho):
    assert largo >  0 and ancho >  0, "El largo y el ancho deben ser positivos"
    return largo * ancho

# Ejemplo de uso:
try:
    area = calcular_area_rectangulo(5,  3)  # Esto es válido y no se lanzará ninguna excepción
    print(area)  # Imprimirá  15
    area = calcular_area_rectangulo(-5,  3)  # Esto lanzará un AssertionError
except AssertionError as e:
    print(e)  # Imprimirá "El largo y el ancho deben ser positivos"
"""
# 8 Validar el estado de una variable después de una operación.
"""class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo

    def validar_insercion(self, dato):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            if nodo_actual.dato == dato:
                return True
            nodo_actual = nodo_actual.siguiente
        return False
# Crear una lista enlazada
lista = ListaEnlazada()

# Insertar un nuevo nodo con el valor 5
lista.insertar(5)

# Validar si el dato 5 se ha insertado correctamente
if lista.validar_insercion(5):
    print("La inserción fue exitosa.")
else:
    print("La inserción no tuvo el resultado esperado.")
"""
#  9 Asegurar que un módulo se ha importado correctamente.
"""import sys

def importar_modulo(nombre_modulo):
    try:
        __import__(nombre_modulo)
    except ModuleNotFoundError as e:
        print(f"Error al importar el módulo {nombre_modulo}: {e}")
        return False
    
    assert nombre_modulo in sys.modules, f"El módulo {nombre_modulo} no se ha importado correctamente."
    print(f"El módulo {nombre_modulo} se ha importado correctamente.")
    return True

# Ejemplo de uso:
importar_modulo('hashlib')  # Esto imprimirá "El módulo hashlib se ha importado correctamente."
importar_modulo('modulo_inexistente')  # Esto imprimirá un error y "El módulo modulo_inexistente no se ha importado correctamente."
"""
#  10   Desarrollar el código de buscar nodo en la lista enlazada simple.
"""class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def buscar_nodo(self, valor):
        actual = self.cabeza
        while actual:
            if actual.dato == valor:
                return True
            actual = actual.siguiente
        return False

# Crear una lista enlazada y agregar algunos nodos
lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)

# Buscar un nodo en la lista enlazada
print(lista.buscar_nodo(2))  # Esto imprimirá True
print(lista.buscar_nodo(4))  # Esto imprimirá False"""

# 11 Implementa una función que sume todos los nodos de una lista enlazada simple.
"""class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def sumar_valores(self):
        suma =  0
        actual = self.cabeza
        while actual:
            suma += actual.valor
            actual = actual.siguiente
        return suma

# Crear una lista enlazada y agregar algunos nodos
lista = ListaEnlazada()
lista.agregar(4)
lista.agregar(2)
lista.agregar(7)

# Sumar los valores de todos los nodos
suma = lista.sumar_valores()
print(suma)  # Esto imprimirá  13
"""
#12 Crea una función que devuelva la longitud de una lista enlazada simple.
"""class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo

    def longitud(self):
        nodo_actual = self.cabeza
        longitud = 0
        while nodo_actual is not None:
            longitud += 1
            nodo_actual = nodo_actual.siguiente
        return longitud
# Crear una lista enlazada
lista = ListaEnlazada()

# Insertar algunos nodos
lista.insertar(1)
lista.insertar(2)
lista.insertar(3)
lista.insertar(4)
lista.insertar(5)

# Obtener la longitud de la lista enlazada
longitud = lista.longitud()
print(f"La longitud de la lista enlazada es: {longitud}")
"""
# 13 Implementa una función que concatene dos listas enlazadas simples.
"""class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.largo =  0

    def agregar(self, valor):
        nodo = Nodo(valor)
        if self.largo ==  0:
            self.primero = nodo
        else:
            actual = self.primero
            while actual.proximo:
                actual = actual.proximo
            actual.proximo = nodo
        self.largo +=  1

    def concatenar(self, lista2):
        if self.largo ==  0:
            self.primero = lista2.primero
        else:
            actual = self.primero
            while actual.proximo:
                actual = actual.proximo
            actual.proximo = lista2.primero
        self.largo += lista2.largo

def principal():
    lista1 = ListaEnlazada()
    lista1.agregar(1)
    lista1.agregar(2)
    lista1.agregar(3)

    lista2 = ListaEnlazada()
    lista2.agregar(4)
    lista2.agregar(5)
    lista2.agregar(6)

    lista1.concatenar(lista2)

    actual = lista1.primero
    while actual:
        print(actual.valor)
        actual = actual.proximo

if __name__ == "__main__":
    principal()"""
# 14 Crea una función que elimine los nodos duplicados de una lista enlazada simple.
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo

    def eliminar_duplicados(self):
        if self.cabeza is None:
            return
        valores_vistos = set()
        actual = self.cabeza
        anterior = None
        while actual is not None:
            if actual.dato in valores_vistos:
                anterior.siguiente = actual.siguiente
            else:
                valores_vistos.add(actual.dato)
                anterior = actual
            actual = actual.siguiente
# Crear una lista enlazada
lista = ListaEnlazada()

# Insertar algunos nodos con valores duplicados
lista.insertar(1)
lista.insertar(2)
lista.insertar(3)
lista.insertar(1)
lista.insertar(4)
lista.insertar(2)

# Eliminar nodos duplicados
lista.eliminar_duplicados()

# Imprimir la lista enlazada sin duplicados
nodo_actual = lista.cabeza
while nodo_actual is not None:
    print(nodo_actual.dato, end=" ")
    nodo_actual = nodo_actual.siguiente

# 15 Implementa una función que invierta el orden de una lista enlazada simple.
"""class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
def invertir_lista(lista):
    # Inicializando los valores
    prev = None
    curr = lista.cabeza
    nex = curr.siguiente if curr else None

    # Recorriendo la lista y ajustando los punteros
    while curr:
        # Invirtiendo el enlace
        curr.siguiente = prev

        # Moviendo al siguiente nodo
        prev = curr
        curr = nex
        if nex:
            nex = nex.siguiente

    # Inicializando la cabeza de la lista invertida
    lista.cabeza = prev
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def imprimir_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

def main():
    lista = ListaEnlazada()
    lista.insertar_final(1)
    lista.insertar_final(2)
    lista.insertar_final(3)

    print("Lista original:")
    lista.imprimir_lista()

    invertir_lista(lista)

    print("Lista invertida:")
    lista.imprimir_lista()

if __name__ == "__main__":
    main()

"""