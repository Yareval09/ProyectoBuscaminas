from .EstadoJuego import EstadoJuego
from ..eventos.EventoJuego import EventoJuego
from ..eventos.Observador import Observador

class Juego:
    
    # Inicio del juego
    def _init_(self):
        self.estado = EstadoJuego.SIN_INICIAR
        self.observadores = []

    # Consulta del estado
    def obtener_estado(self) -> EstadoJuego:
        return self.estado

    # Regitro y eliminacion de observadores
    def agregar_observador(self, observador: Observador) -> None:
        if observador not in self.observadores:
            self.observadores.append(observador)

    def eliminar_observador(self, observador: Observador) -> None:
        if observador in self.observadores:
            self.observadores.remove(observador)

    # Notificaciones de eventos
    def notificar_observadores(self, evento: EventoJuego) -> None:
        for observador in self.observadores.copy():
            observador.actualizar(evento)