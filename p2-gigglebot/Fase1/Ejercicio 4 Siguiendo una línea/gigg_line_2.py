from microbit import *
import gigglebot

# Detección de negro
NEGRO = 100

def main():
    # Declaramos velocidades
    gigglebot.set_speed(50, 50)
    # Iniciamos leds
    strip = gigglebot.init()
    while True:
        # Apagamos leds
        strip[2] = (0, 0, 0)
        strip[8] = (0, 0, 0)

        # Leemos los valores del sensor
        values = gigglebot.read_sensor(gigglebot.LINE_SENSOR, gigglebot.BOTH)

        # Si ambos sensores detectan negro el robot avanza
        if values[0] < NEGRO and values[1] < NEGRO:
            gigglebot.drive(gigglebot.FORWARD, 50)
        # Si solo uno de ellos detecta negro, el robot gira ligeramente y enciende led
        elif values[0] < NEGRO:
            strip[2] = (255, 0, 0)
            gigglebot.turn(gigglebot.RIGHT,25)
        elif values[1] < NEGRO:
            strip[8] = (255, 0 ,0)
            gigglebot.turn(gigglebot.LEFT,25)
        strip.show()

if __name__ == "__main__":
    main()
