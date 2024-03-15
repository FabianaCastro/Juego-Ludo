# juego.py
import random
from tablero import imprimir_tablero
from tablero import mapa

def lanzar_dado():
    return random.randint(1, 6)

def mover_ficha(posicion_actual, dado):
    fila, columna = posicion_actual
    nueva_fila, nueva_columna = fila, columna

    # Mover hacia arriba en el borde del tablero
    if columna == 0 and fila - dado >= 0:
        nueva_fila -= dado
    # Mover hacia la derecha en el borde del tablero
    elif fila == 0 and columna + dado <= 10:
        nueva_columna += dado
    # Mover hacia abajo en el borde del tablero
    elif columna == 10 and fila + dado <= 10:
        nueva_fila += dado
    # Mover hacia la izquierda en el borde del tablero
    elif fila == 10 and columna - dado >= 0:
        nueva_columna -= dado

    return (nueva_fila, nueva_columna)

def casilla_especial(posicion_actual, casilla):
    # Si la ficha cae en una casilla especial B1, B2 o B3, retrocede o avanza 5 posiciones
    if casilla in ['10-B1', '20-B2', '30-B3']:
        decision = input("Has caído en una casilla especial {}. ¿Deseas avanzar o retroceder 5 posiciones? (avanzar/retroceder): ".format(casilla))
        if decision.lower() == 'avanzar':
            return mover_ficha(posicion_actual, 5)
        elif decision.lower() == 'retroceder':
            return mover_ficha(posicion_actual, -5)
    return posicion_actual

def jugar_ludo(nombre_jugador, mapa):
    jugador_pos = (10, 0)  # Posición inicial del jugador
    cpu_pos = (10, 0)      # Posición inicial del CPU
    vueltas_jugador = 0
    vueltas_cpu = 0
    turno = nombre_jugador

    print("¡Bienvenido a Ludo!")

    while vueltas_jugador < 3 and vueltas_cpu < 3:
        print("Turno de", turno)

        input("Presiona Enter para lanzar el dado...")
        dado = lanzar_dado()
        print("Has sacado un", dado)

        # Si el dado es 6, el jugador puede lanzar de nuevo
        if dado == 6:
            print("¡Sacaste un 6! Tienes otro turno.")
        else:
            turno = "CPU" if turno == nombre_jugador else nombre_jugador

        # Mover jugador
        if turno == nombre_jugador:
            jugador_pos = casilla_especial(jugador_pos, mapa[jugador_pos[0]][jugador_pos[1]])
            jugador_pos = mover_ficha(jugador_pos, dado)
            imprimir_tablero(jugador_pos, cpu_pos)

            # Verificar si el jugador ha completado una vuelta
            if jugador_pos == (10, 0):
                vueltas_jugador += 1
                print("¡Has completado una vuelta!")

        # Mover CPU (simulado)
        else:
            dado_cpu = lanzar_dado()
            cpu_pos = casilla_especial(cpu_pos, mapa[cpu_pos[0]][cpu_pos[1]])
            cpu_pos = mover_ficha(cpu_pos, dado_cpu)
            imprimir_tablero(jugador_pos, cpu_pos)  # Imprimir tablero con las posiciones actualizadas del jugador y CPU

            # Verificar si el CPU ha completado una vuelta
            if cpu_pos == (10, 0):
                vueltas_cpu += 1

    if vueltas_jugador == 3:
        print("¡Felicidades, has ganado!")
    else:
        print("¡El CPU ha ganado!")



