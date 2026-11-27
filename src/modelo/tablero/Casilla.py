from __future__ import annotations

from dataclasses import dataclass
from typing import Iterator

@dataclass(frozen=True, order=True)
class Coordenada:

    fila: int
    columna: int

    def __post_init__(self) -> None:
        for nombre, valor in (("fila", self.fila), ("columna", self.columna)):
            if not isinstance(valor, int) or isinstance(valor, bool):
                raise TypeError(f"{nombre} debe ser un entero, no {type(valor).__name__}")
            if valor < 0:
                raise ValueError(f"{nombre} no puede ser negativa: {valor}")

    def desplazada(self, d_fila: int, d_columna: int) -> Coordenada:
        """Devuelve una nueva coordenada desplazada (lanza ValueError si queda negativa)."""
        return Coordenada(self.fila + d_fila, self.columna + d_columna)

    def adyacentes(self) -> Iterator[Coordenada]:
        """Genera las hasta 8 coordenadas vecinas, omitiendo las que serían negativas.
        """
        for d_fila in (-1, 0, 1):
            for d_columna in (-1, 0, 1):
                if d_fila == 0 and d_columna == 0:
                    continue
                fila, columna = self.fila + d_fila, self.columna + d_columna
                if fila >= 0 and columna >= 0:
                    yield Coordenada(fila, columna)