
from __future__ import annotations

from enum import Enum


class EstadoCasilla(Enum):
    """Estado visible de una casilla.

    Transiciones permitidas:
        CUBIERTA    -> DESCUBIERTA   (descubrir)
        CUBIERTA    -> CON_BANDERA   (alternar bandera)
        CON_BANDERA -> CUBIERTA      (alternar bandera)
    """

    CUBIERTA = "cubierta"
    DESCUBIERTA = "descubierta"
    CON_BANDERA = "con_bandera"

    def puede_descubrirse(self) -> bool:
        return self is EstadoCasilla.CUBIERTA

    def puede_alternar_bandera(self) -> bool:
        return self is not EstadoCasilla.DESCUBIERTA

    def descubrir(self) -> EstadoCasilla:
        if not self.puede_descubrirse():
            raise ValueError(f"No se puede descubrir una casilla {self.value}")
        return EstadoCasilla.DESCUBIERTA

    def alternar_bandera(self) -> EstadoCasilla:
        if self is EstadoCasilla.CUBIERTA:
            return EstadoCasilla.CON_BANDERA
        if self is EstadoCasilla.CON_BANDERA:
            return EstadoCasilla.CUBIERTA
        raise ValueError(f"No se puede poner o quitar bandera a una casilla {self.value}")