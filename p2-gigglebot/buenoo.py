# Write your code here :-)from microbit import *
import radio
import gigglebot

def lista(identifier_power, identifier, dBm, TOTAL_BALIZAS):
    # Hace una lista con las identificaciones y las potencias

    if identifier not in identifier_power:
        identifier_power[identifier] = dBm
        TOTAL_BALIZAS += 1

    return identifier_power, TOTAL_BALIZAS

def mejor_baliza(identifier_power):
    # Busco la baliza con mayor potencia, la mas próxima al gigglebot

    # Parámetros: diccionario de las identificaciones y potencias obtenidas

    # Devuelve: tupla con la identificación y potencia de la baliza que buscamos

    max_power = 0
    best_identifier = None

    for identifier, power in identifier_power.items():
        if power > max_power:
            max_power = power
            best_identifier = identifier

    return best_identifier, max_power

def quitar_balizas(I, identifier_power2):
    # Descarto las balizas ya encontradas

    del identifier_power2[I]

    return identifier_power2

def mandar_recibir(M_I, S_S, L_B_E, N_B, identifier_power):
    # Mando la petición del secreto, recibo el secreto y almaceno el mensaje
    # y la identificación correspondiente a la baliza recogida

    # Parámetros: identificación de la baliza más cercana, secretos encontrados, lista
    # de las balizas encontradas y número de balizas encontradas

    # Devuelve: diccionario de los secretos, lista de las balizas encontradas y número de balizas encontradas

    secret_messages = {}
    radio.send(M_I)

    received_secret = radio.receive()
    if received_secret is not None:
        secret_messages[M_I] = received_secret
        S_S.append(received_secret)
        L_B_E.append(M_I)
        N_B += 1
        del identifier_power[M_I]
    return secret_messages, L_B_E, N_B

def mensaje_secreto(L_B_E, S_S, N_B):
    # Genero el mensaje final con los secretos encontrados

    # Parámetros: lista de las balizas encontradas, lista de los secretos encontrados
    # y número de balizas encontradas

    # Devuelve: mensaje final con los secretos

    secret_message = ""

    for i in range(N_B):
        secret_message += L_B_E[i] + ": " + S_S[i] + " "

    return secret_message

# Programa principal

TOTAL_BALIZAS = 0
Lst_id_p = {}
Lst_ENCONTRADAS = []
BALIZAS_ENCONTRADAS = 0
SECRETOS_ENCONTRADOS = []

gigglebot.set_speed(60, 60)

radio.on()

while True:
    # Escaneo para encontrar balizas

    balizas = radio.scan()

    for baliza in balizas:
        Lst_id_p, TOTAL_BALIZAS = lista(Lst_id_p, baliza[0], baliza[1], TOTAL_BALIZAS)

    if TOTAL_BALIZAS > 0:
        M_I, POTENCIA = mejor_baliza(Lst_id_p)

        Lst_id_p2 = Lst_id_p.copy()

        Lst_id_p2 = quitar_balizas(M_I, Lst_id_p2)

        # Giro hacia la baliza mas cercana

        gigglebot.turn_to(M_I)

        # Mando la peticion del secreto y recibo el secreto

        secretos, Lst_ENCONTRADAS, BALIZAS_ENCONTRADAS = mandar_recibir(M_I, SECRETOS_ENCONTRADAS, Lst_ENCONTRADAS, BALIZAS_ENCONTRADAS, Lst_id_p)

        # Genero el mensaje final con los secretos encontrados

        mensaje_final = mensaje_secreto(Lst_ENCONTRADAS, SECRETOS_ENCONTRADAS, BALIZAS_ENCONTRADAS)

        # Muestro el mensaje final por pantalla

        display.scroll(mensaje_final)


