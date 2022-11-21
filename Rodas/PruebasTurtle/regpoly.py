import turtle

#Funcion para dibujar el espiral
def draw(t,n,x):
    total = 180*(n-2) #Calculo de los grados internos del polinomio
    t.pendown()
    t.right(180-(total/n)) #Calculo para obtener cada cambio de direccion necesario para generar el polinomio
    t.forward(x)

#Funcion principal
def main():
    lados = int(input("Lados: "))
    tamaño = int(input("Tamaño: "))
    wnd = turtle.Screen() #Crea la ventana del turtle
    turtle.setup(600,600) 
    
    #Miguelangel
    miky = turtle.Turtle() #Crea a la tortuga
    n = 0
    miky.penup()
    miky.pencolor("orange")
    miky.goto(-150,150)   #Posicion de Miky
    while n < lados:
        draw(miky,lados,tamaño)
        n = n + 1

    #Leonardo
    leo = turtle.Turtle() #Crea a la tortuga
    n = 0
    leo.penup()
    leo.color("blue")
    leo.goto(150,150)   #Posicion de Leo
    while n < lados:
        draw(leo,lados,tamaño)
        n = n + 1        

    #Rafael
    rafa = turtle.Turtle() #Crea a la tortuga
    n = 0
    rafa.penup()
    rafa.color("red")
    rafa.goto(-150,-150)   #Posicion de Rafa
    while n < lados:
        draw(rafa,lados,tamaño)
        n = n + 1 

    #Donatelo
    dony = turtle.Turtle() #Crea a la tortuga
    n = 0
    dony.penup()
    dony.color("purple")
    dony.goto(150,-150)   #Posicion de Dony
    while n < lados:
        draw(dony,lados,tamaño)
        n = n + 1 

    wnd.exitonclick()

if __name__ == "__main__": #Correr el programa principal
    main()