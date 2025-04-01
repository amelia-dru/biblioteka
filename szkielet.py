import klasy
import model

user = int(input('logujesz sie jako 1.pracownik czy 2.uzytkownik? '))
if user == 1:
    logowanie = input(('Podaj haslo(1212): '))
    if logowanie == '1212':
        while True:
            czynnosc = int(input(f'Jaka czynnosc chcesz wykonac?\n1.lista ksiazek\n2.dodaj ksiazke\n3.usun ksiazke\n4.wypozycz\n5.zwroc\n6.zaloz konto\n7.lista uzytkownikow\n8.wyszukaj osobe\n9.zakoncz  '))
            
            if czynnosc == 1:
                klasy.bibliotekarz.wyswietlanie()

            if czynnosc == 2:
                klasy.bibliotekarz.dodawanie()

            if czynnosc == 3:
                klasy.bibliotekarz.usuwanie()

            if czynnosc == 4:
                klasy.bibliotekarz.wypozyczenie()

            if czynnosc == 5:
                klasy.bibliotekarz.zwrot()
            
            if czynnosc == 6:
                klasy.bibliotekarz.zaloz_konto()

            if czynnosc == 7:
                klasy.bibliotekarz.lista_uzytkownikow()
            
            if czynnosc == 8:
                klasy.bibliotekarz.wyszukiwanie_osoby()
            
            if czynnosc == 9:
                break
    else:
        print('wpisano zle haslo')
            
if user == 2:
    nazwa = input('Podaj imie i nazwisko: ').strip().split(' ')
    uzyt = klasy.Uzytkownik(nazwa)
    uzyt.logowanie()
    if uzyt.znalezienie == True:
        while True:
            wybor = int(input(f'Jaka czynnosc chcesz wykonac?\n1.wypozycz ksiazke\n2.zwroc ksiazke\n3.zobacz zbior ksiazek '))
            if wybor == 1:
                uzyt.wypozyczenie() 

            if wybor == 2:
                uzyt.zwroc()

            if wybor == 3:
                uzyt.lista()

                
            

            
