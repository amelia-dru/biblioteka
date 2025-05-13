
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
        return f'tytul -> {self.tytul}, autor -> {self.autor}, rok -> {self.rok}, id ->  {self.id}, ilosc -> {self.ilosc}'

    def __str__(self):
        return self.szczegoly()


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
