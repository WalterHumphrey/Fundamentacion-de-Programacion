"""Código para realizar los ejercicios de la asignatura Fundamentos de
Programación del grado en Ingeniería de Robótica Software de nombre:
"Estudios sobre abstracción funcional para Python y cuarteto de galápagos"
"""

import turtle

def init(title, color, width, height):
    """
    Crea una ventana para poder dibujar con el módulo de python turtle

    Parámetros: título, color de fondo, ancho y alto de la ventana creada
    Devuelve: la ventana creada.
    """

    window = turtle.Screen()
    turtle.setup(width, height)
    window.bgcolor(color)
    window.title(title)

    return window


def finish(window):
    """
    Espera a que se haga click en window para cerrar la ventana.
    Se debe llamar al final de un programa que use turtle.

    Parámetros: una ventana creada por init()
    """

    window.exitonclick()

def square(t,l,x,y):
    t.pu()
    t.setpos(x,y)
    t.pd()
    for i in range(4):
        t.forward(l)
        t.left(90)
    t.pu()
    t.setpos(0,0)
    t.pd()
    return

def rectangle(t,an,al,x,y):
    t.pu()
    t.setpos(x,y)
    t.pd()
    for i in range(2):
        t.forward(an)
        t.left(90)
        t.forward(al)
        t.left(90)
    t.pu()
    t.setpos(0,0)
    t.pd()
    return

def new_turtle(color,psize,shape):
    t = turtle.Turtle()
    t.pencolor(color)
    t.pensize(psize)
    t.shape(shape)
    return t