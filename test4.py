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
            return print("bien hecho!") and True
        if ok in ('n', 'no', 'nop', 'nope'):
            return print("y a que esperas?") and False
        retries = retries - 1
        if retries < 0:
            raise ValueError("respuesta invalida")
        print(reminder)

ask_ok("ok, has invertido en Cardano?")

print_subtitle("4.7.2 Palabras claves como argumentos")

def device(voltage, state='baratas', action='BOOM', type='Acer'):
    print("-- Este dispositivo hizo", action, end=' ')
    print("cuando hubo un pico de", voltage, "voltios")
    print("-- No tenia protección de subida de tension, no me gusta la marca", type)
    print("-- Son", state, ":/")

device(10000);

print_subtitle("Ejemplo nº2")

def burgershop(kind, *arguments, **keywords):
    print("-- Tienes alguna", kind, "?")
    print("-- Lo siento, no nos queda", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

burgershop("Hamburguesa", "Respuesta random.",
           "Otra respuesta random.",
           vendedor="Ana",
           cliente="Juan",
           tienda="Hamburgueseria")

print_subtitle("4.7.3 Parametros especiales")

print("""def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
       |             |                  |
       |  Posicionales y palabras clave |
       |                                - Palabras clave
        -- Solo posicionales""")

# Si / y * no están presentes en la definición de la función, los parámetros pueden ser pasados a una función posicionalmente o por palabra clave.

def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


# "4.7.4 Listas de argumentos arbitrarios"

def write_multiple_items(file, separartor, *args):
    file.write(separartor.join(args))

def concat(*args, sep="/"):
    return sep.join(args)

concat("earth", "mars", "venus")
concat("earth", "mars", "venus", sep=".")

print_subtitle("4.7.5 Desempaquetando una lista de argumentos")

list(range(3, 6))

args = [3, 6]
list(range(*args))

