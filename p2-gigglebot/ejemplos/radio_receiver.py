import radio
from microbit import display, sleep

def main():
    radio.on()

    while True:
        sleep(1000)

        # Intenta recoger un mensaje que haya llegado al microbit
        # Si no ha llegado ningún mensaje receive_full() devuelve None
        # Si ha llegado un mensaje, receive_full() devuelve una tupla de 3 valores:
        #   - una lista de bytes con el mensaje recibido
        #   - la potencia de señal recibida, en dBm, entre 0 (potencia máxima) y -255 (potencia mínima)
        #   - una marca de tiempo con el instante en que se recibió el mensaje
        radio.config(power=7,group=41)

        received = radio.receive_full()

        if received != None:
            # Separamos los 3 valores de la tupla. La marca de tiempo no la usaremos
            msg = received[0]
            dBm = received[1]
            ts = received[2]

            # En msg los primeros 3 bytes de la lista son una cabecera que descartamos
            # Convertimos el resto de bytes a un string con codificación UTF8
            identifier = str(msg[3:], 'utf8')

            # Muestra en el display el identificador recibido y la potencia de señal
            # con la que se recibió
            #    el segundo parámetro de scroll() permite variar la velocidad en que
            #    se muestra el texto (por defecto 150, cuanto más bajo más rápido se
            #    desplaza el texto)
            display.scroll(identifier + " # " + str(dBm), 200)


if __name__ == "__main__":
    main()
