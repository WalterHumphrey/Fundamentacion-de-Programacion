from microbit import *
import radio
import gigglebot

# Inicializamos la radio
radio.on()

# Decalramos velocidades
gigglebot.set_speed(50, 50)

while True:
    # Configuramos radio a maximo poder, grupo 3 y reducimos la queue a 1 mensaje
    radio.config(power=7,group=3,queue=1)
    # Esperamos a recibir orden
    orden = radio.receive()
    if orden != None:
        display.show(orden)
        # Si la orden es "FORWARD", el robot avanza 1 segundo
        if orden == "FORWARD":
            gigglebot.drive(gigglebot.FORWARD, 1000)
        # Si la orden es "BACKWARD", el robot retrocede 1 segundo
        elif orden == "BACKWARD":
            gigglebot.drive(gigglebot.BACKWARD, 1000)
        # Si la orden es "RIGHT", el robot gira a la derecha 0.5 segundos
        elif orden == "RIGHT":
            gigglebot.turn(gigglebot.RIGHT, 500)
        # Si la orden es "LEFT", el robot gira a la izquierda 0.5 segundos
        elif orden == "LEFT":
            gigglebot.turn(gigglebot.LEFT, 500)
        # Si la orden es "STOP", se detiene el robot
        else:
            gigglebot.stop()
    sleep(1000)
