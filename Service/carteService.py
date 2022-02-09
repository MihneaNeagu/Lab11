import jsonpickle

from Domain.carte import Carte
from Domain.carte_validator import CarteValidator
from Repository.json_repository import JsonRepository


class CarteService:
    def __init__(self, carte_repository: JsonRepository,
                 carte_validator: CarteValidator,
                 autor_repository: JsonRepository):
        self.carte_repository = carte_repository
        self.carte_validator = carte_validator
        self.autor_repository = autor_repository

    def adauga(self, id_carte, titlu, categorie,
               nr_pagini, pret, lista_autori):
        """
        Adauga o carte in multimea de carti
        :param id_carte:
        :param titlu:
        :param categorie:
        :param nr_pagini:
        :param pret:
        :param lista_autori:
        :return:
        """
        carte = Carte(id_carte, titlu, categorie,
                      nr_pagini, pret, lista_autori)
        self.carte_validator.valideaza(carte)
        self.carte_repository.create(carte)

    def get_all(self):
        return self.carte_repository.read()

    def ordonare_carti_audiobook(self):
        """
        ordoneaza in ordine alfabetica toate cartile de tip audiobook
        :return:
        """
        carti_audio = []
        for carte in self.carte_repository.read():
            if carte.categorie == "audiobook":
                carti_audio.append(carte.titlu)
        carti_audio.sort()
        for carte in self.carte_repository.read():
            for carte.titlu in carti_audio:
                return carte

    def pret_pagini_carti(self):
        """
        Afiseaza pretul maxim si nr mediu de pagini
        al fiecarei categorie de carti
        :return:
        """

    def export_json(self, filename: str):
        """

        :param filename: numele fisierului in care se face exportul
        :return:
        """
        rezultat = {}
        for autor in self.autor_repository.read():
            nume = self.autor_repository.read(autor.nume)
            prenume = self.autor_repository.read(autor.prenume)
            numecomplet = nume+" "+prenume
            rezultat[autor.nume] = []
            for carte in self.carte_repository.read():
                if numecomplet in carte.list_autori:
                    rezultat[numecomplet].append(carte.titlu)

        with open(filename, 'w') as f:
            f.write(jsonpickle.dumps(rezultat))
