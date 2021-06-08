# PRACTICAS Y EJERCICIOS PYTHON3
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

# 4.4 Las sentencias break, continue, y else en bucles
print_title("4.4 sentencias break y continue")
    #break: se usa para interrumpir un bucle for o while, tambien puede ser usado en una condicion si este esta dentro de un bucle.
print_subtitle("break")

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'igual que', x, '*', n//x)
            break
    else:
        print(n, 'es un numero primo')

print_subtitle("continue")

    #continue: se usa para continuar hacia la siguiente linea en la siguiente iteracion del bucle

for num in range(2, 10):
    if num % 2 == 0:
        print("Encontre un numero par", num)
        continue
    print("Encontre un numero inpar", num)

# print("-------------------------")

# 4.5 La sentencia pass
    #pass : se usa para interrupir bucles o crear clases vacias o funciones vacias donde implementar codigo.

#   while True:
#       pass    # bucle interrumpido como la interrupcion de (Ctrl+C)

#   class MyEmtyClass:
#       pass    # Interrupcion de la fonrmacion de una clase (la clase es creada, pero vacio)

#   def initlog(*args):
#       pass    # Con esto no da error, pero recuerda implementar codigo aqui.

# 4.6 Definiendo funciones
    #Podemos crear una funcion que escriba la serie de Fibonacci hasta un limite determinado:
print_title("4.6 Definiendo funciones")
print_subtitle("Fauncion de la serie de Fibonacci")

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(2000)
f = fib
f(100)
print(f(0))
    # Podemos crear una funcion que retorne la liste de los numeros de fibonacci en lugar de imprimirlos
print_subtitle("Funcion de la serie de Fibonacci en un array")

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

f100 = fib2(100)
print(f100)

print_title("4.7 Definicion de funciones")
print_subtitle("4.7.1 Argumentos con valores por omision")

def ask_ok(prompt, retries=4, reminder="Por favor intentelo de nuevo"):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes', 'si'):
            return print("entonces to the moon") and True
        if ok in ('n', 'no', 'nop', 'nope'):
            return print("eres tontisimo") and False
        retries = retries - 1
        if retries < 0:
            raise ValueError("respuesta invalida")
        print(reminder)

ask_ok("ok, has invertido en Cardano?")

print_subtitle("4.7.2 Palabras claves como argumentos")

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- Este loro no haría", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000);

print_subtitle("4.7.3 Parametros especiales")

print("""def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
       |             |                  |
       |        Positional or keyword   |
       |                                - Keyword only
        -- Positional only""")






