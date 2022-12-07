from Classes.Dictionary import Dictionary
from Classes.Validator import Validator
from Classes.Stats import Stats

class Engine:
    def __init__(self):
        self.difficulty = 4
        self.dictionary = Dictionary()
        self.validator = Validator()
        self.tries = 10
        self.word = None
        self.wordlen = None
        self.stats = Stats()

    def setDifficulty(self, x):
        self.difficulty = x

    def getDifficulty(self):
        return self.difficulty

    def setTries(self, x):
        self.tries = x

    def getTries(self):
        return self.tries

    def giveWordOnDifficulty(self):
        self.word = self.dictionary.giveWord()
        if self.difficulty == 1:
            while len(self.word) > 5 or len(self.word) < 3:
                self.word = self.dictionary.giveWord()
        elif self.difficulty == 2:
            while len(self.word) > 8 or len(self.word) < 6:
                self.word = self.dictionary.giveWord()
        elif self.difficulty == 3:
            while len(self.word) < 9:
                self.word = self.dictionary.giveWord()
        elif self.difficulty == 4:
            self.word = self.dictionary.giveWord()
        self.wordlen = len(self.word)

    def game(self):
        self.giveWordOnDifficulty()
        print(f"Dlugosc wylosowanego slowa to: {self.wordlen}")
        x = self.tries
        while self.tries > 0:
            user_word = input("Podaj slowo: ").lower()
            if self.validator.validUserWord(user_word, self.wordlen):
                if self.validator.validIfWon(user_word, self.word):
                    print("Gratulacje udalo ci sie odgadnac slowo!Czy chcesz zapisac swoj wynik?")
                    while True:
                        user = input("Wybierz[tak/nie]: ")
                        if user == "tak":
                            file = open("Data/highscores.txt", "a")
                            nick = input("Podaj swoj nick: ")
                            file.write(f"Nick: \t{nick} | WordLenght: \t{self.wordlen} | TriesStart/Triesleft: \t{self.tries}/{x}\n")
                            break
                        elif user == "nie":
                            break
                        else:
                            print("Podaj 'tak' lub 'nie'")
                    break
                else:
                    print("To nie jest to slowo!")
                    self.tries -= 1
                    i = 0
                    for char in user_word:
                        if char == self.word[i]:
                            self.stats.addBulls()
                        elif self.word.__contains__(char):
                            self.stats.addCows()
                        i += 1
                    self.stats.printStats()
                    self.stats.delStats()
            if self.tries == 0:
                print("Skonczyly ci sie proby wiec przegrales!")
