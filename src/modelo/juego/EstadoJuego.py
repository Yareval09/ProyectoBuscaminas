from enum import Enum

class EstadoJuego(Enum):
    SIN_INICIAR = "sin_iniciar"
    EN_CURSO = "en_curso"
    GANADA = "ganada"
    PERDIDA = "perdida"

    def esta_terminada(self) -> bool:
        return self in (
            EstadoJuego.GANADA,
            EstadoJuego.PERDIDA
        )