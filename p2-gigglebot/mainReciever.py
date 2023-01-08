from microbit import *
import radio
import gigglebot

def lista(Lst_id_p, identifier, dBm, TOTAL_BALIZAS, Lst_ENCONTRADAS,BALIZAS_ENCONTRADAS):
    # Hace una lista con las identificaciones y las potencias

    iguales = 0

    for i in range(BALIZAS_ENCONTRADAS):
        if Lst_ENCONTRADAS[i][1] == identifier:
            iguales = 1

    if iguales == 0:
        if TOTAL_BALIZAS == 0 : #Primera baliza
            Lst_id_p = [(identifier, dBm)]
            TOTAL_BALIZAS = TOTAL_BALIZAS + 1
        elif TOTAL_BALIZAS != 0:
            for i in range(TOTAL_BALIZAS):
                if Lst_id_p[i][0] == identifier:
                    iguales = iguales +1

            if iguales == 0:# Hago una lista con las balizas y su potencia
                Lst_id_p = Lst_id_p + [(identifier, dBm)]
                TOTAL_BALIZAS = TOTAL_BALIZAS + 1
                return (Lst_id_p, TOTAL_BALIZAS)
            iguales = 0

    return (Lst_id_p, TOTAL_BALIZAS)

def mejor_baliza(L_I_P):
    # Busco la baliza con mayor potencia, la mas próxima al gigglebot

    # Parámetros: lista de las identificaciones y potencias obtenidas

    # Devuelve: tupla con la identificación y potencia de la baliza que buscamos

    Potencias_Mayores = 0

    if len(L_I_P) == 1:
        identificacion =  L_I_P[0][0]
        potencia =  L_I_P[0][1]

    for p in range(len(L_I_P)): # Busco la potencia que sea mayor, esta será la que guie al gigglebot
        for i in range(len(L_I_P)):
            if L_I_P[p][1] < L_I_P[i][1]:
                Potencias_Mayores = Potencias_Mayores +1

        if Potencias_Mayores == 0:
            identificacion =  L_I_P[p][0]
            potencia =  L_I_P[p][1]

            return (identificacion, potencia)

        Potencias_Mayores = 0

def quitar_balizas(I, T_B, L_B_E, L_I_P2):
    # Descarto las balizas ya encontradas

    for i in range(T_B-1):
        if L_B_E[I][0] == L_I_P2[i][0]:
            L_I_P2 = L_I_P2[:i] + L_I_P2[i-1:]

            return L_I_P2

        elif L_B_E[I][0] == L_I_P2[T_B-1][0]:
            L_I_P2 = L_I_P2[:(T_B-1)]

            return L_I_P2

    return L_I_P2

def mandar_recibir(M_I, S_S, L_B_E, N_B, L_I_P):
    # Mando la peticion del secreto, recibo el secreto y almaceno el mesaje
    # y la identificacion correspondiente a la baliza recogida

    # Parámetros: identificacion de la baliza mas proxima, secretos encontrados, lista
    # de las balizas encontradas y número de balizas encontradas

    # Devuele: lista de los secretos, lista de las balizas encontradas, número de balizas que se han encontrado
    # y si no se recibe el mensaje la nueva potencia a la que debe acercarse

    for i in range(10):
        iguales = 0

        radio.config(power = 1, group = int(M_I[3:]))
        radio.send("01:dameSecreto")

        received = radio.receive_full()

        if received != None:
            msg, dBm, _ = received
            msg = str(msg[3:], 'utf8')

            for i in range (len(L_I_P)):
                if msg == L_I_P[i][0]:
                    iguales = 1

            if iguales  == 0:
                display.show(msg)
                for pos in range(len(L_B_E)):
                    if L_B_E[pos] == 0:
                        L_B_E[pos] = (M_I, msg)
                        S_S = S_S + "," + msg
                        N_B = N_B + 1

                        return (S_S, L_B_E, N_B)
        sleep(1000)
    return(S_S, L_B_E, N_B)

def main():
    # Guiandose por la señal recibida de un microbit el gigglebot se acerca a este para
    # recibir el mensaje y finalmente entregarle los mensages recibidos a el arbitro

    radio.on()
    gigglebot.set_speed(60, 60)

    POTENCIA_MENSAGE    = -30

    Lst_dBm_ANTERIOR    = [-1000,0] #Declaro el primer elemento de la lista en -1000 para que no comience girand

    Str_SECRETOS        = "03:..."
    Lst_ENCONTRADAS     = [0] * 3
    Lst_id_p            = []
    BALIZAS_ENCONTRADAS = 0
    TOTAL_BALIZAS       = 0

    while True:
        radio.config(group = 41)
        received = radio.receive_full()

        display.show("B") # Buscando señal

        if received != None:
            msg, dBm, _ = received
            identifier = str(msg[3:], 'utf8')
            display.show("R")

            balizas = lista(Lst_id_p, identifier, dBm, TOTAL_BALIZAS, Lst_ENCONTRADAS,BALIZAS_ENCONTRADAS)
            Lst_id_p = balizas[0]
            Lst_id_p_2 = balizas[0]
            TOTAL_BALIZAS = balizas[1]

            if (Lst_id_p[0][0] == identifier) and (TOTAL_BALIZAS != 1) : # Localizó todas las balizas
                display.show("T")
                sleep(500)
                print(balizas)
                if TOTAL_BALIZAS == BALIZAS_ENCONTRADAS:
                    display.show("ACABO" + Str_SECRETOS)
                    print("ACABO")
                    return

                for I in range(BALIZAS_ENCONTRADAS):
                    Lst_id_p_2 = quitar_balizas(I, TOTAL_BALIZAS, Lst_ENCONTRADAS, Lst_id_p_2)
                    TOTAL_BALIZAS = TOTAL_BALIZAS - 1
                    print("-> ",Lst_id_p_2)

                Mejor_Id_P = mejor_baliza(Lst_id_p_2)
                Mejor_Id = Mejor_Id_P[0]
                Mayor_Potencia = Mejor_Id_P[1]

                if Mayor_Potencia > POTENCIA_MENSAGE: # Ha encontrado el microbit
                    display.show(Mejor_Id)
                    print(Mejor_Id)
                    Lst_S_B = mandar_recibir(Mejor_Id, Str_SECRETOS, Lst_ENCONTRADAS, BALIZAS_ENCONTRADAS, Lst_id_p)


                    Str_SECRETOS = Lst_S_B[0]
                    Lst_ENCONTRADAS = Lst_S_B[1]
                    BALIZAS_ENCONTRADAS = Lst_S_B[2]
                    print(Lst_S_B)

                    if BALIZAS_ENCONTRADAS == 0:
                        POTENCIA_MENSAGE = POTENCIA_MENSAGE + 1

                if Mayor_Potencia <= POTENCIA_MENSAGE:
                    Lst_dBm_ANTERIOR[1] = Mayor_Potencia # Almaceno el valor con el que finalizo el anterior ciclo(valor de inicio de este ciclo)
                    print("me muevo")
                    if Mayor_Potencia < Lst_dBm_ANTERIOR[0] : # Comparo el valor de inicio de este ciclo con el del estado anterio
                        gigglebot.turn(gigglebot.RIGHT,400)
                        gigglebot.drive(gigglebot.FORWARD,5000)
                        print("giro")
                    elif Mayor_Potencia >= Lst_dBm_ANTERIOR[0]:
                        gigglebot.drive(gigglebot.FORWARD,5000)
                        print("adelante")

                Lst_dBm_ANTERIOR[0] = Lst_dBm_ANTERIOR[1]
                TOTAL_BALIZAS = 0

            sleep(1000)


if __name__ == "__main__":
    main()
