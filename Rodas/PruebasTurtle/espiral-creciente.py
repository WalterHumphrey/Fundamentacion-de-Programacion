import turtle

#Funcion para dibujar el escpiral creciente, usando: turtle, radio, grados, pensize
def draw(t,l,g,p):
    t.pendown()
    t.circle(l,g)
    t.pensize(p)

def main():
    size = float(input("Incremento de longitud: "))
    grad = float(input("Ángulo previo a cambio: "))
    wnd = turtle.Screen()
    turtle.setup(600,600)
    miky = turtle.Turtle()
    x = size
    pen = 1
    n = 0
    while n < 800:
        draw(miky,size,grad,pen)
        size = size + x
        pen = pen + 0.03
        n = n + 1

    wnd.exitonclick()

if __name__ == "__main__":
    main()
