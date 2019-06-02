from array import *
from fromFileTo2D2 import *
from fromFileTo2D import *

x = 0
while (x in [0, 1]):
    #Pliki fromFileTo2D.py oraz fromFileTo2D2.py sluza do wypelnienia tablic tableInterval1 oraz tableInterval2
    #rekordami zapisanymi w pliku learning.txt w sposob jak zaprezentowany nizej na przykladzie tabel
    #Int1 oraz Int2. Po podaniu przedzialow 1 i 2 nastepuje wyliczenie prawdopodobienstwa z jakim dane przedzialy
    # naleza do konkretnej klasy.

    #TO sa pogladowe tabele - tabela tableInterval1 oraz tableInterval2 (parametry aktualne funkcji naiveBayes
    #wygladaja tak samo:
    #Wartosci w kolumnach to nastepujaco:
    # przedzial, ilosc wystapien, ilosc wystapien jesli A, ilosc wystapien jesli B, ilosc wystapien jesli C
    # Int1 = [['[4; 5)', 43, 0, 37, 6],
    #           ['[5; 6)', 35, 0, 2, 33],
    #           ['[1; 2)', 50, 50, 0, 0],
    #           ['[3; 4)', 11, 0, 11, 0],
    #         ['[6; 7)', 11, 0, 0, 11]]
    # Int2 = [['[1; 1,5)', 36, 0, 35, 1],
    #         ['[1,5; 2)', 35, 0, 15, 20],
    #         ['[0; 0,5)', 48, 48, 0, 0],
    #         ['[2,5; 3)', 3, 0, 0, 3],
    #         ['[2: 2,5)', 26, 0, 0, 26],
    #         ['[0,5: 1)', 2, 2, 0, 0]]

    def naiveBayes(int1p, int2p):
        for i in range(5):
            if (int1p[i][0] == interval1):

                interval_first_row = i
            else:
                ()
        for i in range(6):
            if (int2p[i][0] == interval2):

                interval_second_row = i
            else:
                ()

        for i in range(3):
            w = i + 2
            # tutaj w funkcji mnozone jest prawdopodobienstwo dla jednego i drugiego przedzialu
            result = (int1p[interval_first_row][w] / 50) * (int2p[interval_second_row][w] / 50)
            print(result)
            if (w == 2):
                print('a ^')
            elif (w == 3):
                print('b ^')
            elif (w == 4):
                print('c ^')

    print("\n\nWybierz co chcesz zrobic:")
    print("1. Sprawdź przedział")
    print("2. Zakoncz dzialanie programu\n")
    choice = input("Podaj co chcesz zrobic: ")
    x = 0
    if choice == '1':
        x = 1
        a = input("Podaj poczatek pierwszego przedzialu: ")
        b = input("Podaj koniec pierwszego przedzialu: ")
        c = input("Podaj poczatek pierwszego przedzialu: ")
        d = input("Podaj koniec drugiego przedzialu: ")
        # new_interval = ("[%s; %s)|[%s; %s)" % (a, b, c, d))
        interval1 = ("[%s; %s)" % (a, b))
        interval2 = ("[%s; %s)" % (c, d))
        interval1value = 0
        interval_first_row = 0
        interval_second_row = 0
        # print(interval1)
        naiveBayes(tableInterval1, tableInterval2)
    elif choice == '2':
        x = 2
        break