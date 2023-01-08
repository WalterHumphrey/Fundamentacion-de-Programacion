import radio
from microbit import sleep, display, Image

def main():
    # String con un identificador del emisor, cámbialo para no coincidir con el
    # de otros microbits que puedan estar transmitiendo cerca de ti
    IDENTIFIER = "MB_310"

    # Periodo de emisión del mensaje, en milisegundos
    PERIOD = 10000

    # Enciende la radio
    radio.on()

    # Establece la potencia de la emisión, de 0 a 7 siendo 7 la potencia máxima
    # Mira la documentación para ver otros parámetros que pueden fijarse en radio.config()
    radio.config(power=7,group=41)

    while True:
        # Muestra dos recuadros en pantalla para indicar que va a enviar un mensaje
        display.show(Image.SQUARE_SMALL)
        sleep(500)
        # Envía el mensaje
        radio.send(IDENTIFIER)
        display.show(Image.SQUARE)
        sleep(500)
        display.clear()
        sleep(PERIOD-1000)  # ya se han esperado 1000ms al mostrar las imágenes

if __name__ == "__main__":
    main()
