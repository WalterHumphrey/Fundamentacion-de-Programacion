from microbit import *
import gigglebot
import micropython

#
# NOTA: Las sentencias sleep() sólo se incluyen para que sea más
# fácil estudiar el comportamiento del programa
#

def main():
    # inicializa los neopixels
    gigglebot.init()
    sleep(2000)

    # enciende del color adecuado uno de los ojos:
    #   el primer parámetro identifica un ojo o los dos: LEFT, RIGHT o BOTH
    #   los siguientes parámetros son las componentes RGB del color (0-255)
    gigglebot.set_eyes(gigglebot.BOTH, 0, 255, 0)
    sleep(2000)

    # enciende de un mismo color todos los neopixels de la sonrisa:
    #   los parámetros son las componentes RGB del color (0-255)
    gigglebot.set_smile(100, 0, 100)
    sleep(2000)


    # init devuelve un objeto con una lista de tuplas con las componentes RGB
    # de cada neopixel.
    #   la posición 0 de la lista representa el color del ojo izquierdo
    #   la posición 1 de la lista representa el color del ojo derecho
    #   las posiciones 2-8 de la lista representan el color de los
    #     neopixels de la sonrisa, de izquierda a derecha

    strip = gigglebot.init()

    strip[2]=(248, 12, 18)
    strip[3]=(255, 68, 34)
    strip[4]=(255, 153, 51)
    strip[5]=(208, 195, 16)
    strip[6]=(34, 204, 170)
    strip[7]=(51, 17, 187)
    strip[8]=(68, 34, 153)

    # El método show() muestra en las sonrisa los colores almacenados en la
    # variable
    strip.show()

if __name__ == "__main__":
    main()
