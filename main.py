from turtle import *
from freegames import vector
import math

# La función se llama line
# parametro de entrada: start y end
# parametro de salida: N/A (no regresa valores)
# Descripcion: dibuja una linea dados 2 pixeles (donde empieza y donde termina)
def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)
    
# La función se llama square
# parametro de entrada: start y end
# parametro de salida: N/A (no regresa valores)
# Descripcion: dibuja una rectangulo dados 2 pixeles (donde empieza y donde termina)
# lo rellena utilizando un for, creando curvas de 90º
def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    x =  pow(abs(start.x - end.x),2)
    y = pow(abs(start.y - end.y),2)
    diam = pow((x+y), (1/2))
    circumfrence = math.pi * diam
    step_size = circumfrence / 360
    for _ in range(360):
        forward(step_size)
        left(1)
        
    end_fill()

def rectangle(start, end):
    "Draw rectangle from start to end."
    
    pass  # TODO

def triangle(start, end):
    "Draw triangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.x)
        left(60)

    end_fill()

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda:color('orange'), 'O')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()