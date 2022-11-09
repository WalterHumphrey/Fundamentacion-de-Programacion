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
    
    t = galapagar.new_turtle("green",10,"turtle")
    l = 100
    a = 50
    
    for i in range(1,4):
        d = 0
        if i == 1:
            inc = -1
            d = -7
        elif i == 2:
            inc = 1
            d = 0
        else:
            inc = 3
            d = 7

        galapagar.rectangle(t,l,a,-50*inc-d,25+13)
        galapagar.rectangle(t,l,a,-50*inc-d,-25)
        galapagar.rectangle(t,l,a,-50*inc-d,-75-13)

    galapagar.finish(the_window)

main()
