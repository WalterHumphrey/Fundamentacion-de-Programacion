import galapagar
import turtle

NUMERO_DE_ESTUDIO = 2
ANCHURA_VENTANA = 500
ALTURA_VENTANA = 500

def main():

    the_window = galapagar.init("Estudio " + str(NUMERO_DE_ESTUDIO),
                                "lightgray",
                                ANCHURA_VENTANA,
                                ALTURA_VENTANA)

    ###
    #
    # Escribe aquí el código del estudio
    #
    # ...

    t = turtle.Turtle()
    t.pencolor("green")
    t.pensize(5)
    t.shape("turtle")
    an = 100
    al = 50
    galapagar.rectangle(t,an,al,-ANCHURA_VENTANA/2, ALTURA_VENTANA/2)

    galapagar.rectangle(t,an,al,ANCHURA_VENTANA/2 - an, ALTURA_VENTANA/2)

    galapagar.rectangle(t,an,al,-ANCHURA_VENTANA/2, -ALTURA_VENTANA/2 + al)

    galapagar.rectangle(t,an,al,ANCHURA_VENTANA/2 - an, -ALTURA_VENTANA/2 + al)

    t.pencolor("blue")
    t.pensize(2)
    t.shape("triangle")
    l = 60

    galapagar.square(t,l,-ANCHURA_VENTANA/2, ALTURA_VENTANA/2)

    galapagar.square(t,l,ANCHURA_VENTANA/2 - l, ALTURA_VENTANA/2)

    galapagar.square(t,l,-ANCHURA_VENTANA/2, -ALTURA_VENTANA/2 + l)

    galapagar.square(t,l,ANCHURA_VENTANA/2 - l, -ALTURA_VENTANA/2 + l)


    galapagar.finish(the_window)

main()
