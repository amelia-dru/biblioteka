import data
import dane
import model

class Uzytkownik:
    def __init__(self, nazwa, dane):
        self.dane = dane
        self.znalezienie = False
        self.nazwa = nazwa.strip()
        podzial = self.nazwa.split(' ')
        self.imie = podzial[0]
        self.nazwisko = podzial[1]
        try:   
            if len(self.nazwa) > 1: 
                for i in self.dane.user:    #nie wiem jak to zapisac
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
        for i in dane.book: #dalczego nie self.dane.book?
            if i.tytul == tytul and i.autor == autor and i.dostepnosc >= 1:
                znalezienie = True
                for y in dane.user:#dalczego nie self.dane.book?
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
        for i in dane.book:#dalczego nie self.dane.book?
            if i.autor == autor and i.tytul == tytul:
                znalezienie = True
                for y in dane.user:#dalczego nie self.dane.user?
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
        for i in dane.book:#dalczego nie self.dane.book?
            n += 1
            print(f'{n}.Tytuł: {i.tytul}, Autor: {i.autor}, Rok: {i.rok}, Ilość: {i.ilosc}')
