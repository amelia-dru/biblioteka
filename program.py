import dane
import bibliotekarz
import uzyt
import data

info = dane.Dane()

while True:
    user = int(input('logujesz sie jako 1.pracownik czy 2.uzytkownik? lub 3.koniec '))
    if user == 1:
        logowanie = input(('Podaj haslo(1212): '))
        if logowanie == '1212':
            while True:
                biblio = bibliotekarz.Bibliotekarz(info)
                biblio.wczytywanie_z_pliku_ksiazki()
                biblio.wczytywanie_uzytkownikow_z_listy()
                czynnosc = int(input(f'Jaka czynnosc chcesz wykonac?\n1.lista ksiazek\n2.dodaj ksiazke\n3.usun ksiazke\n'
                                     f'4.wypozycz\n5.zwroc\n6.zaloz konto\n7.lista uzytkownikow\n8.wyszukaj osobe\n'
                                     f'9.zapisz do pliku spis ksiazek\n10.zapisz do pliku spisu uzytkownikow\n11.usuwanie uzytkownika z systemu\n12.zakoncz '))
                
                if czynnosc == 1:
                    biblio.wyswietlanie()

                if czynnosc == 2:
                    biblio.dodawanie()

                if czynnosc == 3:
                    biblio.usuwanie()

                if czynnosc == 4:
                    biblio.wypozyczenie()

                if czynnosc == 5:
                    biblio.zwrot()
                
                if czynnosc == 6:
                    biblio.zaloz_konto()

                if czynnosc == 7:
                    biblio.lista_uzytkownikow()
                
                if czynnosc == 8:
                    biblio.wyszukiwanie_osoby()
                
                if czynnosc == 9:
                    biblio.zapisywanie_ksiazek()

                if czynnosc == 10:
                    biblio.zapisywanie_listy_uzyt()

                if czynnosc == 11:
                    biblio.usuwanie_uztykownikow()
                
                if czynnosc == 12:
                    break
        else:
            print('wpisano zle haslo')
                
    if user == 2:
        nazwa = input('Podaj imie i nazwisko: ').strip().split(' ')
        uzyt1 = uzyt.Uzytkownik(nazwa, dane)
        uzyt1.logowanie()
        if uzyt1.znalezienie == True:
            while True:
                wybor = int(input(f'Jaka czynnosc chcesz wykonac?\n1.wypozycz ksiazke\n2.zwroc ksiazke\n3.zobacz zbior ksiazek\n4.zakoncz '))
                if wybor == 1:
                    uzyt1.wypozyczenie() 

                if wybor == 2:
                    uzyt1.zwroc()

                if wybor == 3:
                    uzyt1.lista()

                if wybor == 4:
                    break
    
    if user == 3:
        break

                
            

            
