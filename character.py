import random
INVENTORY_PATH = "inventory"
STATWEIGHT = 12
class character: 
    def __init__(self, name="undefined", age="undefined", gender="undefined", race="undefined"):
        self.name = name
        self.age = age
        self.gender = gender
        self.race = race
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.wisdom = 0
        self.charisma = 0
        self.hp = 100
        self.hastats = False
        self.inventory = []
        self.isFriendly = True
        self.pron = self.pronoun()
        self.generateStats()

    def pronoun(self):
        if self.gender.lower() == "male":
            return "he"
        elif self.gender.lower() == "female":
            return "she"
        else: 
            return "it"

    def generateStats(self): 
        self.strength = random.randint(0,STATWEIGHT)
        self.constitution = random.randint(0,STATWEIGHT)
        self.dexterity = random.randint(0,STATWEIGHT)
        self.wisdom = random.randint(0,STATWEIGHT)
        self.charisma = random.randint(0,STATWEIGHT)
        self.HasStats = True
    
    def showStats(self):
        if self.HasStats:
            print("Your strength is: " + str(self.strength))
            print("Your dexterity is: " + str(self.dexterity))
            print("Your constitution is: " + str(self.constitution)) 
            print("Your wisdom is: " + str(self.wisdom)) 
            print("Your charisma is: " + str(self.charisma)) 
        else:
            print("You have no valid stats, please generate stats")


    def showInventory(self): 
        print(f"You currently have: {self.inventory}")

    def removeItem(self, item):
        if item in self.inventory:
            f = open(INVENTORY_PATH, "w")
            f.remove(item)
            f.close()
            self.inventory.remove(item)
        else:
            print("You don't currently have that item!")

    def statCheck(self, stat, weight): 
        stat = stat.lower()
        if stat == "strength":
            if weight >= self.strength:
                return False
            else: return True
        
        elif stat == "dexterity":
            if weight >= self.dexterity:
                return False
            else: return True
        
        elif stat == "constitution":
            if weight >= self.constitution:
                return False
            else: return True
        
        elif stat == "wisdom":
            if weight >= self.wisdom:
                return False
            else: return True
        
        elif stat == "charisma":
            if weight >= self.charisma:
                return False
            else: return True
        
        else: print("invalid input. Please input a proper stat (Strength, Wisdom, Dexterity, Constitution or charisma).")
        
    def makeHostile(self):
        self.isFriendly = False

    def isItFriendly(self):
        return self.isFriendly

    def expandInv(self, args):
        if len(self.inventory) == 0:
            f = open(INVENTORY_PATH, "w")
            args.split(" ")
            f.write(args+", ")
            f.close
            self.inventory.append(args)
        else:
            f = open(INVENTORY_PATH, "a")
            f.write(args)
            f.close
            self.inventory.append(args)


