####### 1
"""class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None
class ListaEnlazadaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def duplicar_nodos(self):
        actual = self.cabeza
        while actual:
            nuevo_nodo = Nodo(actual.valor)
            nuevo_nodo.siguiente = actual.siguiente
            nuevo_nodo.anterior = actual
            actual.siguiente = nuevo_nodo
            actual = nuevo_nodo.siguiente

    def imprimir_lista(self, direccion):
        if direccion == 'adelante':
            actual = self.cabeza
            while actual:
                print(actual.valor, end=" -> ")
                actual = actual.siguiente
        elif direccion == 'atras':
            actual = self.cola
            while actual:
                print(actual.valor, end=" <- ")
                actual = actual.anterior
        print("None")
def main():
    lista = ListaEnlazadaDoble()
    lista.insertar_final(1)
    lista.insertar_final(2)
    lista.insertar_final(3)
    lista.insertar_final(4)

    print("Lista original hacia adelante:")
    lista.imprimir_lista('adelante')
    print("Lista original hacia atrás:")
    lista.imprimir_lista('atras')

    lista.duplicar_nodos()

    print("\nLista duplicada hacia adelante:")
    lista.imprimir_lista('adelante')
    print("Lista duplicada hacia atrás:")
    lista.imprimir_lista('atras')

if __name__ == "__main__":
    main()
"""

########## 2
"""class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaEnlazadaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar_nodo(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def imprimir_hacia_adelante(self):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print(nodo_actual.dato, end=" -> ")
            nodo_actual = nodo_actual.siguiente
        print("None")

    def imprimir_hacia_atras(self):
        nodo_actual = self.cola
        while nodo_actual is not None:
            print(nodo_actual.dato, end=" <- ")
            nodo_actual = nodo_actual.anterior
        print("None")
# Crear la lista enlazada doble
lista = ListaEnlazadaDoble()

# Agregar  9 nodos a la lista
nodos = [1,  2,  3,  4,  5,  6,  7,  8,  9]
for nodo in nodos:
    lista.agregar_nodo(nodo)

# Contar nodos pares e impares
pares =  0
impares =  0
nodo_actual = lista.cabeza
while nodo_actual is not None:
    if nodo_actual.dato %  2 ==  0:
        pares +=  1
    else:
        impares +=  1
    nodo_actual = nodo_actual.siguiente

# Imprimir la cantidad de nodos pares e impares
print(f"Nodos pares: {pares}")
print(f"Nodos impares: {impares}")

# Imprimir la lista hacia adelante y hacia atrás
print("Lista hacia adelante:")
lista.imprimir_hacia_adelante()
print("Lista hacia atrás:")
lista.imprimir_hacia_atras()"""

######## 5
"""class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaEnlazadaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar_nodo(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def invertir_lista(self):
        nodo_actual = self.cabeza
        nodo_anterior = None
        nodo_siguiente = None

        while nodo_actual is not None:
            nodo_siguiente = nodo_actual.siguiente
            nodo_actual.siguiente = nodo_anterior
            nodo_actual.anterior = nodo_siguiente
            nodo_anterior = nodo_actual
            nodo_actual = nodo_siguiente

        self.cabeza, self.cola = self.cola, self.cabeza

    def imprimir_hacia_adelante(self):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print(nodo_actual.dato, end=" -> ")
            nodo_actual = nodo_actual.siguiente
        print("None")

    def imprimir_hacia_atras(self):
        nodo_actual = self.cola
        while nodo_actual is not None:
            print(nodo_actual.dato, end=" <- ")
            nodo_actual = nodo_actual.anterior
        print("None")

# Crear la lista enlazada doble
lista = ListaEnlazadaDoble()

# Agregar  6 nodos a la lista
nodos = [1,  2,  3,  4,  5,  6]
for nodo in nodos:
    lista.agregar_nodo(nodo)

# Invertir la lista
lista.invertir_lista()

# Imprimir la lista hacia adelante y hacia atrás
print("Lista hacia adelante:")
lista.imprimir_hacia_adelante()
print("Lista hacia atrás:")
lista.imprimir_hacia_atras()
"""

#########  8
"""def evaluar_posfija(expresion):
    pila = []
    for elemento in expresion.split():
        if elemento.isdigit():
            pila.append(int(elemento))
        else:
            # Asume que todos los operadores son binarios
            operando2 = pila.pop()
            operando1 = pila.pop()
            if elemento == '+':
                resultado = operando1 + operando2
            elif elemento == '-':
                resultado = operando1 - operando2
            elif elemento == '*':
                resultado = operando1 * operando2
            elif elemento == '/':
                resultado = operando1 / operando2
            pila.append(resultado)
    return pila.pop()

# Ejemplo de uso
expresion_posfija = "2  3 +"
resultado = evaluar_posfija(expresion_posfija)
print(f"El resultado de la expresión {expresion_posfija} es {resultado}.")"""

###### 11
"""def eliminar_duplicados_pila(pila):
    # Crear una nueva lista para almacenar los elementos únicos
    pila_sin_duplicados = []
    
    # Iterar sobre los elementos de la pila original
    for elemento in pila:
        # Si el elemento no está en la nueva pila, agregarlo
        if elemento not in pila_sin_duplicados:
            pila_sin_duplicados.append(elemento)
    
    # Devolver la nueva pila sin duplicados
    return pila_sin_duplicados

# Ejemplo de uso
pila_original = [1,  2,  3,  3,  2,  2,  4,  5,  5]
pila_sin_duplicados = eliminar_duplicados_pila(pila_original)
print(pila_sin_duplicados)"""

#######   14
"""class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, elemento):
        self.elementos.append(elemento)

    def pop(self):
        if not self.vacia():
            return self.elementos.pop()

    def vacia(self):
        return len(self.elementos) ==  0

class SistemaDeshacer:
    def __init__(self):
        self.acciones = Pila()
        self.deshaceres = Pila()

    def agregar(self, elemento):
        self.acciones.push(('agregar', elemento))

    def eliminar(self, elemento):
        self.acciones.push(('eliminar', elemento))

    def deshacer(self):
        if not self.acciones.vacia():
            accion, elemento = self.acciones.pop()
            self.deshaceres.push((accion, elemento))
            if accion == 'agregar':
                print(f"Deshaciendo: eliminando {elemento}")
            else:
                print(f"Deshaciendo: agregando {elemento}")

    def rehacer(self):
        if not self.deshaceres.vacia():
            accion, elemento = self.deshaceres.pop()
            self.acciones.push((accion, elemento))
            if accion == 'eliminar':
                print(f"Rehaciendo: agregando {elemento}")
            else:
                print(f"Rehaciendo: eliminando {elemento}")

# Ejemplo de uso
sistema = SistemaDeshacer()

# Agregando elementos
sistema.agregar('elemento1')
sistema.agregar('elemento2')

# Deshaciendo una acción
sistema.deshacer()

# Rehaciendo una acción
sistema.rehacer()
"""
