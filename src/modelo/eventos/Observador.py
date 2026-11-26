from abc import ABC, abstractmethod
from .EventoJuego import EventoJuego

class Observador(ABC):

    # Sirve para recibir las notificacione del juego
    @abstractmethod
    def actualizar(self, evento: EventoJuego) -> None:
        pass