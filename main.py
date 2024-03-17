# main.py
from juego import jugar_ludo
from tablero import mapa

def main():
    print("¡Bienvenido a Ludo!")
    nombre_jugador = input("Por favor, introduce tu nombre: ")
    jugar_ludo(nombre_jugador, mapa)

if __name__ == "__main__":
    main()