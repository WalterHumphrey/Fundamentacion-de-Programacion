from microbit import *
import gigglebot

def main():
    while True:
        LUZ = 20
        # Obtenemos valores del sensor
        values = gigglebot.read_sensor(gigglebot.LIGHT_SENSOR, gigglebot.BOTH)
        total_values = values[0] + values[1]

        # Declaramos velocidades
        gigglebot.set_speed(50, 50)

        # Si la suma de ambos sensores supera el umbral de luz, el robot avanza siguiendo la luz.
        # De lo contrario gira hasta encpntrar luz.
        if total_values < LUZ:
            gigglebot.turn(gigglebot.RIGHT,500)
        else:
            gigglebot.drive(gigglebot.FORWARD, 500)

if __name__ == "__main__":
    main()
