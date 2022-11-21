import turtle
import random

def draw(t):
    t.pendown()
    t.circle(100,90)
    t.left(90)
    t.circle(100,90)
    x = random.randint(0,180)
    y = random.randint(0,180)
    t.penup()
    t.goto(x,y)

def main():
    num = int(input("Ingresar el numero de petalos deseados: "))
    n = 0
    wnd = turtle.Screen()
    turtle.setup(600,600)
    miky = turtle.Turtle()
    while n < num:
        draw(miky)
        n = n + 1

    wnd.exitonclick()

if __name__ == "__main__":
    main()