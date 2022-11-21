import turtle

#Funcion para dibujar la tortuga
def draw(t,s,g):
    t.pendown()
    for x in range(0,4): #Crea el cuadro
        t.right(90)
        t.forward(s)
    t.left(g)   #Cambia de angulo para el siguiente cuadro

def main():
    num = int(input("Ingresar el numero de cuadros deseados: "))
    size = int(input("Tamaño de los cuadros: "))
    grad = int(input("Ángulo entre los cuadros: "))

    n = 0
    wnd = turtle.Screen()
    turtle.setup(600,600)
    miky = turtle.Turtle()
    while n < num:  #Dibuja la cantidad de cuadrados deseados
        draw(miky,size,grad)
        n = n + 1

    wnd.exitonclick()

if __name__ == "__main__":
    main()