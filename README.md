# Learning-Python
Primitive example of "learning" done as exercise for class
#Pliki fromFileTo2D.py oraz fromFileTo2D2.py sluza do wypelnienia tablic tableInterval1 oraz tableInterval2
    #rekordami zapisanymi w pliku learning.txt w sposob jak zaprezentowany nizej na przykladzie tabel
    #Int1 oraz Int2. Po podaniu przedzialow 1 i 2 nastepuje wyliczenie prawdopodobienstwa z jakim dane przedzialy
    # naleza do konkretnej klasy.
    
    PROGRAM URUCHAMIAMY Z PLIKU INDEX2.py - w pliku INDEX.py jest starsza wersja działająca bez naiwnego klasyfikatora
    bayesowskiego
    
    TO sa pogladowe tabele - tabela tableInterval1 oraz tableInterval2 (parametry aktualne funkcji naiveBayes
    wygladaja tak samo:
    Wartosci w kolumnach to nastepujaco:
     przedzial, ilosc wystapien, ilosc wystapien jesli A, ilosc wystapien jesli B, ilosc wystapien jesli C
     Int1 = [['[4; 5)', 43, 0, 37, 6],
               ['[5; 6)', 35, 0, 2, 33],
               ['[1; 2)', 50, 50, 0, 0],
               ['[3; 4)', 11, 0, 11, 0],
             ['[6; 7)', 11, 0, 0, 11]]
     Int2 = [['[1; 1,5)', 36, 0, 35, 1],
             ['[1,5; 2)', 35, 0, 15, 20],
             ['[0; 0,5)', 48, 48, 0, 0],
             ['[2,5; 3)', 3, 0, 0, 3],
             ['[2: 2,5)', 26, 0, 0, 26],
             ['[0,5: 1)', 2, 2, 0, 0]]
