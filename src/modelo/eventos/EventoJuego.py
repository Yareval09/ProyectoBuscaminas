from enum import Enum

class EventoJuego(Enum):

    # Eventos al inicio de la partida
    NUEVA_PARTIDA = "nueva_partida"
    PARTIDA_INICIADA = "partida_iniciada"

    # Eventos que modifican el tablero
    CASILLA_DESCUBIERTA = "casilla_descubierta"
    BANDERA_MODIFICADA = "bandera_modificada"

    # Eventos al final de la partida
    VICTORIA = "victoria"
    DERROTA = "derrota"

    