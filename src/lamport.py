from dataclasses import dataclass
from threading import Lock


@dataclass(frozen=True, order=True)
class EventOrder:
    """Desempata marcas iguales usando el identificador fijo de la oficina."""

    counter: int
    node_id: int