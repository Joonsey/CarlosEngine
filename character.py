import random
INVENTORY_PATH = "inventory"
STATWEIGHT = 12
class character: 
    # initiates a character with name, age, gender, and race. None of which needs to be specified
    def __init__(self, name="undefined", age="undefined", gender="undefined", race="undefined"):
        # also has alot more stats and properties than can be called at any time
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
    
    def __str__(self):
        return f"{self.name} is {self.age} years old, and a {self.race}"

    def pronoun(self):
        # This function  calls the apriopriate name pronoun for the character. Use self.noun to call this function
        if self.gender.lower() == "male" or "m":
            return "he"
        elif self.gender.lower() == "female" or "f":
            return "she"
        else: 
            return "it"


    def generateStats(self): 
        # generates stats for the character, this gets called when character is made
        self.strength = random.randint(0,STATWEIGHT)
        self.constitution = random.randint(0,STATWEIGHT)
        self.dexterity = random.randint(0,STATWEIGHT)
        self.wisdom = random.randint(0,STATWEIGHT)
        self.charisma = random.randint(0,STATWEIGHT)
        self.HasStats = True
    
    def showStats(self):
        # call this function to print stats
        # TODO: make this being called by a command / input
        if self.HasStats:
            print("Your strength is: " + str(self.strength))
            print("Your dexterity is: " + str(self.dexterity))
            print("Your constitution is: " + str(self.constitution)) 
            print("Your wisdom is: " + str(self.wisdom)) 
            print("Your charisma is: " + str(self.charisma)) 
        else:
            print("You have no valid stats, please generate stats")


    def showInventory(self): 
        # prints your current inventory
        print(f"You currently have: {self.inventory}")

    def removeItem(self, item):
        # removed selected item from inventory, both the file and the list.
        if item in self.inventory:
            f = open(INVENTORY_PATH, "w")
            f.remove(item)
            f.close()
            self.inventory.remove(item)
        else:
            print("You don't currently have that item!")

    def statCheck(self, stat, weight): 
        # check selected stat for for current character and matches it against the weight attribute
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
        
    def makeHostile(self): # defines that the enemy is hostile
        self.isFriendly = False

    def isItFriendly(self): # return if enemy is friendly
        return self.isFriendly

    def expandInv(self, args): # expands the inventory by adding selected item to the character.
        # if you have no items in your inventory instead of adding item it will recreate and rewrite the file.
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


