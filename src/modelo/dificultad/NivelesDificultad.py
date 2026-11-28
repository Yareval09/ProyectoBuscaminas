from __future__ import annotations

from src.modelo.dificultad.ConfiguracionDificultad import ConfiguracionDificultad

class NivelesDificultad:

    """niveles de dificultad.
    Catálogo de niveles de dificultad disponibles:
        facil    -> 9 * 9      10
        medio    -> 16 * 16    40
        dificil  -> 16 * 30    99
        
    """

    FACIL = "Facil"
    MEDIO = "Medio"
    DIFICIL = "Dificil"


    def __init__(self) -> None:
        self._niveles = {}
        self._niveles[self.FACIL] = ConfiguracionDificultad(filas=9, columnas=9, minas=10, nombre=self.FACIL)
        self._niveles[self.MEDIO] = ConfiguracionDificultad(filas=16, columnas=16, minas=40, nombre=self.MEDIO)
        self._niveles[self.DIFICIL] = ConfiguracionDificultad(filas=16, columnas=30, minas=99, nombre=self.DIFICIL)
    
    def obtener(self, nombre: str) -> ConfiguracionDificultad:
        if nombre in self._niveles:
            return self._niveles[nombre]
        raise ValueError(f"No hay nombre: {nombre}")


    def listar(self) -> list[ConfiguracionDificultad]:
        return list(self._niveles.values())

    def registrar(self, configuracion: ConfiguracionDificultad) -> None:
        if configuracion.nombre in self._niveles:
            raise ValueError(f"ya existe un nivel llamado: {configuracion.nombre}")
        self._niveles[configuracion.nombre] = configuracion
