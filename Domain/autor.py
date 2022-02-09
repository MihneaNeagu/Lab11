from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Autor(Entity):
    nume: str
    prenume: str
    email: str
