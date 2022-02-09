from Service.autorService import AutorService
from Service.carteService import CarteService


class Console:
    def __init__(self, carte_service: CarteService,
                 autor_service: AutorService):
        self.__carte_service = carte_service
        self.__autor_service = autor_service

    def run_menu(self):
        while True:
            print("1. Adaugati o noua carte: ")
            print("2. Adaugati un nou autor: ")
            print("3. Afisati toate "
                  "cartile de tip audiobook in ordine alfabetica:")
            print("4. Afisati ")
            print("5. Export Json: ")
            print("a1. Show all carti: ")
            print("a2. Show all autori: ")
            print("x. Iesire")
            optiune = input("Dati aici optiunea: ")
            if optiune == "1":
                self.ui_adauga_masina()
            elif optiune == "2":
                self.ui_adauga_autor()
            elif optiune == "3":
                print(self.__carte_service.ordonare_carti_audiobook())
            elif optiune == "4":
                print(self.__carte_service.pret_pagini_carti())
            elif optiune == "5":
                self.export_json()
            elif optiune == "a1":
                print(self.__carte_service.get_all())
            elif optiune == "a2":
                print(self.__autor_service.get_all())
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati: ")

    def ui_adauga_masina(self):
        try:
            lista_autori = []
            id_carte = input("Dati id-ul cartii: ")
            titlu = input("Dati titlul cartii: ")
            categorie = input("Dati categoria cartii: ")
            nr_pagini = int(input("Dati numarul de pagini al cartii: "))
            pret = float(input("Dati pretul cartii: "))
            nr = int(input("Dati nr de autori din lista de autori: "))
            for i in range(0, nr):
                autori = input("Scrieti autorii, dand space dupa fiecare: ")
                lista_autori.append(autori)
            self.__carte_service.adauga(id_carte, titlu, categorie,
                                        nr_pagini, pret, lista_autori)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_adauga_autor(self):
        try:
            id_autor = input("Dati id-ul autorului: ")
            nume = input("Dati numele autorului: ")
            prenume = input("Dati prenumele autorului: ")
            email = input("Dati emailul autorului: ")
            self.__autor_service.adauga(id_autor, nume, prenume, email)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def export_json(self):
        try:
            filename = input(
                "Dati numele fisierului in care s eva face exportul: ")

            self.__carte_service.export_json(filename)
        except Exception as e:
            print(e)
