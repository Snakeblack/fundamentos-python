import os
os.system("clear")

def print_title(title):
    l = len(title)
    c = "-" * (l + 3)
    print("\n", c)
    print("|",title,"|")
    print(c)
    
def print_subtitle(subtitle):
    l = len(subtitle)
    c = "-" * (l + 2)
    print("\n", subtitle)
    print(c)

print_title("Estructura de datos")
# Usando listas como colas / Using List as Queues

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")   # Terry arrives
queue.append("Graham")  # Graham arrives
x = queue.popleft()     # The first to arrive now leaves
print(x)                # 'Eric'
x = queue.popleft()     # The second to arrive now leaves
print(x)                # 'Jhon'
print(queue)            # deque(['Michael', 'Terry', 'Graham'])

# Comprension de listas

squares = []
print_subtitle("opcion for")
for x in range(10):
    squares.append(x**2)
print("\n", squares)
print_subtitle("opcion map + lambda")
squares = list(map(lambda x: x**2, range(10)))
print("\n", squares)
print_subtitle("opcion de lista de comprension")
squares = [x**2 for x in range(10)]
print("\n", squares)

test = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print("\n", test)

vec = [-4, -2, 0, 2, 4]
# crea una lista con valores dobles
[x*2 for x in vec]

# filtra la lista de numeros negativos
[x for x in vec if x >= 0]

# aplica una funcion a todos los elementos
[abs(x) for x in vec]

# llama al metodo en todos los elementos
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]

# crea una lista con tuplas (numero, cuadrado)
[(x, x**2) for x in range(6)]

# la tupla necesita estar entre parentesis, de lo contrario se genera un error
# [x, x**2 for x in range(6)]

# normaliza una lista usando una composicion de lista con dos 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]

# Generar un rango de numeros pi.
from math import log, pi
num_pi = [str(round(pi, i)) for i in range(1, 6)]
print("\n", num_pi)

# Listas por comprensión anidadas
print_subtitle("Listas por comprensión anidadas")

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
matri = [[row[i] for row in matrix] for i in range(4)]
print(matri)

print(round(10.3456, 2))

x = '123' + '456'
print(x)

