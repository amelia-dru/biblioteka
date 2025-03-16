from ksiazki import lista
from ksiazki import Ksiazka

def dodawanie():
    tytul = input('Podaj tytul: ').strip().title()
    autor = input('Podaj autora: ').strip().title()
    rok = int(input('Podaj rok'))
    ksiazka_do_dodania = Ksiazka(tytul, autor, rok)
    lista.append(ksiazka_do_dodania)
    print('super dodano ksiazke do zbioru')