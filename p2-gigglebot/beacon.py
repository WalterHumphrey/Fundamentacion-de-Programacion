import radio
from microbit import *

def main():
    PREFIX_BEACON  = "00:"
    SECRET_REQUEST = "01:dameSecreto"
    SECRET_MSG     = ["02:Madrid","02:Barcelona","02:Sevilla"]
    BEACON_GROUP   = 41
    BEACON_ID      = [3,5,7]
    POWER_BEACON   = 7
    POWER_SECRET   = 1
    PERIOD         = 1000
    current_index = 0


    radio.on()

    while True:
        # Send beacon
        display.scroll(BEACON_ID[current_index])

        if button_a.is_pressed():
            current_index += 1
            if current_index >= len(BEACON_ID):
                current_index = 0

        if button_b.is_pressed():
            while True:
                # Configurar la radio para transmitir el identificador de la baliza actual
                radio.config(power = POWER_BEACON, group = BEACON_GROUP)
                radio.send(PREFIX_BEACON + str(BEACON_ID[current_index]))
                # Mostrar alguna indicación visual de que se está transmitiendo el identificador
                display.show(Image.HEART)

                # If SECRET_REQUEST received then send SECRET_MSG
                radio.config(power = POWER_SECRET, group = BEACON_ID[current_index])
                for i in range(10):
                    received = radio.receive_full()
                    if received != None:
                        msg = received[0]
                        dBm = received[1]
                        msg = str(msg[3:], 'utf8')
                        if msg == SECRET_REQUEST:
                            display.show(msg[3:])
                            radio.send(SECRET_MSG[current_index])
                    sleep(PERIOD)

if __name__ == "__main__":
    main()
