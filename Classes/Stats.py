class Stats:
    def __init__(self):
        self.cows = 0
        self.bulls = 0

    def getCows(self):
        return self.cows

    def getBulls(self):
        return self.bulls

    def addCows(self):
        self.cows += 1

    def addBulls(self):
        self.bulls += 1

    def delStats(self):
        self.cows = 0
        self.bulls = 0

    def printStats(self):
        print(f"Cows: {self.cows} Bulls: {self.bulls}")
