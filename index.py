x = 0
while (x in [0, 1, 2]):
    ###############################
    przedzialy = []
    klucz = []
    distinct = []

    with open('learning.txt', 'r') as file:
        line = file.readline()
        for myline in file:
            # print(myline[:15])
            przedzialy.append(myline[:len(myline) - 3])

    with open('learning.txt', 'r') as file:
        line = file.readline()
        for myline in file:
            # print(myline[:15])
            klucz.append(myline[len(myline) - 2:len(myline) - 1])

    matrix = [[0 for x in range(len(przedzialy))] for y in range(2)]

    for i in range(len(przedzialy)):
        matrix[0][i] = przedzialy[i]

    for i in range(len(klucz)):
        matrix[1][i] = klucz[i]

    for x in przedzialy:
        if x not in distinct:
            distinct.append(x)

    distinct_count = [[0 for x in range(len(distinct))] for y in range(4)]
    # for i in range(len(distinct)):
    #     print(distinct[i])

    for i in range(len(distinct)):
        for j in range(len(przedzialy)):
            if distinct[i] == matrix[0][j]:
                if matrix[1][j] == 'A':
                    distinct_count[0][i] += 1
                elif matrix[1][j] == 'B':
                    distinct_count[1][i] += 1
                elif matrix[1][j] == 'C':
                    distinct_count[2][i] += 1


    def recognition(dist, dist_count):
        for j in range(len(dist)):
            if dist_count[0][j] > dist_count[1][j] and dist_count[0][j] > dist_count[2][j]:
                dist_count[3][j] = 'A'
                print(dist[j] + " jest A")
            elif dist_count[1][j] > dist_count[0][j] and dist_count[1][j] > dist_count[2][j]:
                dist_count[3][j] = 'B'
                print(dist[j] + " jest B")
            elif dist_count[2][j] > dist_count[0][j] and dist_count[2][j] > dist_count[1][j]:
                dist_count[3][j] = 'C'
                print(dist[j] + " jest C")


    def setKey(_interval):
        file = open("learning.txt", "a+")
        print("Przedzial " + _interval + " nie moze byc zidentyfikowany w oparciu o obecnie posiadane dane.")
        key = input("Podaj klucz do tego przedzialu. Użyj jednego z aktualnie zastosowanych:")
        if key in ['A', 'B', 'C']:
            file.write(_interval + "|" + key + "\n")
        else:
            setKey()


    def interval(interval_, dist, dist_count):
        found = 0
        for k in range(len(dist)):
            if dist[k] == interval_:
                print("Przedzial " + interval_ + " jest zdentyfikowany jako: " + str(dist_count[3][k]))
                found += 1
        if found == 0:
            setKey(interval_)


    ###############################

    print("\n\nWybierz co chcesz zrobic:")
    print("1. Sprawdz przyporzadkowanie dla przedzialow z pliku")
    print("2. Dodaj przedzialy")
    print("3. Zakoncz dzialanie programu\n")
    choice = input("Podaj co chcesz zrobic: ")
    x = 0
    if choice == '1':
        x = 1
        recognition(distinct, distinct_count)
    elif choice == '2':
        x = 2
        a = input("Podaj poczatek pierwszego przedzialu: ")
        b = input("Podaj koniec pierwszego przedzialu: ")
        c = input("Podaj poczatek pierwszego przedzialu: ")
        d = input("Podaj koniec drugiego przedzialu: ")
        new_interval = ("[%s; %s)|[%s; %s)" % (a, b, c, d))

        recognition(distinct, distinct_count)
        interval(new_interval, distinct, distinct_count)
        choice2 = input("Czy chcesz dodac rekord dla tego przedzialu? 1 - TAK, 2 - NIE: ")
        if choice2 == '1':
            setKey(new_interval)

    elif choice == '3':
        x = 3
        break
