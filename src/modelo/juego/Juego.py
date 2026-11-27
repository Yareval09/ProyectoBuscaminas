from .EstadoJuego import EstadoJuego
from ..eventos.EventoJuego import EventoJuego
from ..eventos.Observador import Observador

class Juego:
    
    # Inicio del juego
    def __init__(self, constructor_tablero, expansion, temporizador, evaluador_victoria):
        self.estado = EstadoJuego.SIN_INICIAR
        self.observadores = []
        self.tablero = None
        self.dificultad = None
        self.constructor_tablero = constructor_tablero
        self.expansion = expansion
        self.temporizador = temporizador
        self.evaluador_victoria = evaluador_victoria

    # Consulta de los estados de la partida
    def obtener_estado(self) -> EstadoJuego:
        return self.estado

    def obtener_tablero(self):
        return self.tablero

    def obtener_tiempo(self) -> int:
        return self.temporizador.obtener_tiempo()

    # Registro y eliminacion de observadores
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

    # Creacion de una nueva partida
    def nueva_partida(self, dificultad) -> None:
        tablero = self.constructor_tablero.construir(dificultad)
        self.temporizador.reiniciar()
        self.tablero = tablero
        self.dificultad = dificultad
        self.estado = EstadoJuego.SIN_INICIAR
        self.notificar_observadores(EventoJuego.NUEVA_PARTIDA)

    # Validacion de la parida
    def _jugada_valida(self, coordenada) -> bool:
        return (self.tablero is not None
                 and not self.estado.esta_terminada()
                 and self.tablero.contiene(coordenada))

    # Inicio del temporizador
    def _iniciar_partida(self) -> None:
        if self.estado == EstadoJuego.SIN_INICIAR:
            self.temporizador.iniciar()
            self.estado = EstadoJuego.EN_CURSO
            self.notificar_observadores(EventoJuego.PARTIDA_INICIADA)

    # Descubrimiento de casillas
    def descubrir_casilla(self, coordenada) -> None
        if not self._jugada_valida(coordenada):
                return

        casilla = self.tablero.obtener_casilla(coordenada)
        if not casilla.esta_cubierta():
            return
    
        self._iniciar_partida()

        # Derrota al descubrir mina
        if casilla.tiene_mina():
            casilla.descubrir()
            self._finalizar_partida(EstadoJuego.PERDIDA)
            return

        # Expansion de casillas vacias
        if casilla.obtener_minas_adyacentes() == 0:
            self.expansion.expandir(self.tablero, coordenada)
        else:
            casilla.descubrir

        # Validacion de victoria
        if self.evaluador_victoria.hay_victoria(self.tablero):
            self._finalizar_partida(EstadoJuego.GANADA)
        else:
            self.notificar_observadores(EventoJuego.CASILLA_DESCUBIERTA)

        # Colocacion de banderas
        def alternar_bandera(self, coordenada) -> None:
            if not (casilla.esta_cubierta() or casilla.tiene_bandera()):
                return

            self.iniciar_partida()
            casilla.alternar_bandera()
            self.notificar_observadores(EventoJuego.BANDERA_MODIFICADA)

    # Fin de la partida
    def _finalizar_partida(self, estado: EstadoJuego) -> None
        self.temporizador.detener()
        self.estado = estado

        if estado == EstadoJuego.GANADA:
            self.notificar_observadores(EventoJuego.VICTORIA)
        else:
            self.notificar_observadores(EventoJuego.DERROTA)
