# models/rutinas.py

from models.rutinas_futbol import RUTINAS_FUTBOL
from models.rutinas_baloncesto import RUTINAS_BALONCESTO
from models.rutinas_natacion import RUTINAS_NATACION
from models.rutinas_tenis import RUTINAS_TENIS

RUTINAS = (
    RUTINAS_FUTBOL +
    RUTINAS_BALONCESTO +
    RUTINAS_NATACION +
    RUTINAS_TENIS
)
