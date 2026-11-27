
from __future__ import annotations

from src.modelo.tablero.EstadoCasilla import EstadoCasilla

MAX_MINAS_VECINAS = 8


class Casilla:
    """Una celda del tablero.

    Guarda si tiene mina, cuántas minas la rodean y su estado visible.
    Solo cambia de estado
    """

    def __init__(self, tiene_mina: bool = False) -> None:
        self._tiene_mina: bool = tiene_mina
        self._minas_vecinas: int = 0
        self._estado: EstadoCasilla = EstadoCasilla.CUBIERTA

    @property
    def tiene_mina(self) -> bool:
        return self._tiene_mina

    @property
    def minas_vecinas(self) -> int:
        return self._minas_vecinas

    @property
    def estado(self) -> EstadoCasilla:
        return self._estado

    @property
    def esta_cubierta(self) -> bool:
        return self._estado is EstadoCasilla.CUBIERTA

    @property
    def esta_descubierta(self) -> bool:
        return self._estado is EstadoCasilla.DESCUBIERTA

    @property
    def tiene_bandera(self) -> bool:
        return self._estado is EstadoCasilla.CON_BANDERA

    @property
    def es_vacia(self) -> bool:
        """True si no tiene mina ni minas vecinas (dispara la expansión en cascada)."""
        return not self._tiene_mina and self._minas_vecinas == 0

 
    def colocar_mina(self) -> None:
        self._tiene_mina = True

    def establecer_minas_vecinas(self, cantidad: int) -> None:
        if not 0 <= cantidad <= MAX_MINAS_VECINAS:
            raise ValueError(f"minas_vecinas debe estar entre 0 y {MAX_MINAS_VECINAS}: {cantidad}")
        self._minas_vecinas = cantidad

    # --- Acciones del jugador 
    def puede_descubrirse(self) -> bool:
        return self._estado.puede_descubrirse()

    def descubrir(self) -> None:
        """Descubre la casilla. Lanza ValueError si tiene bandera o ya está descubierta."""
        self._estado = self._estado.descubrir()

    def alternar_bandera(self) -> None:
        """Pone o quita la bandera. Lanza ValueError si ya está descubierta."""
        self._estado = self._estado.alternar_bandera()

    def __repr__(self) -> str:
        return (
            f"Casilla(mina={self._tiene_mina}, vecinas={self._minas_vecinas}, "
            f"estado={self._estado.name})"
        )