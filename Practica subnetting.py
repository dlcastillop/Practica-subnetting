from ipv4_subnetting import *

print("""PRACTICA SUBNETTING
-----------------------------------------------------------------------------------
Programa para ayudar a las personas con el desarrollo de la habilidad de subnetting
-----------------------------------------------------------------------------------
""")

# Ciclo infinito
while True:
    # Generar dirección IP aleatoria
    ip = ip_aleatoria()

    # Validar que a la dirección IP generada se le puede aplicar el proceso de subnetting
    while not validar_subnetting(ip):
        ip = ip_aleatoria()

    # Generar máscara aleatoria
    mascara = randint(8, 30)

    # Elegir aleatoriamente el formato de la máscara
    formato_mascara = randint(0, 1)
    if formato_mascara == 0:
        imprimir_mascara = f"/{str(mascara)}"
        mascara = mascara_ddn(mascara)
    else:
        mascara = mascara_ddn(mascara)
        imprimir_mascara = f"con máscara {mascara}"
    
    # Imprimir el ejercicio
    print(f"A partir de la dirección IP {ip} {imprimir_mascara} determina:")

    # Pedir las respuestas
    resp_ID = input("ID de subred: ")
    resp_broadcast = input("Dirección broadcast: ")
    resp_primera_dir = input("Primera dirección asignable a hosts: ")
    resp_ultima_dir = input("Última dirección asignable a hosts: ")
    print()

    # Calcular las respuestas correctas
    ID_correcto = id_subred(ip, mascara)
    broadcast_correcto = dir_broadcast(ip, mascara)
    primera_correcta = primera_dir(ip, mascara)
    ultima_correcta = ultima_dir(ip, mascara)

    # Revisar las respuestas del usuario
    if ID_correcto == resp_ID:
        print("¡Has introducido el ID de subred correctamente!\n")
    else:
        print(f"El ID de subred introducido es incorrecto. La respuesta correcta es: {ID_correcto}\n")

    if broadcast_correcto == resp_broadcast:
        print("¡Has introducido la dirección broadcast correctamente!\n")
    else:
        print(f"La dirección broadcast introducida es incorrecta. La respuesta correcta es: {broadcast_correcto}\n")

    if primera_correcta == resp_primera_dir and ultima_correcta == resp_ultima_dir:
        print("¡Has introducido el rango de direcciones asignables a hosts correctamente!\n")
    else:
        print("El rango de direcciones asignables a hosts introducido es incorrecto. La respuesta correcta es:"
              f" {primera_correcta} - {ultima_correcta}\n")
