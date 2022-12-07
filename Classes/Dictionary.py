import random


class Dictionary:
    def __init__(self):
        file = open("Data/dictionary.txt")
        text = ""
        for line in file:
            line = line.lower()
            text += line
        self.array = list(text.split())

    def giveWord(self):
        return random.choice(self.array)

