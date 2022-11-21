import turtle

def draw(t,x):
    t.pendown()
    t.right(120)
    t.forward(100 + x)


def main():
    wnd = turtle.Screen()
    turtle.setup(600,600)
    miky = turtle.Turtle()
    x = 20
    n = 0
    miky.left(90)    
    while n < 20:
        draw(miky,x)
        x = x + 10
        n = n + 1

    wnd.exitonclick()

if __name__ == "__main__":
    main()
