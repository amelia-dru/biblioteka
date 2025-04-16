import model
import dane
import data

class Bibliotekarz:
    def __init__(self, dane):
        self.dane = dane
    
    def wyswietlanie(self):
        l = 0
        for i in dane.book: #wedlug mnie zapis powinien wygladac tak -> self.dane.book
            l += 1
            print(f'{l}. Tytuł: {i.tytul.title()}, Autor: {i.autor.title()}, Rok wydania: {i.rok}, Dostepna ilsoc: {i.ilosc}')

    def pobieranie_inforamcji_o_ksiazce(self):
        tytul = input('Podaj tytul: ').strip().upper()
        autor = input('Podaj autora: ').strip().upper()
        rok = int(input('Podaj rok: '))
        return tytul, autor, rok
    
    def pobieranie_danych_uzytkownika(self):
        nazwa = input('Podaj imie i nzawisko: ').strip().split(' ')
        imie = nazwa[0].capitalize()
        nazwisko = nazwa[1].capitalize()
        wiek = int(input('Podaj wiek: '))
        return imie, nazwisko, wiek

    def dodawanie(self):
        tytul, autor, rok = self.pobieranie_inforamcji_o_ksiazce()
        znalezienie = False
        for i in dane.book: #wedlug mnie -> self.dane.book
            if i.tytul == tytul and  i.autor == autor and i.rok == rok:
                i.ilosc += 1
                znalezienie = True
                break
        if znalezienie == False:
            ksiazka_do_dodania = model.Ksiazka(tytul, autor, rok, 1)
            dane.book.append(ksiazka_do_dodania) #-> #wedlug mnie -> self.dane.book
            print('super dodano ksiazke do zbioru')

    def usuwanie(self):
        tytul, autor = self.pobieranie_inforamcji_o_ksiazce()
        znalezniono = False
        for i in dane.book: #wedlug mnie -> self.dane.book
            if i.tytul == tytul and i.autor == autor:
                dane.book.remove(i) #wedlug mnie -> self.dane.book.remove
                print(f'ksiazka {i.szczegoly()} zostala usunieta')
                znalezniono = True
                break
        if znalezniono == False:
            print('ksiazka nie wystepuje w naszym zbiorze.')

    def wypozyczenie(self):
        imie, nazwisko = self.pobieranie_danych_uzytkownika()
        znalazlam = False
        for i in dane.user: ##wedlug mnie -> self.dane.user
            if i.imie == imie and i.nazwisko == nazwisko:
                tytul = input('Podaj tytul ksiazki: ').strip().upper()
                for ii in dane.book: #wedlug mnie -> self.dane.book
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
        for i in dane.user: #wedlug mnie -> self.dane.user
            liczba += 1
            if len(i.lista_ksiazek) == 0:
                print(f'{liczba}. Imie i nazwisko: {i.imie} {i.nazwisko}, wiek: {i.wiek}, lista ksiazek: BRAK')
            else:
                print(f'{liczba}. Imie i nazwisko: {i.imie} {i.nazwisko}, wiek: {i.wiek}, lista ksiazek: {i.lista_ksiazek}')

    def zwrot(self):
        imie, nazwisko = self.pobieranie_danych_uzytkownika()
        znalazlam = False
        brak_imienia = False
        for i in dane.user: #wedlug mnie -> self.dane.user
            if i.imie == imie and i.nazwisko == nazwisko:
                tytul = input('Podaj tytul: ').strip().upper()
                brak_imienia = True
                if tytul in i.lista_ksiazek:
                    i.lista_ksiazek.remove(tytul)
                    for x in dane.book: #wedlug mnie -> self.dane.book
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

                dane.book.append(model.Ksiazka(tytul, autor, rok, 1)) #wedlug mnie -> self.dane.book.append
                print('Dzięki za poszerzenie naszego zbioru!')
            else:
                print('Okej.')
    
    def zaloz_konto(self):
        imie, nazwisko, wiek = self.pobieranie_danych_uzytkownika()
        znaleziono = False
        for i in dane.user: #wedlug mnie -> self.dane.user
            if i.imie == imie and i.nazwisko == nazwisko:
                print('Taka osoba juz posiada konto w naszej bibliotece')
                znaleziono = True
                break
        if znaleziono == False:
            dane.user.append(model.Uzytkownik(imie, nazwisko, wiek)) #wedlug mnie -> self.dane.user.apppend
            print(f'super udalo zalozyc sie konto dla uczytkownika {imie} {nazwisko}')

    def wyszukiwanie_osoby(self):
        imie, nazwisko, wiek = self.pobieranie_danych_uzytkownika()
        znaleziono = False
        for i in dane.user: #wedlug mnie -> self.dane.user
            if i.imie == imie and i.nazwisko == nazwisko:
                if len(i.lista_ksiazek) == 0:
                    print(f'Imie i nazwisko: {i.imie} {i.nazwisko}, wiek: {i.wiek}, lista ksiazek: BRAK')
                else:
                    print(f'Imie i nazwisko: {i.imie} {i.nazwisko}, wiek: {i.wiek}, lista ksiazek: {i.lista_ksiazek}')
                znaleziono = True
                break
        if znaleziono == False:
            print('Uzytkownik nie znajduje sie w naszej bazie')

bibliotekarz = Bibliotekarz(dane)
