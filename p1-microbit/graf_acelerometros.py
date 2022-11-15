from microbit import *

# Maximo de tuplas en lista
MAX = 100

# Funcion para calcular aceleracion maxima
def max_a(acc,j):
    r = acc[0] # r toma el valor de la primera aceleracion
    for a in range(j): # Recorremos la lista de aceleraciones hasta donde se hayan tomado medidas
        if r < acc[a]: # Si la aceleracion a comparar es mayor a r, r toma su valor
            r = acc[a]
    return r # Se regresa r (aceleracion maxima)

# Funcion para calcular aceleracion minima
def min_a(acc,j):
    r = acc[0] # r toma el valor de la primera aceleracion
    for a in range(j): # Recorremos la lista de aceleraciones hasta donde se hayan tomado medidas
        if r > acc[a]: # Si la aceleracion a comparar es menor a r, r toma su valor
            r = acc[a]
    return r # Se regresa r (aceleracion minima)

def main():
    # Lista de tuplas de tamaño MAX
    readings = [(0, 0, 0)] * MAX

    # Creamos lista para aceleracion en cada eje
    ax = [0] * MAX
    ay = [0] * MAX
    az = [0] * MAX

    # Contador lecturas
    i = 0

    # Contador para promedios
    j = 0
    while True:
        # Suma 1 al contador para promedios
        j = j + 1
        # Rellenamos la lista con tupla de aceleraciones
        readings[i] = accelerometer.get_values()
        # Separamos aceleraciones por eje en listas
        ax[i] = readings[i][0]
        ay[i] = readings[i][1]
        az[i] = readings[i][2]

        # Calculamos el promedio de aceleracion por eje cuando readings no tiene MAX datos
        if j < MAX:
            meanx = sum(ax) / j
            meany = sum(ay) / j
            meanz = sum(az) / j

        # Calculamos el promedio de aceleracion por eje cuando reading tiene MAX datos
        else:
            meanx = sum(ax) / MAX
            meany = sum(ay) / MAX
            meanz = sum(az) / MAX
        # Imprimimos en trazador el promedio de aceleraciones por eje
        print( (meanx,meany,meanz) )

        # Si el boton a es presionado desplegamos en el diplay la aceleracion maxima por eje
        if button_a.is_pressed():
            max_r = "Max x= " + str(max_a(ax,j)) + "Max y= " + str(max_a(ay,j)) + "Max z= " + str(max_a(az,j))
            display.scroll(max_r)

        # Si el boton a es presionado desplegamos en el diplay la aceleracion minima por eje
        if button_b.is_pressed():
            min_r = "Min x= " + str(min_a(ax,j)) + "Min y= " + str(min_a(ay,j)) + "Min z= " + str(min_a(az,j))
            display.scroll(min_r)

        # Sumamos 1 al contador de lecturas para rellenar la lista
        i += 1
        # Si llegamos al tamaño maximo comenzamos a sobreescribir reiniciando el contador
        if i == MAX:
            i = 0
        sleep(200)

if __name__ == "__main__":
    main()
