from microbit import *
import gigglebot

def main():
    strip = gigglebot.init()
    # Matriz con colores
    colors = [(255,255,255),(255,0,0),(0,255,0),(0,0,255),(255,255,0),(0,255,255),(255,0,255)]

    while True:
        # Ciclo para ir rotando colores por los leds
        for i in range(len(strip)):
            strip[2]= colors[(i+1) % len(colors)]
            strip[3]= colors[(i+2) % len(colors)]
            strip[4]= colors[(i+3) % len(colors)]
            strip[5]= colors[(i+4) % len(colors)]
            strip[6]= colors[(i+5) % len(colors)]
            strip[7]= colors[(i+6) % len(colors)]
            strip[8]= colors[(i+8) % len(colors)]
            strip.show()
            sleep(150)

if __name__ == "__main__":
    main()
