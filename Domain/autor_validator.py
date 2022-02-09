from Domain.autor import Autor


class AutorValidator:
    def valideaza(self, autor: Autor):
        erori = []
        if autor.nume == '':
            erori.append("Numele autorului nu poate fi gol!")
        if autor.prenume == '':
            erori.append("Prenumele autorului nu poate fi gol!")
        if "@" not in autor.email and autor.email == '':
            erori.append("Emailul nu poate fi gol si tb sa contina @")
        if erori:
            raise ValueError(erori)
