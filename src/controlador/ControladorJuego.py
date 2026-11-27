from modelo.juego.Juego import Juego
from modelo.tablero.Coordenada import Coordenada

class ControladorJuego:

    # Iniciador del control
    def __init__(self, juego: Juego):
        self.juego = juego

    # Creacion de la partida nueva
    def nueva_partida(self, dificultad) -> None:
        self.juego.nueva_partida(dificultad)

    # Acciones del jugador
    def clic_izquierdo(self, fila: int, columna: int) -> None:
        coordenada = Coordenada(fila, columna)
        self.juego.descubrir_casilla(coordenada)

    def clic_derecho(self, fila: int, columna: int) -> None:
        coordenada = Coordenada(fila, columna)
        self.juego.alternar_bandera(coordenada)