from Classes.Engine import Engine
from Classes.Dictionary import Dictionary

file = open("data/zasady.txt")
eng = Engine()
dic = Dictionary()

while True:
    for col in ["1-Nowa Gra", "2-Zasady Gry", "3-Zmien poziom trudnosci", f"4-Zmien ilosc prob", f"5-Koniec"]:
        print(col)
    print(f"Aktualne ustawienia: ")
    print(f"Ilosc prob - {eng.getTries()}")
    if eng.getDifficulty() == 1:
        print("poziom trudnosci - Latwy")
    elif eng.getDifficulty() == 2:
        print("poziom trudnosci - Sredni")
    elif eng.getDifficulty() == 3:
        print("poziom trudnosci - Trudny")
    elif eng.getDifficulty() == 4:
        print("poziom trudnosci - Random")
    user = "0"
    try:
        user = input("Wybor[1-5]: ")
        if int(user) == 1:
            eng.game()
        elif int(user) == 2:
            print(file.read())
        elif int(user) == 3:
            try:
                while True:
                    user = int(input("Wybierz poziom trudnosci: \n1-Latwy[3-5]\n2-Sredni[6-8]\n"
                                     "3-Trudny[9+]\n4-Randomowe slowo(domyslny)\nWybierz: "))
                    if user == 1:
                        eng.setDifficulty(1)
                        break
                    elif user == 2:
                        eng.setDifficulty(2)
                        break
                    elif user == 3:
                        eng.setDifficulty(3)
                        break
                    elif user == 4:
                        eng.setDifficulty(4)
                        break
                    else:
                        print("Musisz podac liczbe!")
            except ValueError:
                print("To nie jest liczba")
        elif int(user) == 4:
            try:
                eng.setTries(int(input("Podaj liczbe prob: ")))
            except ValueError:
                print("To nie jest liczba")
        elif int(user) == 5:
            break
        else:
            print("Musisz wybrać jakąś opcje!")
    except ValueError:
        print("To nie jest liczba")
