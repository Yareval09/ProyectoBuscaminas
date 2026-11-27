from enum import Enum

class EstadoJuego(Enum):

    # Posibles estados de la patida 
    SIN_INICIAR = "sin_iniciar"
    EN_CURSO = "en_curso"
    GANADA = "ganada"
    PERDIDA = "perdida"

    # Verifica si la partida termino
    def esta_terminada(self) -> bool:
        return self in (
            EstadoJuego.GANADA,
            EstadoJuego.PERDIDA
        )