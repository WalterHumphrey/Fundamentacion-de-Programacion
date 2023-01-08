from microbit import *
import radio

# Inicializamos la radio
radio.on()

# Lista de ordenes
ordenes = ["FORWARD", "BACKWARD", "RIGHT", "LEFT", "STOP"]

# Posición actual en la lista de ordenes
posicion_actual = 0

while True:
    # Configuramos radio a maximo poder y en grupo 3
    radio.config(power=7,group=3)
    
    # Si se pulsa el boton A, se envia la orden de la posición actual y se avanza la posicion en 1
    if button_a.is_pressed():
        # Enviamos orden
        radio.send(ordenes[posicion_actual])
        # Mostramos en display
        display.show(ordenes[posicion_actual])
        posicion_actual += 1
        # Si se llega al final de la lista regresamos la posicion 0
        if posicion_actual == len(ordenes):
            posicion_actual = 0

    # Si se pulsa el boton B, se envia la orden contraria a la de la posición actual y se retrocede la posicion en 1
    elif button_b.is_pressed():
        # Cambio a orden contraria
        if ordenes[posicion_actual] == "FORWARD":
            orden_contraria = "BACKWARD"
        elif ordenes[posicion_actual] == "BACKWARD":
            orden_contraria = "FORWARD"
        elif ordenes[posicion_actual] == "RIGHT":
            orden_contraria = "LEFT"
        elif ordenes[posicion_actual] == "LEFT":
            orden_contraria = "RIGHT"
        else:
            orden_contraria = "STOP"
        # Enviamos orden
        radio.send(orden_contraria)
        # Mostramos en el display
        display.show(orden_contraria)
        posicion_actual -= 1
        # Si se llega al principio de la lista pasamos a la ultima posicion
        if posicion_actual < 0:
            posicion_actual = len(ordenes) - 1
