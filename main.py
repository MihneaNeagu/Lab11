from Domain.autor_validator import AutorValidator
from Domain.carte_validator import CarteValidator
from Repository.json_repository import JsonRepository
from Service.autorService import AutorService
from Service.carteService import CarteService
from UserInterface.console import Console


def main():
    carte_repository_json = JsonRepository("carti.json")
    carte_validator = CarteValidator()
    autor_repository_json = JsonRepository("autori.json")
    carte_service = CarteService(carte_repository_json, carte_validator,
                                 autor_repository_json)
    autor_validator = AutorValidator()
    autor_service = AutorService(autor_repository_json, autor_validator)
    console = Console(carte_service, autor_service)

    console.run_menu()


if __name__ == '__main__':
    main()
