import turtle
import random

def estaDentroAzar(t):
    resultado = True
    prob = random.random()
    #Con un 10% de probabilidad considero que "está afuera"
    if prob < 0.1:
        resultado = False
    return resultado


def estaDentro(t):
    resultado = True
    x = t.xcor()
    y = t.ycor()
    if x > 300 or x < -300 or y > 300 or y < -300:
        resultado = False
    return resultado


def main():
    wnd = turtle.Screen()
    turtle.setup(600,600)
    leo = turtle.Turtle()
    
    #Cara = 1
    #Cruz = 2
    while estaDentro(leo):
        if random.randrange(1,3) == 1: 
            leo.left(90)
        else:
            leo.right(90)
        leo.forward(50) 

    wnd.exitonclick()

if __name__ == "__main__":
    main()