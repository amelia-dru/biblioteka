#bibliotekarz
class Ksiazka:
    def __init__(self, tytul, autor, rok:int):
        self.tytul = tytul
        self.autor = autor
        self.rok = rok
        self.dostepnosc = True

    def szczegoly(self):
        return f'tytul: {self.tytul}, autor: {self.autor}, rok: {self.rok}'


lista = [
    Ksiazka("Sherlock Holmes: Studium w szkarlacie", "Arthur Conan Doyle", 1887),
    Ksiazka("Zbrodnia i kara", "Fiodor Dostojewski", 1866),
    Ksiazka("Duma i uprzedzenie", "Jane Austen", 1813),
    Ksiazka("Rok 1984", "George Orwell", 1949),
    Ksiazka("Władca Pierścieni", "J.R.R. Tolkien", 1954),
    Ksiazka("Mistrz i Małgorzata", "Michaił Bułhakow", 1967),
    Ksiazka("Hobbit", "J.R.R. Tolkien", 1937),
    Ksiazka("Mały Książę", "Antoine de Saint-Exupéry", 1943),
    Ksiazka("Buszujący w zbożu", "J.D. Salinger", 1951),
    Ksiazka("Harry Potter i Kamień Filozoficzny", "J.K. Rowling", 1997),
    Ksiazka("Imię róży", "Umberto Eco", 1980),
    Ksiazka("Gra o tron", "George R.R. Martin", 1996),
    Ksiazka("Folwark zwierzęcy", "George Orwell", 1945),
    Ksiazka("Ojciec chrzestny", "Mario Puzo", 1969),
    Ksiazka("Lalka", "Bolesław Prus", 1890)
]
