import model

class Dane:
    def __init__(self):
        self.user = [
            model.Uzytkownik("Jan", "Kowalski", 25),
            model.Uzytkownik("Anna", "Nowak", 30),
            model.Uzytkownik("Piotr", "Wiśniewski", 40),
            model.Uzytkownik("Maria", "Dąbrowska", 22),
            model.Uzytkownik("Krzysztof", "Lewandowski", 35),
            model.Uzytkownik("Magdalena", "Wójcik", 28),
            model.Uzytkownik("Tomasz", "Kamiński", 50),
            model.Uzytkownik("Ewa", "Zielińska", 33),
            model.Uzytkownik("Michał", "Szymański", 45),
            model.Uzytkownik("Aleksandra", "Woźniak", 29)
        ]
        self.book = [
            model.Ksiazka("SHERLOCK HOLMES: STUDIUM W SZKARLACIE", "ARTHUR CONAN DOYLE", 1887, 5),
            model.Ksiazka("ZBRODNIA I KARA", "FIODOR DOSTOJEWSKI", 1866, 2 ),
            model.Ksiazka("DUMA I UPRZEDZENIE", "JANE AUSTEN", 1813, 1),
            model.Ksiazka("ROK 1984", "GEORGE ORWELL", 1949, 5),
            model.Ksiazka("WLADCA PIERSCIENI", "J.R.R. TOLKIEN", 1954, 8),
            model.Ksiazka("MISTRZ I MALGORZATA", "MICHAIL BULHAKOW", 1967, 2),
            model.Ksiazka("HOBBIT", "J.R.R. TOLKIEN", 1937, 3),
            model.Ksiazka("MALY KSIAZE", "ANTOINE DE SAINT-EXUPERY", 1943, 1),
            model.Ksiazka("BUSZUJACY W ZBOZU", "J.D. SALINGER", 1951, 7),
            model.Ksiazka("HARRY POTTER I KAMIEN FILOZOFICZNY", "J.K. ROWLING", 1997, 2),
            model.Ksiazka("IMIE ROZY", "UMBERTO ECO", 1980, 1),
            model.Ksiazka("GRA O TRON", "GEORGE R.R. MARTIN", 1996, 1),
            model.Ksiazka("FOLWARK ZWIERZECY", "GEORGE ORWELL", 1945, 8),
            model.Ksiazka("OJCIEC CHRZESTNY", "MARIO PUZO", 1969, 2),
            model.Ksiazka("LALKA", "BOLESLAW PRUS", 1890, 7)
        ]

    def spis_ksiazek(self):
        n = 0
        spis = ""
        for i in self.book:
            n += 1
            spis += (f'{n}. Tytuł -> {i.tytul}, Autor -> {i.autor}, rok wydania -> {i.rok}, ilość -> {i.ilosc}\n')
        return spis

    def lista_uzytkownikow(self):
        for i in self.user:
            print(f'Imie i nazwisko: {i.imie} {i.nazwisko}, wiek: {i.wiek}, wypozyczone ksiazki {i.lista_ksiazek}')

dane = Dane()
