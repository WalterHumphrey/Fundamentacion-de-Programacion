from microbit import *
import gigglebot

def main():
    finish = False
    while not finish:
        # Obtiene la lectura de los sensores de luz
        # El segundo parámetro puede ser LEFT, RIGHT o BOTH
        # Si se lee un sólo sensor, devuelve un entero
        # Si se leen los dos sensores, se devuelve una tupla de 2 enteros (izquierdo, derecho)
        # Los valores devueltos están entre 0 y 1024, cuanto mayor, más luz detectada.
        values = gigglebot.read_sensor(gigglebot.LIGHT_SENSOR, gigglebot.BOTH)
        print(values)
        sleep(1000)

        # Si se pulsa algún botón del microbit, se sale de bucle y termina el programa
        if button_a.was_pressed() or button_a.was_pressed():
            finish = True
if __name__ == "__main__":
    main()

