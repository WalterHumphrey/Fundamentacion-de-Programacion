########################################################################
#
# En este otro caso las sentencias del bucle while se ejecutan si
# no está presionado el botón A. Si se presiona, la condición será
# falsa y no se ejecutarán las sentencias del bucle while,
# continuando la ejecución en la sentencia que viene después del bucle:
# display.clear()
#
from microbit import *

def main():
    while not button_a.is_pressed():
        display.show(Image.HAPPY)
        if accelerometer.was_gesture("shake"):
            display.show(Image.SAD)
            sleep(2000)

    display.clear()
    sleep(1000)
    display.scroll("FIN. Pulsa reset para reiniciar")

if __name__ == "__main__":
    main()
