from dane import lista, Uzytkownik
from dane import Ksiazka, uzytkownicy
import random
'''from biblioteka_1 import imieklucz, nazwiskoklucz'''

'''def wypozycz_uzytkownik():
    tytul = input('Podaj tytul: ').strip().upper()
    autor = input('Podaj autora: ').strip().upper()
    znalezniono = False
    
    for i in lista:
        if i.tytul == tytul and i.autor == autor:
            
            if i.ilosc == 0:
                print(f'niestety ksiazka aktualnie jest nie dostępna w naszej biblotece, bedzie dosetpna dopiero {data()}')
            
            elif i.ilosc >= 1:
                i.ilosc -= 1
                print(f'ksiazka zostala wypozyczona, masz czas na oddanie do {data()}')
                
                for g in uzytkownicy:
                    
                    if g.imie == imieklucz and g.nazwisko == nazwiskoklucz:
                        g.lista_ksiazek.append(i)
            znalezniono = True
            break'''

'''    if znalezniono == False:
        print('niesety taka ksiazka nie znajduje sie w naszych zbiorach')'''

#metody dla bibliotekarza

def data():
    dzien = random.randint(1, 30)
    miesiac = random.randint(1,12)
    rok = random.randint(2025,2027)
    if dzien < 10:
        dzien = '0' + str(dzien)
    if miesiac < 10:
        miesiac = '0' + str(miesiac)
    return f'{dzien}.{miesiac},{rok}'

def dodawanie():
    tytul = input('Podaj tytul: ').strip().upper()
    autor = input('Podaj autora: ').strip().upper()
    rok = int(input('Podaj rok: '))
    ksiazka_do_dodania = Ksiazka(tytul, autor, rok, 1)
    lista.append(ksiazka_do_dodania)
    print('super dodano ksiazke do zbioru')


def usuwanie():
    tytul = input('Podaj tytul: ').upper()
    autor = input('Podaj autora: ').upper()
    znalezniono = False
    for i in lista:
        if i.tytul == tytul and i.autor == autor:
            lista.remove(i)
            print(f'ksiazka {i.szczegoly()} zostala usunieta')
            znalezniono = True
            break
    if znalezniono == False:
        print('ksiazka nie wystepuje w naszym zbiorze.')


def wyswietlanie():
    l = 0
    for i in lista:
        l += 1
        print(f'{l}. Tytuł: {i.tytul.title()}, Autor: {i.autor.title()}, Rok wydania: {i.rok}, Dostepna ilsoc: {i.ilosc}')



'''def zwroc():
    tytul = input('Podaj tytul: ').upper()
    autor = input('Podaj autora: ').upper()
    znalezniono = False
    for i in lista:
        if i.tytul == tytul and i.autor == autor:
            i.ilosc += 1
            print('super dzieki za zwrot')
            znalezniono = True
            break
    if znalezniono == False:
        print('niesety taka ksiazka nie znajduje sie w naszych zbiorach')''' #dla uzytkowika

    
def zaloz_konto():
    nazwa = input('Podaj imie i nzawisko: ').strip().split(' ')
    imie = nazwa[0].capitalize()
    nazwisko = nazwa[1].capitalize()
    wiek = int(input('Podaj wiek: '))
    znaleziono = False
    for i in uzytkownicy:
        if i.imie == imie and i.nazwisko == nazwisko:
            print('Taka osoba juz posiada konto w naszej bibliotece')
            znaleziono = True
            break
    if znaleziono == False:
        uzytkownicy.append(Uzytkownik(imie, nazwisko, wiek))
        print(f'super udalo zalozyc sie konto dla uczytkownika {imie} {nazwisko}')

def lista_uzytkownikow():
    liczba = 0
    for i in uzytkownicy:
        liczba += 1
        if len(i.lista_ksiazek) == 0:
            print(f'{liczba}. Imie i nazwisko: {i.imie} {i.nazwisko}, wiek: {i.wiek}, lista ksiazek: BRAK')
        else:
            print(f'{liczba}. Imie i nazwisko: {i.imie} {i.nazwisko}, wiek: {i.wiek}, lista ksiazek: {i.lista_ksiazek}')

    
def wyszukiwanie_osoby():
    nazwa = input('Podaj imie i nzawisko: ').strip().split(' ')
    imie = nazwa[0].capitalize()
    nazwisko = nazwa[1].capitalize()
    znaleziono = False
    for i in uzytkownicy:
        if i.imie == imie and i.nazwisko == nazwisko:
            if len(i.lista_ksiazek) == 0:
                print(f'Imie i nazwisko: {i.imie} {i.nazwisko}, wiek: {i.wiek}, lista ksiazek: BRAK')
            else:
                print(f'Imie i nazwisko: {i.imie} {i.nazwisko}, wiek: {i.wiek}, lista ksiazek: {i.lista_ksiazek}')
            znaleziono = True
            break
    if znaleziono == False:
        print('Uzytkownik nie znajduje sie w naszej bazie')


def wypozyczenie():
    nazwa = input('Podaj imie i nzawisko: ').strip().split(' ')
    imie = nazwa[0].capitalize()
    nazwisko = nazwa[1].capitalize()
    znalazlam = False
    for i in uzytkownicy:
        if i.imie == imie and i.nazwisko == nazwisko:
            tytul = input('Podaj tytul ksiazki: ').strip().upper()
            for ii in lista:
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

def zwrot():
    nazwa = input('Podaj imie i nzawisko: ').strip().split(' ')
    imie = nazwa[0].capitalize()
    nazwisko = nazwa[1].capitalize()
    znalazlam = False
    brak_imienia = False
    for i in uzytkownicy:
        if i.imie == imie and i.nazwisko == nazwisko:
            tytul = input('Podaj tytul: ').strip().upper()
            brak_imienia = True
            if tytul in i.lista_ksiazek:
                i.lista_ksiazek.remove(tytul)
                for x in lista:
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

        lista.append(Ksiazka(tytul, autor, rok, 1))
        print('Dzięki za poszerzenie naszego zbioru!')
    else:
        print('Okej.')
                 

#uzytkownicy

