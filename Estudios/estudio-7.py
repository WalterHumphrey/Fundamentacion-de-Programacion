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
    
    t = galapagar.new_turtle("black",1,"turtle")
    l = 10
    inc = 0

    for i in range(1,11):
         galapagar.square(t,l+inc,-l/2-inc/2,-l/2-inc/2)
         inc += 6

    galapagar.finish(the_window)

main()
