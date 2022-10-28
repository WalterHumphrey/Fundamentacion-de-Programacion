import galapagar
import turtle

NUMERO_DE_ESTUDIO = 1
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
    t.pencolor("red")
    l = 50 
    galapagar.square(t,l,-ANCHURA_VENTANA/2, ALTURA_VENTANA/2)

    galapagar.square(t,l,ANCHURA_VENTANA/2 - l, ALTURA_VENTANA/2)

    galapagar.square(t,l,-ANCHURA_VENTANA/2, -ALTURA_VENTANA/2 + l)

    galapagar.square(t,l,ANCHURA_VENTANA/2 - l, -ALTURA_VENTANA/2 + l)

    galapagar.finish(the_window)

main()
