from microbit import *
import gigglebot

def main():
    while True:
        if button_a.was_pressed():
            # Obtiene la lectura de los sensores de línea
            # El segundo parámetro puede ser LEFT, RIGHT o BOTH
            # Si se lee un sólo sensor, devuelve un entero
            # Si se leen los dos sensores, se devuelve una tupla de 2 enteros (izquierdo, derecho)
            # Los valores devueltos están entre 0 y 1024, cuanto mayor, más clara es la superficie
            # sobre la que se encuentra el robot.
            values = gigglebot.read_sensor(gigglebot.LINE_SENSOR, gigglebot.BOTH)
            display.scroll(str(values[0]) + " # " + str(values[1]))

if __name__ == "__main__":
    main()