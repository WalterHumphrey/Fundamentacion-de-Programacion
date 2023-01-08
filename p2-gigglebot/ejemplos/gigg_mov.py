from microbit import *
import gigglebot

def main():

    # Fija la velocidad de los motores izquierdo, derecho, de -100 a 100.
    # Si la velocidad es negativa, el motor gira hacia atrás.
    # Si la velocidad de los dos motores es la misma, el robot debería
    # avanzar recto hacia adelante, si no lo hiciera, ajusta levemente la
    # velocidad de uno de los dos motores
    gigglebot.set_speed(50, 50)

    # Mueve los dos motores a la velocidad fijada, y
    # hacia adelante si la velocidad fijada es positiva
    # El segundo argumento es el número de milisegundos, transcurridos los
    # cuales los motores se paran.
    gigglebot.drive(gigglebot.FORWARD, 1000)

    # Mueve los dos motores a la velocidad fijada, y
    # hacia atrás si la velocidad fijada es positiva
    # El segundo argumento es el número de milisegundos, transcurridos los
    # cuales los motores se paran
    gigglebot.drive(gigglebot.BACKWARD, 1000)

    sleep(1000)

    # Gira el robot hacia la izquierda si la velocidad fijada es positiva,
    # girando uno de los dos motores
    # El segundo argumento es el número de milisegundos, transcurridos los
    # cuales los motores se paran
    gigglebot.turn(gigglebot.LEFT,500)

    # Gira el robot hacia la derecha si la velocidad fijada es positiva,
    # girando uno de los dos motores
    # El segundo argumento es el número de milisegundos, transcurridos los
    # cuales los motores se paran
    gigglebot.turn(gigglebot.RIGHT,500)

    # Para el robot (innecesario en este ejemplo)
    gigglebot.stop()

    # NOTA: Sin especificar en estas funciones un tiempo, el movimiento
    # será indefinido, hasta que se llame a otra de las funciones o a stop()

if __name__ == "__main__":
    main()
