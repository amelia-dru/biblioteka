import model
'''import biblioteka.test as test'''
import dane
import os

class Bibliotekarz:
    def __init__(self, info:dane.Dane):
        self.info = info

    def lokalizowanie_pliku_z_uzytkowniakmi(self):
        self.find_uzyt = False
        if os.path.exists("spis_uzytklownikow.txt"):
            self.find_uzyt = True

    def wczytywanie_uzytkownikow_z_listy(self):
        self.lokalizowanie_pliku_z_uzytkowniakmi()
        if self.find_uzyt == True:
            with open('spis_uzytkownikow.txt', 'r') as plik:
                i = []
                nazwa = []
                w = []
                imie = []
                nazwisko = []
                wiek = []
                for z in plik:
                    podzial = z.split(':')
                    i.append(podzial[1])
                    w.append(podzial[2])

                for linijka in i:
                    nazwa.append(linijka.strip().split(',')[0])

                for os in nazwa:
                    podzial = os.split(' ')
                    imie.append(podzial[0])
                    nazwisko.append(podzial[1])

                for linia in w:
                    wiek.append(int(linia))

                self.lista_uzyt_finalna = [model.Uzytkownik(name,surname,age) for name, surname, age in zip(imie,nazwisko,wiek)]
        else:
            self.lista_uzyt_finalna = self.info.user

    def lokalizowanie_pliku(self):
        self.find = False
        if os.path.exists("spis_ksiazek.txt"):
            self.find = True

    def wczytywanie_z_pliku_ksiazki(self):
        self.lokalizowanie_pliku()
        if self.find == True:
            with open ('spis_ksiazek.txt', 'r') as plik:
                t = []
                a = []
                r = []
                tytul = []
                autor = []
                rok = []
                ilosc = []
                for i in plik:
                    podzial = i.split('->')
                    t.append(podzial[1])
                    a.append(podzial[2])
                    r.append(podzial[3])
                    ilosc.append(int(podzial[4].strip()))
                    

                for i in t:
                    tytul.append(i.strip().split(',')[0])
                
                for x in a:
                    autor.append(x.strip().split(',')[0])

                for y in r:
                    rok.append(int(y.strip().split(',')[0]))

                self.zbior = [model.Ksiazka(q, w, b, j) for q , w, b, j in zip(tytul, autor, rok, ilosc)]
        else:
            self.zbior = self.info.book
    
    def wyswietlanie(self):
        l = 0
        for i in self.zbior:
            l += 1
            print(f'{l}. Tytuł: {i.tytul.title()}, Autor: {i.autor.title()}, Rok wydania: {i.rok}, Dostepna ilsoc: {i.ilosc}')

    def pobieranie_inforamcji_o_ksiazce(self):
        self.metoda_tytul = input('Podaj tytul: ').strip().upper()
        self.metoda_autor = input('Podaj autora: ').strip().upper()
        self.metoda_rok = int(input('Podaj rok: '))
        return self.metoda_tytul, self.metoda_autor, self.metoda_rok
    
    def pobieranie_danych_uzytkownika(self):
        self.metofa_uzyt_nazwa = input('Podaj imie i nzawisko: ').strip().split(' ')
        self.metofa_uzyt_imie = self.metofa_uzyt_nazwa[0].capitalize()
        self.metofa_uzyt_nazwisko = self.metofa_uzyt_nazwa[1].capitalize()
        self.metofa_uzyt_wiek = int(input('Podaj wiek: '))
        return self.metofa_uzyt_imie, self.metofa_uzyt_nazwisko, self.metofa_uzyt_wiek

    def dodawanie(self):
        self.pobieranie_inforamcji_o_ksiazce()
        znalezienie = False
        for i in self.zbior:
            if i.tytul == self.metoda_tytul and  i.autor == self.metoda_autor and i.rok == self.metoda_rok:
                i.ilosc += 1
                znalezienie = True
                break
        if znalezienie == False:
            ksiazka_do_dodania = model.Ksiazka(self.metoda_tytul, self.metoda_autor, self.metoda_rok, 1)
            self.info.book.append(ksiazka_do_dodania)
            print('super dodano ksiazke do zbioru')
        
        self.zapisywanie_ksiazek()

    def usuwanie(self):
        self.pobieranie_inforamcji_o_ksiazce()
        znalezniono = False
        for i in self.zbior:
            if i.tytul == self.metoda_tytul and i.autor == self.metoda_autor:
                self.info.book.remove(i)
                print(f'ksiazka {i.szczegoly()} zostala usunieta')
                znalezniono = True
                break
        if znalezniono == False:
            print('ksiazka nie wystepuje w naszym zbiorze.')
        self.zapisywanie_ksiazek()

    def wypozyczenie(self):
        self.pobieranie_danych_uzytkownika()
        znalazlam = False
        for i in self.lista_uzyt_finalna:
            if i.imie == self.metofa_uzyt_imie and i.nazwisko == self.metofa_uzyt_nazwisko:
                tytul = input('Podaj tytul ksiazki: ').strip().upper()
                for ii in self.zbior:
                    if ii.tytul == tytul:
                        if ii.ilosc >= 1:
                            ii.ilosc -= 1
                            znalazlam = True
                            i.lista_ksiazek.append(tytul)
                            print(f'super udalo ci sie wypozyczyc ksiazke {tytul}, masz czas na zwrot do ...')
                            break
                        if ii.ilosc <= 0:
                            print(f'ksiazka aktalnie jest w obiegu, bedzie dostepna dopiero ...')
        if znalazlam == False:
            print('Przykro mi taka ksiazka nie znajuduje sie w naszym aktualnym zbiorze')

    def lista_uzytkownikow(self):
        liczba = 0
        for i in self.lista_uzyt_finalna: 
            liczba += 1
            if len(i.lista_ksiazek) == 0:
                print(f'{liczba}. Imie i nazwisko: {i.imie} {i.nazwisko}, wiek: {i.wiek}, lista ksiazek: BRAK')
            else:
                print(f'{liczba}. Imie i nazwisko: {i.imie} {i.nazwisko}, wiek: {i.wiek}, lista ksiazek: {i.lista_ksiazek}')

    def zwrot(self):
        imie, nazwisko = self.pobieranie_danych_uzytkownika()
        znalazlam = False
        brak_imienia = False
        for i in self.lista_uzyt_finalna:
            if i.imie == imie and i.nazwisko == nazwisko:
                tytul = input('Podaj tytul: ').strip().upper()
                brak_imienia = True
                if tytul in i.lista_ksiazek:
                    i.lista_ksiazek.remove(tytul)
                    for x in self.info.book:
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

                self.info.book.append(model.Ksiazka(tytul, autor, rok, 1)) 
                print('Dzięki za poszerzenie naszego zbioru!')
            else:
                print('Okej.')
    
    def zaloz_konto(self):
        imie, nazwisko, wiek = self.pobieranie_danych_uzytkownika()
        znaleziono = False
        for i in self.lista_uzyt_finalna:
            if i.imie == imie and i.nazwisko == nazwisko:
                print('Taka osoba juz posiada konto w naszej bibliotece')
                znaleziono = True
                break
        if znaleziono == False:
            self.info.user.append(model.Uzytkownik(imie, nazwisko, wiek))
            print(f'super udalo zalozyc sie konto dla uczytkownika {imie} {nazwisko}')

        self.zapisywanie_listy_uzyt()

    def wyszukiwanie_osoby(self):
        imie, nazwisko, wiek = self.pobieranie_danych_uzytkownika()
        znaleziono = False
        for i in self.lista_uzyt_finalna:
            if i.imie == imie and i.nazwisko == nazwisko:
                if len(i.lista_ksiazek) == 0:
                    print(f'Imie i nazwisko: {i.imie} {i.nazwisko}, wiek: {i.wiek}, lista ksiazek: BRAK')
                else:
                    print(f'Imie i nazwisko: {i.imie} {i.nazwisko}, wiek: {i.wiek}, lista ksiazek: {i.lista_ksiazek}')
                znaleziono = True
                break
        if znaleziono == False:
            print('Uzytkownik nie znajduje sie w naszej bazie')
            
    def zapisywanie_ksiazek(self):
        with open('spis_ksiazek.txt', 'w') as lista_ksiazek:
            n = 0
            for ii in self.info.book:
                n += 1
                lista_ksiazek.write(f"{n}. tytul -> {ii.tytul}, autor -> {ii.autor}, rok: -> {ii.rok}, ilosc -> {ii.ilosc}\n")

    def zapisywanie_listy_uzyt(self):
        with open('spis_uzytkownikow.txt', 'w') as plik:
            n = 0
            for i in self.info.user:
                n += 1
                plik.write(f'{n}. imie: {i.imie} {i.nazwisko}, wiek: {i.wiek}\n')
