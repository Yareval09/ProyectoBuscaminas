"""CasillasVacias: revelación en cascada de casillas vacías."""

from __future__ import annotations

from collections import deque

from src.modelo.tablero.Coordenada import Coordenada
from src.modelo.tablero.Tablero import Tablero


class CasillasVacias:
    """Descubre una casilla y, si es vacía, propaga la revelación a sus vecinas.
    """

    def expandir(self, tablero: Tablero, origen: Coordenada) -> list[Coordenada]:
        """Descubre `origen` y propaga si corresponde.

        Devuelve las coordenadas descubiertas, en orden (la primera es `origen`).
        Devuelve una lista vacía, sin cambiar nada, si `origen` no se puede
        descubrir (tiene bandera o ya estaba descubierta).
        Lanza IndexError si `origen` está fuera del tablero.
        """
        casilla_origen = tablero.casilla(origen)
        if not casilla_origen.puede_descubrirse():
            return []

        casilla_origen.descubrir()
        descubiertas = [origen]
        if not casilla_origen.es_vacia:
            return descubiertas 

        pendientes = deque([origen])
        while pendientes:
            actual = pendientes.popleft()
            for coordenada in tablero.vecinas(actual):
                vecina = tablero.casilla(coordenada)
                if vecina.tiene_mina or not vecina.puede_descubrirse():
                    continue
                vecina.descubrir()
                descubiertas.append(coordenada)
                if vecina.es_vacia:
                    pendientes.append(coordenada)
        return descubiertas