from __future__ import annotations

from typing import Iterator

from src.modelo.tablero.Casilla import Casilla
from src.modelo.tablero.Coordenada import Coordenada


class Tablero:
    """Cuadrícula de `filas` x `columnas` casillas.

    Se crea con todas las casillas vacías y cubiertas.
    """

    def __init__(self, filas: int, columnas: int) -> None:
        for nombre, valor in (("filas", filas), ("columnas", columnas)):
            if not isinstance(valor, int) or isinstance(valor, bool):
                raise TypeError(f"{nombre} debe ser un entero, no {type(valor).__name__}")
            if valor < 1:
                raise ValueError(f"{nombre} debe ser al menos 1: {valor}")
        self._filas: int = filas
        self._columnas: int = columnas
        self._casillas: list[list[Casilla]] = [
            [Casilla() for _ in range(columnas)] for _ in range(filas)
        ]

    @property
    def filas(self) -> int:
        return self._filas

    @property
    def columnas(self) -> int:
        return self._columnas

    @property
    def total_casillas(self) -> int:
        return self._filas * self._columnas

    def contiene(self, coordenada: Coordenada) -> bool:
        """True si la coordenada está dentro del tablero."""
        return coordenada.fila < self._filas and coordenada.columna < self._columnas

    def casilla(self, coordenada: Coordenada) -> Casilla:
        """Devuelve la casilla en la coordenada. Lanza IndexError si está fuera."""
        if not self.contiene(coordenada):
            raise IndexError(
                f"{coordenada} fuera del tablero de {self._filas}x{self._columnas}"
            )
        return self._casillas[coordenada.fila][coordenada.columna]

    def coordenadas(self) -> Iterator[Coordenada]:
        """Recorre todas las coordenadas, fila por fila."""
        for fila in range(self._filas):
            for columna in range(self._columnas):
                yield Coordenada(fila, columna)

    def casillas(self) -> Iterator[Casilla]:
        """Recorre todas las casillas, fila por fila."""
        for fila in self._casillas:
            yield from fila

    def vecinas(self, coordenada: Coordenada) -> list[Coordenada]:
        """Coordenadas vecinas (hasta 8) que están dentro del tablero."""
        return [c for c in coordenada.adyacentes() if self.contiene(c)]

    def casillas_vecinas(self, coordenada: Coordenada) -> list[Casilla]:
        """Casillas vecinas (hasta 8) que están dentro del tablero."""
        return [self.casilla(c) for c in self.vecinas(coordenada)]

    @property
    def total_minas(self) -> int:
        return sum(1 for c in self.casillas() if c.tiene_mina)

    @property
    def total_banderas(self) -> int:
        return sum(1 for c in self.casillas() if c.tiene_bandera)

    @property
    def total_descubiertas(self) -> int:
        return sum(1 for c in self.casillas() if c.esta_descubierta)

    def __repr__(self) -> str:
        return f"Tablero({self._filas}x{self._columnas})"