from microbit import *
import gigglebot

def main():
    # Número de lados del polígono (cuanto más lados, más se aproxima al círculo)
    num_lados = 100
    # Radio del círculo (en cm)
    radio = 40
    # Distancia que debe avanzar el robot en cada paso (calculada como el arco de un círculo de radio 'radio')
    distancia = 2*3.14*radio/num_lados
    # Ángulo que se forma entre cada lado del polígono (en grados)
    angulo = (360/num_lados)
    # Fija la velocidad de los motores izquierdo y derecho a 50 (de -100 a 100)
    gigglebot.set_speed(50, 50)
    # Repite el proceso el número de veces necesario para completar el polígono
    for i in range(num_lados):
        # Gira el robot hacia la izquierda el ángulo calculado
        radians = angulo * (3.14/180)
        radians_sec = 50 * 0.07283185
        tiempo = radians / radians_sec
        gigglebot.turn(gigglebot.LEFT, tiempo*1000)
        # Avanza una distancia determinada
        gigglebot.drive(gigglebot.FORWARD, distancia/50 * 1000)

if __name__ == "__main__":
    main()
