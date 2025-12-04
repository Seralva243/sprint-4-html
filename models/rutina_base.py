from dataclasses import dataclass, field
from typing import List

@dataclass
class Rutina:
    deporte: str
    nivel: str
    tipo_sesion: str      # "Gimnasio", "Aire libre", "Piscina"
    titulo: str
    descripcion: str
    duracion: str
    pasos: List[str]
    # Por defecto sin imagen; luego la rellenamos en el viewmodel
    imagen: str = ""
    evitar_flags: List[str] = field(default_factory=list)
