from ksiazki import lista
from ksiazki import Ksiazka
from metody import dodawanie

user = int(input('logujesz sie jako 1.pracownik czy 2.uzytkownik? '))
if user == 1:
    logowanie = input(('Podaj haslo(1212): '))
    if logowanie == '1212':
        while True:
            czynnosc = int(input('Jaka czynnosc chcesz wykonac? 1.lista ksiazek, 2.dodaj ksiazke, 3.usun ksiazke   '))
            if czynnosc == 1:
                for i in lista:
                    print(i.szczegoly())

            if czynnosc == 2:
                '''tytul = input('Podaj tytul: ').strip().title()
                autor = input('Podaj autora: ').strip().title()
                rok = int(input('Podaj rok'))
                ksiazka_do_dodania = Ksiazka(tytul, autor, rok)
                lista.append(ksiazka_do_dodania)
                print('super dodano ksiazke do zbioru')''' #opcja 1 spakowana w pliky metody.py

                dodawanie() #opcja 2, ktora nie dziala nie wiem dlaczego 



            if czynnosc == 3:
                tytul = input('Podaj tytul: ').upper()
                autor = input('Podaj autora: ').upper()
                rok = int(input('Podaj rok'))
                ksiazka_do_usuniecia = Ksiazka(tytul, autor, rok)
                if ksiazka_do_usuniecia in lista:
                    lista.remove(ksiazka_do_usuniecia)
                    print('super udalo sie usunac ksiazke ze zbioru')
                else:
                    print('taka ksiazka nie znajduje sie w zbiorze') 
                    # mam problem z wielkoscia liter. w jakim miejscu najlepiej bd dodac upper/lower do listy aby wszystko smigalo?

                
            
#mam tez problem aby "if czynnosc == 2 oraz czynnosc == 3" spakowac jako metode w innym pliku tak aby dzialalo 
# wyskakuje mi taki blad -> cannot import name 'dodawanie' from 'metody'
#sprawdzaam pisownie i lokalizacje pliku wszystko jest ok wiec nie wiem z czego moze wynikac blad
