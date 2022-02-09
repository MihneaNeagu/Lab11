from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Carte(Entity):
    titlu: str
    categorie: str
    nr_pagini: int
    pret: float
    list_autori: list
