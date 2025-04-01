#bibliotekarz
import random

id_user = 0
id_book = 0

class Ksiazka:
    def __init__(self, tytul, autor, rok:int, ilosc:int):
        global id_book
        id_book += 1
        self.tytul = tytul
        self.autor = autor
        self.rok = rok
        self.ilosc = ilosc
        self.dostepnosc = ilosc > 0
        self.id = id_book

    def szczegoly(self):
        return f'tytul: {self.tytul}, autor: {self.autor}, rok: {self.rok}, id: {self.id}, ilosc: {self.ilosc}'


lista = [
    Ksiazka("SHERLOCK HOLMES: STUDIUM W SZKARLACIE", "ARTHUR CONAN DOYLE", 1887, 5),
    Ksiazka("ZBRODNIA I KARA", "FIODOR DOSTOJEWSKI", 1866, 2 ),
    Ksiazka("DUMA I UPRZEDZENIE", "JANE AUSTEN", 1813, 1),
    Ksiazka("ROK 1984", "GEORGE ORWELL", 1949, 5),
    Ksiazka("WLADCA PIERSCIENI", "J.R.R. TOLKIEN", 1954, 8),
    Ksiazka("MISTRZ I MALGORZATA", "MICHAIL BULHAKOW", 1967, 2),
    Ksiazka("HOBBIT", "J.R.R. TOLKIEN", 1937, 3),
    Ksiazka("MALY KSIAZE", "ANTOINE DE SAINT-EXUPERY", 1943, 1),
    Ksiazka("BUSZUJACY W ZBOZU", "J.D. SALINGER", 1951, 7),
    Ksiazka("HARRY POTTER I KAMIEN FILOZOFICZNY", "J.K. ROWLING", 1997, 2),
    Ksiazka("IMIE ROZY", "UMBERTO ECO", 1980, 1),
    Ksiazka("GRA O TRON", "GEORGE R.R. MARTIN", 1996, 1),
    Ksiazka("FOLWARK ZWIERZECY", "GEORGE ORWELL", 1945, 8),
    Ksiazka("OJCIEC CHRZESTNY", "MARIO PUZO", 1969, 2),
    Ksiazka("LALKA", "BOLESLAW PRUS", 1890, 7)
]

class Uzytkownik():
    def __init__(self, imie, nazwisko, wiek:int):
        global id_user 
        id_user += 1
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.lista_ksiazek = []
        self.id = id_user
    
    def szczegoly(self):
        return f'imie i nazwisko: {self.imie} {self.nazwisko}, wiek: {self.wiek}, lista ksiazek {self.lista_ksiazek}, id: {self.id}'


uzytkownicy = [
    Uzytkownik("Jan", "Kowalski", 25),
    Uzytkownik("Anna", "Nowak", 30),
    Uzytkownik("Piotr", "Wiśniewski", 40),
    Uzytkownik("Maria", "Dąbrowska", 22),
    Uzytkownik("Krzysztof", "Lewandowski", 35),
    Uzytkownik("Magdalena", "Wójcik", 28),
    Uzytkownik("Tomasz", "Kamiński", 50),
    Uzytkownik("Ewa", "Zielińska", 33),
    Uzytkownik("Michał", "Szymański", 45),
    Uzytkownik("Aleksandra", "Woźniak", 29)
]
