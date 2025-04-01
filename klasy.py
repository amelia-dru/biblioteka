import model
import random

def data():
    dzien = random.randint(1, 30)
    miesiac = random.randint(1,12)
    rok = random.randint(2025,2027)
    if dzien < 10:
        dzien = '0' + str(dzien)
    if miesiac < 10:
        miesiac = '0' + str(miesiac)
    return f'{dzien}.{miesiac},{rok}'

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

class Bibliotekarz(Dane):
    def __init__(self):
        super().__init__()  # Inicjalizacja klasy bazowej
    
    def wyswietlanie(self):
        l = 0
        for i in self.book:
            l += 1
            print(f'{l}. Tytuł: {i.tytul.title()}, Autor: {i.autor.title()}, Rok wydania: {i.rok}, Dostepna ilsoc: {i.ilosc}')

    def dodawanie(self):
        tytul = input('Podaj tytul: ').strip().upper()
        autor = input('Podaj autora: ').strip().upper()
        rok = int(input('Podaj rok: '))
        znalezienie = False
        for i in self.book:
            if i.tytul == tytul and i.autor == autor and i.rok == rok:
                i.ilosc += 1
                znalezienie = True
                break
        if znalezienie == False:
            ksiazka_do_dodania = model.Ksiazka(tytul, autor, rok, 1)
            self.book.append(ksiazka_do_dodania)
            print('super dodano ksiazke do zbioru')

    def usuwanie(self):
        tytul = input('Podaj tytul: ').upper()
        autor = input('Podaj autora: ').upper()
        znalezniono = False
        for i in self.book:
            if i.tytul == tytul and i.autor == autor:
                self.book.remove(i)
                print(f'ksiazka {i.szczegoly()} zostala usunieta')
                znalezniono = True
                break
        if znalezniono == False:
            print('ksiazka nie wystepuje w naszym zbiorze.')

    def wypozyczenie(self):
        nazwa = input('Podaj imie i nzawisko: ').strip().split(' ')
        imie = nazwa[0].capitalize()
        nazwisko = nazwa[1].capitalize()
        znalazlam = False
        for i in self.user:
            if i.imie == imie and i.nazwisko == nazwisko:
                tytul = input('Podaj tytul ksiazki: ').strip().upper()
                for ii in self.book:
                    if ii.tytul == tytul:
                        if ii.ilosc >= 1:
                            ii.ilosc -= 1
                            znalazlam = True
                            i.lista_ksiazek.append(tytul)
                            print(f'super udalo ci sie wypozyczyc ksiazke {tytul}, masz czas na zwrot do {data()}')
                            break
                        if ii.ilosc <= 0:
                            print(f'ksiazka aktalnie jest w obiegu, bedzie dostepna dopiero {data()}')
        if znalazlam == False:
            print('Przykro mi taka ksiazka nie znajuduje sie w naszym aktualnym zbiorze')

    def lista_uzytkownikow(self):
        liczba = 0
        for i in self.user:
            liczba += 1
            if len(i.lista_ksiazek) == 0:
                print(f'{liczba}. Imie i nazwisko: {i.imie} {i.nazwisko}, wiek: {i.wiek}, lista ksiazek: BRAK')
            else:
                print(f'{liczba}. Imie i nazwisko: {i.imie} {i.nazwisko}, wiek: {i.wiek}, lista ksiazek: {i.lista_ksiazek}')

    def zwrot(self):
        nazwa = input('Podaj imie i nzawisko: ').strip().split(' ')
        imie = nazwa[0].capitalize()
        nazwisko = nazwa[1].capitalize()
        znalazlam = False
        brak_imienia = False
        for i in self.user:
            if i.imie == imie and i.nazwisko == nazwisko:
                tytul = input('Podaj tytul: ').strip().upper()
                brak_imienia = True
                if tytul in i.lista_ksiazek:
                    i.lista_ksiazek.remove(tytul)
                    for x in self.book:
                        if tytul == x.tytul:
                            x.ilosc += 1
                            print('dzieki za zwrot!')
                            znalazlam = True
                            break
        if brak_imienia == False:
            print('taki uztkownik nie znajduje sie w naszej bazie uzytkownikow prosze zalozyc konto.')
            return
        
        if not znalazlam:
            print('Taki tytuł nie znajduje się w naszym zbiorze. Jeśli chcesz nam go podarować, potrzebujemy kilku szczegółów.')
            while True:
                try:
                    wybor = int(input('1. Tak, 2. Nie: '))
                    if wybor in [1, 2]:
                        break 
                    else:
                        print('Podaj 1 lub 2.')
                except ValueError:
                    print('Podaj 1 lub 2.')

            if wybor == 1:
                autor = input('Podaj autora: ').strip().capitalize()

                while True:
                    try:
                        rok = int(input('Podaj rok: '))
                        break 
                    except ValueError:
                        print('Podaj rok w postaci liczb.')

                self.book.append(model.Ksiazka(tytul, autor, rok, 1))
                print('Dzięki za poszerzenie naszego zbioru!')
            else:
                print('Okej.')
    
    def zaloz_konto(self):
        nazwa = input('Podaj imie i nzawisko: ').strip().split(' ')
        imie = nazwa[0].capitalize()
        nazwisko = nazwa[1].capitalize()
        wiek = int(input('Podaj wiek: '))
        znaleziono = False
        for i in self.user:
            if i.imie == imie and i.nazwisko == nazwisko:
                print('Taka osoba juz posiada konto w naszej bibliotece')
                znaleziono = True
                break
        if znaleziono == False:
            self.user.append(model.Uzytkownik(imie, nazwisko, wiek))
            print(f'super udalo zalozyc sie konto dla uczytkownika {imie} {nazwisko}')

    def wyszukiwanie_osoby(self):
        nazwa = input('Podaj imie i nzawisko: ').strip().split(' ')
        imie = nazwa[0].capitalize()
        nazwisko = nazwa[1].capitalize()
        znaleziono = False
        for i in self.user:
            if i.imie == imie and i.nazwisko == nazwisko:
                if len(i.lista_ksiazek) == 0:
                    print(f'Imie i nazwisko: {i.imie} {i.nazwisko}, wiek: {i.wiek}, lista ksiazek: BRAK')
                else:
                    print(f'Imie i nazwisko: {i.imie} {i.nazwisko}, wiek: {i.wiek}, lista ksiazek: {i.lista_ksiazek}')
                znaleziono = True
                break
        if znaleziono == False:
            print('Uzytkownik nie znajduje sie w naszej bazie')

class Uzytkownik(Dane):
    def __init__(self, nazwa):
        super().__init__()
        self.znalezienie = False
        self.nazwa = nazwa
        self.imie = self.nazwa[0].capitalize()
        self.nazwisko = self.nazwa[1].capitalize()
        try:   
            if len(self.nazwa) > 1: 
                for i in self.user:
                    if i.imie == self.imie and i.nazwisko == self.nazwisko:
                        self.znalezienie = True
                        break
        except IndexError:
            print('Wpisz imie i nazwisko')

    def logowanie(self):
        while True:
            if self.znalezienie == False:
                print('Niestety taki uzytkownik nie znajduje sie w naszej bazie, prosze utowrzyc konto')
            elif self.znalezienie == True:
                print('Zalogowano pomyslnie')
                break

    def wypozyczenie(self):
        tytul = input('Wpisz tytul: ').strip().upper()
        autor = input('Wpisz autora: ').strip().upper()
        znalezienie = False
        for i in self.book:
            if i.tytul == tytul and i.autor == autor and i.dostepnosc >= 1:
                znalezienie = True
                for y in self.user:
                    if y.imie == self.imie and y.nazwisko == self.nazwisko:
                        i.ilosc -= 1
                        y.lista_ksiazek.append(i.tytul)
                        print(f'ksiazja jest juz twoja do dnia {data()}')
                        break

        if znalezienie == False:
            print(f'Niestety nie mamy aktualnie {tytul} na stanie')

    def zwroc(self):
        tytul = input('Podaj tytul: ').strip().upper()
        autor = input('Podaj autora: ').strip().upper()
        znalezienie = False
        for i in self.book:
            if i.autor == autor and i.tytul == tytul:
                znalezienie = True
                for y in self.user:
                    if y.imie == self.imie and y.nazwisko == self.nazwisko:
                        i.ilosc += 1
                        y.lista_ksiazek.remove(i.tytul)
                        print(f'Dzieki za zwrot\n')
                        break
        if not znalezienie:
            print('Taka ksiazka nie znajduje sie w naszym zbiorze')
            
    def lista(self):
        n = 0
        print()
        for i in self.book:
            n += 1
            print(f'{n}.Tytuł: {i.tytul}, Autor: {i.autor}, Rok: {i.rok}, Ilość: {i.ilosc}')


bibliotekarz = Bibliotekarz()
