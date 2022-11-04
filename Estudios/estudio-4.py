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

    for i in range(0,4):
        for j in range(0,4):
            galapagar.square(t,l,-ANCHURA_VENTANA/2 + i*l, -ALTURA_VENTANA/2 + j*l)

    galapagar.finish(the_window)

main()
