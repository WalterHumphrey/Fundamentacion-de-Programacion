from microbit import *
import gigglebot
import radio

def main():
    gigglebot.set_speed(50, 50)

    # Inicializar variables para almacenar la información de las balizas
    baliza_id = 0
    potencia_maxima = 0

    THRESHOLD = 100

    radio.on()
    A = True

    # Diccionario para almacenar los identificadores y potencias de las balizas
    balizas = {}

    # Repetir constantemente
    while True:
        # Revisar los mensajes de radio que se están recibiendo
        radio.config(group=41)
        mensaje = radio.receive_full()
        display.show('B')
        if mensaje != None:
            # Descomponer el mensaje en sus componentes
            msg = mensaje[0]
            dBm = mensaje[1]
            baliza_id = int(msg[6:])
            display.show('R')
            print(baliza_id)

            # Guardamos el mensaje en el diccionario
            balizas[baliza_id] = dBm
            print(balizas)
        # Si se ha seleccionado una baliza, mover el robot hacia ella
        if len(balizas) == 3:
            # Seleccionamos la baliza con mayor potencia
            identificador_baliza_seleccionada = max(mensajes, key=mensajes.get)
            if potencia  < -35:
                # Usar el sensor de línea para evitar obstáculos mientras se avanza
                #values = gigglebot.read_sensor(gigglebot.LINE_SENSOR, gigglebot.BOTH)
                print('se mueve')
                print(dBm)
                #if values[0] < THRESHOLD:
                    # Girar a la derecha para evitar el obstáculo
                #    gigglebot.turn(gigglebot.LEFT,500)
                #if values[1] < THRESHOLD:
                #    gigglebot.turn(gigglebot.RIGHT,500)
                #else:
                    # Avanzar hacia la baliza
                #    gigglebot.drive(gigglebot.FORWARD, 4000)
            elif potencia > -35:
                # Revisar si se ha llegado a la baliza
                radio.config(power = 1, group = baliza_id)
                while A:
                    radio.send("01:dameSecreto")
                    mensaje = radio.receive_full()

                    if mensaje != None:
                        msg = mensaje[0]
                        msg = str(msg[3:], 'utf8')
                        print('dameSecreto')
                        # Mostrar el mensaje secreto en la pantalla
                        display.scroll(msg)
                        print(msg)

                        # Reiniciar la búsqueda de balizas
                        baliza_id = 0
                        potencia_maxima = 0

                        # Detener el robot
                        #gigglebot.stop()
                        A = False
                    sleep(500)
                # Esperar un poco antes de volver a revisar los mensajes de
                A = True
        sleep(1000)
if __name__ == "__main__":
    main()
