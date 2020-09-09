import random
class dice:
    def __init__(self, x):
        self.x = x

    def roll(self):
        self.x = random.randint(0,self.x)
        return self.x