import radio
from microbit import display, sleep
import gigglebot

def main():
    radio.on()

    BEACON_GROUP   = 41
    POWER_RE       = 7
    B1 = "00:3"
    B2 = "00:5"
    B3 = "00:7"
    umbral_dBm = -50
    giro = True

    gigglebot.set_speed(50, 50)

    while True:
        radio.config(power = POWER_RE, group = BEACON_GROUP, queue=1)
        received = radio.receive_full()
        if received != None:
            msg = received[0]
            dBm = received[1]
            msg = str(msg[3:], 'utf8')
            #display.scroll(msg, 200)
            if dBm < umbral_dBm:
                if giro == True:
                    gigglebot.turn(gigglebot.LEFT,1000)
                    giro = not giro
                else:
                    gigglebot.turn(gigglebot.RIGHT,1000)
                    giro = not giro
                gigglebot.drive(gigglebot.FORWARD, 3000)
            else:
                gigglebot.drive(gigglebot.FORWARD, 3000)
        sleep(500)

if __name__ == "__main__":
    main()
