class classes():

    number = None
    prof = None
    peoples = None

    def __init__(self, number, prof, peoples):
        self.number = number
        self.peoples = peoples
        self.prof = prof

    def getInfo(self):
        print(f"Name: {self.number}{self.prof} | peoples: {self.peoples}")