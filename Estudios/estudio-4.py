import galapagar

NUMERO_DE_ESTUDIO = 3
ANCHURA_VENTANA = 800
ALTURA_VENTANA = 800

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
    
    t = galapagar.new_turtle("red",5,"turtle")
    l = 100

    # Fila 1
    galapagar.square(t,l,-ANCHURA_VENTANA/2, -ALTURA_VENTANA/2 + 3*l)

    galapagar.square(t,l,-ANCHURA_VENTANA/2 + l, -ALTURA_VENTANA/2 + 3*l)

    galapagar.square(t,l,-ANCHURA_VENTANA/2 + 2*l, -ALTURA_VENTANA/2 + 3*l)

    galapagar.square(t,l,-ANCHURA_VENTANA/2 + 3*l, -ALTURA_VENTANA/2 + 3*l)

    # Fila 2 
    galapagar.square(t,l,-ANCHURA_VENTANA/2, -ALTURA_VENTANA/2 + 2*l)

    galapagar.square(t,l,-ANCHURA_VENTANA/2 + l, -ALTURA_VENTANA/2 + 2*l)

    galapagar.square(t,l,-ANCHURA_VENTANA/2 + 2*l, -ALTURA_VENTANA/2 + 2*l)

    galapagar.square(t,l,-ANCHURA_VENTANA/2 + 3*l, -ALTURA_VENTANA/2 + 2*l)

    # Fila 3
    galapagar.square(t,l,-ANCHURA_VENTANA/2, -ALTURA_VENTANA/2 + l)

    galapagar.square(t,l,-ANCHURA_VENTANA/2 + l, -ALTURA_VENTANA/2 + l)

    galapagar.square(t,l,-ANCHURA_VENTANA/2 + 2*l, -ALTURA_VENTANA/2 + l)

    galapagar.square(t,l,-ANCHURA_VENTANA/2 + 3*l, -ALTURA_VENTANA/2 + l)

    # Fila 4
    galapagar.square(t,l,-ANCHURA_VENTANA/2, -ALTURA_VENTANA/2)

    galapagar.square(t,l,-ANCHURA_VENTANA/2 + l, -ALTURA_VENTANA/2)

    galapagar.square(t,l,-ANCHURA_VENTANA/2 + 2*l, -ALTURA_VENTANA/2)

    galapagar.square(t,l,-ANCHURA_VENTANA/2 + 3*l, -ALTURA_VENTANA/2)


    galapagar.finish(the_window)

main()
