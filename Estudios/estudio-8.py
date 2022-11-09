import galapagar

NUMERO_DE_ESTUDIO = 7
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
    l = 200
    inc = 0
    l2 = 340
    inc2 = 0

    for i in range(1,11):
        galapagar.square(t,l-inc,-ANCHURA_VENTANA/4-l+inc/2,ALTURA_VENTANA/2-l+inc/2)
        galapagar.square(t,l2-inc2,ANCHURA_VENTANA/2-l2-inc2/2,ALTURA_VENTANA/2-l2-inc2/2)
        inc += 20
        inc2 +=24

    galapagar.finish(the_window)

main()
