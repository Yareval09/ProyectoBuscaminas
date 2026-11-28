from __future__ import annotations

from dataclasses import dataclass

@dataclass(frozen=True)
class ConfiguracionDificultad:

    filas: int
    columnas: int
    minas: int
    nombre: str
    def __post_init__(self) -> None:
        for nombre, valor in (("filas", self.filas), ("columnas", self.columnas), ("minas", self.minas)):
            if not isinstance(valor, int) or isinstance(valor, bool):
                raise TypeError(f"{nombre} debe ser un entero, no {type(valor).__name__}")
            if valor < 1:
                raise ValueError(f"{nombre} no puede ser menor a 1: {valor}")
            
        if not isinstance(self.nombre, str):
            raise TypeError(f"nombre debe ser una cadena de texto, no {type(self.nombre).__name__}")

        if not self.nombre.strip():
            raise ValueError("El nombre de la dificultad no puede estar vacío.")

        if self.minas >= self.filas * self.columnas or self.minas <= 0:
            raise ValueError(f"El número de minas ({self.minas}) no puede ser mayor o igual al número de casillas ({self.filas * self.columnas})")