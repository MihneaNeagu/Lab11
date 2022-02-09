from Domain.carte import Carte


class CarteValidator:
    def valideaza(self, carte: Carte):
        erori = []
        if carte.titlu == '':
            erori.append("Titlul cartii nu poate fi gol!")
        if carte.categorie not in ["beletristică", "sănătate",
                                   "istorie", "economie", "psihologie",
                                   "audiobook", "memorii", "tehnologie"]:
            erori.append("Categoria cartii nu este buna!")
        if carte.nr_pagini == 0:
            erori.append("Numarul de pagini al cartii nu poate fi nul!")
        if carte.pret < 0:
            erori.append("Pretul cartii trebuie sa fie real pozitiv!")
        if carte.list_autori is []:
            erori.append("Lista de autori nu poate fi goala!")
        if erori:
            raise ValueError(erori)
