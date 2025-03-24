import metody

from dane import uzytkownicy
user = int(input('logujesz sie jako 1.pracownik czy 2.uzytkownik? '))
if user == 1:
    logowanie = input(('Podaj haslo(1212): '))
    if logowanie == '1212':
        while True:
            czynnosc = int(input(f'Jaka czynnosc chcesz wykonac?\n1.lista ksiazek\n2.dodaj ksiazke\n3.usun ksiazke\n4.wypozycz\n5.zwroc\n6.zaloz konto\n7.lista uzytkownikow\n8.wyszukaj osobe\n9.zakoncz  '))
            
            if czynnosc == 1:
                metody.wyswietlanie()

            if czynnosc == 2:
                metody.dodawanie()

            if czynnosc == 3:
                metody.usuwanie()

            if czynnosc == 4:
                metody.wypozyczenie()

            if czynnosc == 5:
                metody.zwrot()
            
            if czynnosc == 6:
                metody.zaloz_konto()

            if czynnosc == 7:
                metody.lista_uzytkownikow()
                
            if czynnosc == 8:
                metody.wyszukiwanie_osoby()
            
            if czynnosc == 9:
                break
    else:
        print('wpisano zle haslo')
            
if user == 2:
    nazwa = input('Podaj imie i nazwisko: ').split(' ')
    imieklucz = nazwa[0].strip().capitalize()
    nazwiskoklucz = nazwa[1].strip().capitalize()
    for i in uzytkownicy:
        if i.imie == imieklucz and i.nazwisko == nazwiskoklucz:
            print('Zalogowano pomyslnie')
            wybor = int(input(f'Jaka czynnosc chcesz wykonac?\n1.wypozycz ksiazke\n2.zwroc ksiazke\n3.lista twoich wypozyczonych ksiazek\n4.zbior wszystkich ksiazek '))
            if wybor == 1:
                metody.wypozycz_uzytkownik()
                for i in uzytkownicy:
                    print(i.imie, i.lista_ksiazek)
            

