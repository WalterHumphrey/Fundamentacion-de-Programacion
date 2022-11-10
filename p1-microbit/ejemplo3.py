###################################################################
#
# Muestra en mu-editor el Trazador y REPL y observa los valores.
#
# Comenta la sentencia sleep y observa lo que ocurre. Prueba a
# cambiar el valor de milisegundos
#
from microbit import *

def main():
    while True:
        accel_x = accelerometer.get_x()
        accel_y = accelerometer.get_y()
        accel_z = accelerometer.get_z()

        print((accel_x, accel_y, accel_z))
        sleep(200)

if __name__ == "__main__":
    main()
