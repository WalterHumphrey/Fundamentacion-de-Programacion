import galapagar

NUMERO_DE_ESTUDIO = 5
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
    
    t = galapagar.new_turtle("blue",1,"turtle")
    l = 100

    for i in range(1,4):
        galapagar.square(t,l,ANCHURA_VENTANA/2 - i*(l + 5), ALTURA_VENTANA/2 - l)
        galapagar.square(t,l,ANCHURA_VENTANA/2 - i*(l + 5), ALTURA_VENTANA/2 - 2*l - 5)

    galapagar.finish(the_window)

main()
