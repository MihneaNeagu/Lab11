from Domain.autor import Autor
from Domain.autor_validator import AutorValidator
from Repository.json_repository import JsonRepository


class AutorService:
    def __init__(self, autor_repository: JsonRepository,
                 autor_validator: AutorValidator):
        self.autor_repository = autor_repository
        self.autor_validator = autor_validator

    def adauga(self, id_autor, nume, prenume, email):
        """
        Adauga un autor in multimea de autori
        :param id_autor:
        :param nume:
        :param prenume:
        :param email:
        :return:
        """
        autor = Autor(id_autor, nume, prenume, email)
        self.autor_validator.valideaza(autor)
        self.autor_repository.create(autor)

    def get_all(self):
        return self.autor_repository.read()
