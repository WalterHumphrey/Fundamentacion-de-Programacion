from microbit import *
import gigglebot

# umbral de detección de negro
THRESHOLD = 100

def main():
    strip = gigglebot.init()
    while True:
        strip[2] = (0, 0, 0)
        strip[8] = (0, 0, 0)
        values = gigglebot.read_sensor(gigglebot.LINE_SENSOR, gigglebot.BOTH)
        if values[0] < THRESHOLD:
            strip[2] = (255, 0, 0)
        if values[1] < THRESHOLD:
            strip[8] = (255, 0 ,0)
        strip.show()
        sleep(200)

if __name__ == "__main__":
    main()
