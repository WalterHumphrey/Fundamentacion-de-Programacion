import turtle
import random

t = turtle.Turtle()
turtle.screensize(500,500)

def draw_pet(n):
    for i in range(n):
        t.pd()
        t.circle(100,90)
        t.left(90)
        t.circle(100,90)
        t.left(random.randint(0,360))
        t.pu()
        pos = random.randint(-200,200)
        t.goto(pos,pos)

draw_pet(int(input("Numero de petalos: ")))
turtle.done()