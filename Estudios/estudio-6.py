import galapagar

NUMERO_DE_ESTUDIO = 6
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
    
    t = galapagar.new_turtle("green",1,"turtle")
    l = 100
    a = 50

    for i in range(1,4):
        galapagar.rectangle(t,l,a,ANCHURA_VENTANA/4 - i*(2*l + 7), ALTURA_VENTANA/4 - a)
        galapagar.rectangle(t,l,a,ANCHURA_VENTANA/4 - i*(2*l + 7), ALTURA_VENTANA/4 - 2*a - 13)
        galapagar.rectangle(t,l,a,ANCHURA_VENTANA/4 - i*(2*l + 7), ALTURA_VENTANA/4 - 3*a - 26)

    galapagar.finish(the_window)

main()
