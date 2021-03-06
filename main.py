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
# Descripcion: dibuja un cuadrado dados 2 pixeles (donde empieza y donde termina)
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
    
# La función se llama circle
# parametro de entrada: start y end
# parametro de salida: N/A (no regresa valores)
# Descripcion: dibuja un círculo dados 2 pixeles (donde empieza y donde termina)
# calcula el diámetro y la circunferencia y lo rellena.
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

# La función se llama rectangle
# parametro de entrada: start y end
# parametro de salida: N/A (no regresa valores)
# Descripcion: dibuja una rectangulo dados 2 pixeles (donde empieza y donde termina)
# lo rellena utilizando un for, creando curvas de 90º
def rectangle(start, end):
    "Draw rectangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    
    forward(start.x - end.x)
    right(90)
    forward(start.y - end.y)
    left(90)
    forward(end.x - start.x)
    right(90)
    forward(end.y - start.y)

    end_fill()
    
# La función se llama triangle
# parametro de entrada: start y end
# parametro de salida: N/A (no regresa valores)
# Descripcion: dibuja una triágulo dados 2 pixeles (donde empieza y donde termina)
# lo rellena utilizando un for, creando curvas o vuelta de 60º
def triangle(start, end):
    "Draw triangle from start to end."
    pass  # TODO
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.x)
        left(60)

    end_fill()

# la funcion tap ayuda a definir los puntos donde se empieza y donde termina
# estos son los parametros que toman las demas funciones para dibujar las figuras
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

# ayuda a definir los defaults
def store(key, value):
    "Store value in state at key."
    state[key] = value
state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
# estos son los diferentes colores y figuras que se pueden dibujar al presionar la letra del teclado correspondiente
# la funcion 'onkey' tiene como parametros una funcion sin argumentos y una tecla
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