class Validator:
    def validUserWord(self, user, wordlen):
        if len(user) == wordlen:
            for char in user:
                if user.count(char) > 1:
                    print("Uzyte slowo nie jest izogramem!")
                    return False
            return True
        else:
            print("Uzyte slowo nie ma tyle liter co wylosowane slowo!")
            return False

    def validIfWon(self, user, word):
        if user == word:
            return True
        else:
            return False


