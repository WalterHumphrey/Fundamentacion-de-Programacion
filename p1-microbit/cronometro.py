from microbit import *

# Codigo para desplegar cada numero
zero = "99999:99999"
one = "00000:99999"
two = "90999:99909"
three = "90909:99999"
four = "99900:09999"
five = "99909:90999"
six = "99999:90999"
seven = "90900:99999"
eight = "99099:99099"
nine = "99900:99999"
null = "00000:00000"

# Tupla con todos los numeros
fonts = (zero, one, two, three, four, five, six, seven, eight, nine)

# Funcion para desplegar en el display (recibe el numero y un selector)
def dis_num(num,sel):
    # Dividimos por columna
    number = num.split(":")
    # Recorremos las 5 filas
    for y in range(5):
        # 2 columnas
        for i in range(2):
            # Primera pasada despliega en columa 0 o 3 y segunda pasada en columna 1 o 4
            if i < 1:
                # Si el selector es 1 desplegamos en columna 3, de lo contrario en la 0
                if sel == 1:
                    display.set_pixel(3, y,int(number[0][y]))
                else:
                    display.set_pixel(0, y,int(number[0][y]))
            else:
                # Si el selector es 1 desplegamos en columna 4, de lo contrario en la 1
                if sel == 1:
                    display.set_pixel(4, y,int(number[1][y]))
                else:
                    display.set_pixel(1, y,int(number[1][y]))

# Funcion que llama a dis_num dependiendo si hay 1 o 2 digitos
def digito(n):
    # Convertimos numero a string
    sn = str(n)
    # Antes de los 10 segundos solo despliega 1 digito
    if n < 10:
        sn = "0" + str(n) # Ajuste de tamaño de string
        dis_num(null,2) # Apagamos leds columnas 0 y 1
    else:
        n2 = int(sn[0]) # Digito columnas 0 y 1
        dis_num(fonts[n2],2) # Funcion para desplegar digito en columnas 0 y 1
    n1 = int(sn[1]) # Digito columnas 3 y 4
    dis_num(fonts[n1],1) # Funcion para desplegar digito en columnas 3 y 4

def main():
    # Variables de tiempo
    seg = 0
    m = 0
    h = 0

    while True:
        # A los 59 segundos reiniciamos su valor y sumamos 1 minuto
        if seg > 59:
            seg = 0
            m +=1
            # A los 59 minutos reiniciamos el valor de minutos y segundos y sumamos 1 hora
            if m > 59:
                seg = 0
                m = 0
                h += 1
                # A las 23 horas reiniciamos todos los valores
                if h > 23:
                    seg = 0
                    m = 0
                    h = 0

        # Desplegamos segundos
        digito(seg)

        # Mostrar horas si se presiona el boton A
        if button_a.is_pressed():
            # Si no ha pasado una hora los leds estaran apagados
            if h != 0:
                digito(h) # Desplegamos horas
            else:
                dis_num(null,1)
                dis_num(null,2)

        # Mostrar minutos si se presiona el boton B
        if button_b.is_pressed():
            # Si no ha pasado un minuto los leds estaran apagados
            if m != 0:
                digito(m) # Desplegamos minutos
            else:
                dis_num(null,1)
                dis_num(null,2)

        print("seg: ",seg)
        print("min: ",m)
        print("hor: ",h)
        sleep(1000) #  Cada ciclo durara 1 seg (muy aprox)
        seg += 1 # Aumentamos 1 segundo

if __name__ == "__main__":
    main()
