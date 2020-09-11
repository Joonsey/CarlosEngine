import random
class dice: # basic dice that rolls a defined amount of times and gives a random output between 0 and defined amount
    def __init__(self, x):
        self.x = x

    def roll(self):
        self.x = random.randint(0,self.x)
        return self.x

if __name__ == "__main__":
    pass