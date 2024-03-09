#Ejercicio parte 01 –  Colas:
#Verificar si una palabra es palíndroma
#1. Implementa una función que determine si una palabra es palíndroma o no. Utiliza una cola para comparar los caracteres de la palabra en orden original y reverso.
"""from collections import deque

def es_palindromo(palabra):
    # Convertir la palabra a minúsculas para hacer la comparación insensible a mayúsculas
    palabra = palabra.lower()
    
    # Crear una cola y agregar cada carácter de la palabra a la cola
    cola = deque()
    for char in palabra:
        if char.isalpha(): # Ignorar espacios y caracteres no alfabéticos
            cola.append(char)
    
    # Comparar los caracteres de la palabra en orden original y en orden inverso
    while len(cola) > 1:
        primer_caracter = cola.popleft() # Quitar el primer carácter de la cola
        ultimo_caracter = cola.pop() # Quitar el último carácter de la cola
        
        if primer_caracter != ultimo_caracter:
            return False # Si los caracteres no coinciden, no es un palíndromo
    
    return True # Si todos los caracteres coinciden, es un palíndromo

# Ejemplo de uso
palabra = "Anita lava la tina"
if es_palindromo(palabra):
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")"""


#Diseño de un sistema de gestión de pedidos
#2. Crea un sistema de gestión de pedidos que utilice una cola para procesar los pedidos en el orden en que 
#fueron recibidos. Implementa funciones para agregar pedidos, procesar pedidos y mostrar el estado 
#actual de la cola.
"""from collections import deque

class Pedido:
    def __init__(self, id_pedido, descripcion):
        self.id_pedido = id_pedido
        self.descripcion = descripcion

    def __str__(self):
        return f"Pedido {self.id_pedido}: {self.descripcion}"

class GestorPedidos:
    def __init__(self):
        self.cola_pedidos = deque()

    def agregar_pedido(self, pedido):
        self.cola_pedidos.append(pedido)
        print(f"Pedido {pedido.id_pedido} agregado a la cola.")

    def procesar_pedido(self):
        if not self.cola_pedidos:
            print("No hay pedidos en la cola.")
            return
        pedido_procesado = self.cola_pedidos.popleft()
        print(f"Procesando: {pedido_procesado}")
        # Aquí puedes agregar el código para procesar el pedido

    def mostrar_estado(self):
        print("Estado actual de la cola de pedidos:")
        for pedido in self.cola_pedidos:
            print(pedido)

# Ejemplo de uso
gestor = GestorPedidos()

# Agregar pedidos a la cola
gestor.agregar_pedido(Pedido(1, "Pizza grande"))
gestor.agregar_pedido(Pedido(2, "Hamburguesa"))

# Procesar el primer pedido en la cola
gestor.procesar_pedido()

# Mostrar el estado actual de la cola
gestor.mostrar_estado()
"""
#Búsqueda de rutas en un laberinto
#3.    Desarrolla un programa que encuentre el camino más corto a través de un laberinto. Utiliza una cola 
#para realizar un recorrido en anchura (BFS) desde el punto de inicio hasta el punto de destino.
"""from collections import deque

def encontrar_camino(laberinto):
    # Encontrar la posición inicial y final
    for i in range(len(laberinto)):
        for j in range(len(laberinto[0])):
            if laberinto[i][j] == 'S':
                inicio = (i, j)
            if laberinto[i][j] == 'D':
                destino = (i, j)

    # Inicializar la cola y el diccionario de visitados
    cola = deque([inicio])
    visitados = {inicio: None}

    while cola:
        x, y = cola.popleft()
        if (x, y) == destino:
            # Construir el camino más corto
            camino = []
            while (x, y) != inicio:
                camino.append((x, y))
                x, y = visitados[(x, y)]
            camino.append(inicio)
            camino.reverse()
            return camino

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(laberinto)) and (0 <= ny < len(laberinto[0])) and (laberinto[nx][ny] != '#') and (nx, ny) not in visitados:
                cola.append((nx, ny))
                visitados[(nx, ny)] = (x, y)

    return None # No se encontró un camino

# Ejemplo de laberinto
laberinto = [
    ['S', '.', '.', '.', '.', '#', '#', '#', '#'],
    ['#', '.', '#', '#', '#', '.', '#', '#', '#'],
    ['#', '.', '.', '.', '#', '.', '#', '#', '#'],
    ['#', '#', '#', '#', '#', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#', '.', '#', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', 'D'],
]

camino = encontrar_camino(laberinto)
if camino:
    print("Camino encontrado:")
    for x, y in camino:
        print(f"({x}, {y})", end=" -> ")
    print("Destino")
else:
    print("No se encontró un camino.")"""


#Diseño de un sistema de gestión de tareas (Avanzado)
#4.    Implementa  un  sistema  de  gestión  de  tareas  que  permita  agregar  tareas,  marcar  tareas  como 
#completadas y mostrar la próxima tarea pendiente.
"""class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append({'tarea': tarea, 'completada': False})
        print(f"Tarea '{tarea}' agregada.")

    def marcar_como_completada(self, tarea):
        for tarea_en_lista in self.tareas:
            if tarea_en_lista['tarea'] == tarea:
                tarea_en_lista['completada'] = True
                print(f"Tarea '{tarea}' marcada como completada.")
                return
        print(f"Tarea '{tarea}' no encontrada.")

    def mostrar_proxima_tarea_pendiente(self):
        for tarea in self.tareas:
            if not tarea['completada']:
                print(f"Próxima tarea pendiente: {tarea['tarea']}")
                return
        print("No hay tareas pendientes.")

# Ejemplo de uso
gestor = GestorTareas()

# Agregar tareas
gestor.agregar_tarea("Hacer la compra")
gestor.agregar_tarea("Llamar al médico")
gestor.agregar_tarea("Estudiar para el examen")

# Marcar una tarea como completada
gestor.marcar_como_completada("Hacer la compra")

# Mostrar la próxima tarea pendiente
gestor.mostrar_proxima_tarea_pendiente()
"""
#Ejercicios parte 02 - Arboles:
#Contar nodos:
#5.    Implementar una función que cuente la cantidad de nodos en el árbol.
def contar_nodos(nodo):
    """
    Cuenta la cantidad de nodos en el árbol.
    
    :param nodo: Diccionario que representa el nodo actual.
    :return: La cantidad total de nodos en el árbol.
    """
    if nodo is None:
        return 0
    else:
        # Suma 1 para contar el nodo actual
        total = 1
        # Suma los nodos hijos
        for hijo in nodo.get('hijos', []):
            total += contar_nodos(hijo)
        return total

# Ejemplo de uso
arbol = {
    'valor': 'A',
    'hijos': [
        {'valor': 'B', 'hijos': [{'valor': 'D'}]},
        {'valor': 'C', 'hijos': [{'valor': 'E'}, {'valor': 'F'}]}
    ]
}

cantidad_nodos = contar_nodos(arbol)
print(f"El árbol tiene {cantidad_nodos} nodos.")

#6.    Implementar una función que cuente la cantidad de nodos hoja (que no tienen hijos).
def contar_nodos_hoja(nodo):
    """
    Cuenta la cantidad de nodos hoja en el árbol.
    
    :param nodo: Diccionario que representa el nodo actual.
    :return: La cantidad total de nodos hoja en el árbol.
    """
    if nodo is None:
        return 0
    elif not nodo.get('hijos', []): # Si el nodo no tiene hijos
        return 1
    else:
        # Suma los nodos hoja de los hijos
        total = 0
        for hijo in nodo.get('hijos', []):
            total += contar_nodos_hoja(hijo)
        return total

# Ejemplo de uso
arbol = {
    'valor': 'A',
    'hijos': [
        {'valor': 'B', 'hijos': [{'valor': 'D'}]}, # Nodo hoja
        {'valor': 'C', 'hijos': [{'valor': 'E'}, {'valor': 'F'}]} # Nodo hoja
    ]
}

cantidad_nodos_hoja = contar_nodos_hoja(arbol)
print(f"El árbol tiene {cantidad_nodos_hoja} nodos hoja.")

#7.     Implementar una función que cuente la cantidad de nodos internos (que tienen al menos un hijo). 
def contar_nodos_internos(nodo):
    """
    Cuenta la cantidad de nodos internos en el árbol.
    
    :param nodo: Diccionario que representa el nodo actual.
    :return: La cantidad total de nodos internos en el árbol.
    """
    if nodo is None:
        return 0
    elif nodo.get('hijos', []): # Si el nodo tiene al menos un hijo
        return 1 + sum(contar_nodos_internos(hijo) for hijo in nodo['hijos'])
    else:
        return 0

# Ejemplo de uso
arbol = {
    'valor': 'A',
    'hijos': [
        {'valor': 'B', 'hijos': [{'valor': 'D'}]}, # Nodo interno
        {'valor': 'C', 'hijos': [{'valor': 'E'}, {'valor': 'F'}]} # Nodo interno
    ]
}

cantidad_nodos_internos = contar_nodos_internos(arbol)
print(f"El árbol tiene {cantidad_nodos_internos} nodos internos.")

#Calcular altura y profundidad:
#8.    Implementar una función que calcule la altura del árbol (la longitud del camino más largo desde la raíz 
#hasta una hoja).
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def altura_arbol(nodo):
    """
    Calcula la altura del árbol.
    
    :param nodo: Nodo raíz del árbol.
    :return: La altura del árbol.
    """
    if nodo is None:
        return 0
    else:
        # Calcula la altura del subárbol izquierdo
        altura_izquierda = altura_arbol(nodo.izquierdo)
        # Calcula la altura del subárbol derecho
        altura_derecha = altura_arbol(nodo.derecho)
        # La altura del árbol es el máximo de las alturas de los subárboles más uno
        return max(altura_izquierda, altura_derecha) + 1

# Ejemplo de uso
nodo_raiz = Nodo(1)
nodo_raiz.izquierdo = Nodo(2)
nodo_raiz.derecho = Nodo(3)
nodo_raiz.izquierdo.izquierdo = Nodo(4)
nodo_raiz.izquierdo.derecho = Nodo(5)

altura = altura_arbol(nodo_raiz)
print(f"La altura del árbol es {altura}.")

#9.    Implementar una función que calcule la profundidad de un nodo (la longitud del camino desde la raíz 
#hasta el nodo).
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def profundidad_nodo(nodo, valor, profundidad=0):
    """
    Calcula la profundidad de un nodo específico en el árbol.
    
    :param nodo: Nodo raíz del árbol.
    :param valor: Valor del nodo para el cual se quiere calcular la profundidad.
    :param profundidad: Profundidad del nodo actual desde la raíz.
    :return: La profundidad del nodo especificado.
    """
    if nodo is None:
        return -1 # Nodo no encontrado
    if nodo.valor == valor:
        return profundidad # Nodo encontrado, retorna la profundidad
    izquierda = profundidad_nodo(nodo.izquierdo, valor, profundidad + 1)
    if izquierda != -1:
        return izquierda # Si encontramos el nodo en el subárbol izquierdo, retornamos la profundidad
    return profundidad_nodo(nodo.derecho, valor, profundidad + 1) # Buscamos en el subárbol derecho

# Ejemplo de uso
nodo_raiz = Nodo(1)
nodo_raiz.izquierdo = Nodo(2)
nodo_raiz.derecho = Nodo(3)
nodo_raiz.izquierdo.izquierdo = Nodo(4)
nodo_raiz.izquierdo.derecho = Nodo(5)

valor_buscado = 5
profundidad = profundidad_nodo(nodo_raiz, valor_buscado)
if profundidad != -1:
    print(f"La profundidad del nodo con valor {valor_buscado} es {profundidad}.")
else:
    print(f"El nodo con valor {valor_buscado} no se encuentra en el árbol.")

#Buscar el mínimo y el máximo:
#10.  Implementar una función que encuentre el nodo con el valor mínimo en el árbol.

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def nodo_minimo(nodo):
    """
    Encuentra el nodo con el valor mínimo en el árbol.
    
    :param nodo: Nodo raíz del árbol.
    :return: El nodo con el valor mínimo.
    """
    if nodo is None:
        return None
    elif nodo.izquierdo is None:
        return nodo
    else:
        return nodo_minimo(nodo.izquierdo)

# Ejemplo de uso
nodo_raiz = Nodo(50)
nodo_raiz.izquierdo = Nodo(30)
nodo_raiz.derecho = Nodo(70)
nodo_raiz.izquierdo.izquierdo = Nodo(20)
nodo_raiz.izquierdo.derecho = Nodo(40)
nodo_raiz.derecho.izquierdo = Nodo(60)
nodo_raiz.derecho.derecho = Nodo(80)

nodo_min = nodo_minimo(nodo_raiz)
if nodo_min:
    print(f"El nodo con el valor mínimo es {nodo_min.valor}.")
else:
    print("El árbol está vacío.")


#11.   Implementar una función que encuentre el nodo con el valor máximo en el árbol.
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def nodo_maximo(nodo):
    """
    Encuentra el nodo con el valor máximo en el árbol.
    
    :param nodo: Nodo raíz del árbol.
    :return: El nodo con el valor máximo.
    """
    if nodo is None:
        return None
    elif nodo.derecho is None:
        return nodo
    else:
        return nodo_maximo(nodo.derecho)

# Ejemplo de uso
nodo_raiz = Nodo(50)
nodo_raiz.izquierdo = Nodo(30)
nodo_raiz.derecho = Nodo(70)
nodo_raiz.izquierdo.izquierdo = Nodo(20)
nodo_raiz.izquierdo.derecho = Nodo(40)
nodo_raiz.derecho.izquierdo = Nodo(60)
nodo_raiz.derecho.derecho = Nodo(80)

nodo_max = nodo_maximo(nodo_raiz)
if nodo_max:
    print(f"El nodo con el valor máximo es {nodo_max.valor}.")
else:
    print("El árbol está vacío.")
