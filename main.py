import random
from character import character
story_dict = ["cave", "magic", "flying", "pirate", "undead"]

class story_loop:
    def __init__(self, outcome1, o2, o3):
        self.ANSWER_A = ["1","A","a"]
        self.ANSWER_B = ["b","2","B"]
        self.ANSWER_C = ["C","c","3"]
        self.FirstOutcome = outcome1
        self.SecondOutcome = o2
        self.ThirdOutcome = o3
        self.run()
    
    def run(self):
        n = input(">>>")
        if n in self.ANSWER_A:
            self.FirstOutcome()
        elif n in self.ANSWER_B:
            self.SecondOutcome()
        elif n in self.ANSWER_C:
            self.ThirdOutcome()
        else:
            print("please enter valid input, A, B or C")
            self.run()

protagonist = character(name="Loba", age=17, gender="female")
def main():
    print(f"""{protagonist.name} woke up to a loud noice not too far in the distance. {protagonist.pronoun()} got up in a hurry anxiously looking for something to defend her self with,
     but before she could reach anything something banged on the door
     What does loba do?
     1. Open the door.
     2. Ignore it and keep looking for something to defend herself with.
     3. Try and find a place to hide.
    """)
    story_loop(DoorOpen, TryHide, IgnoreAndLook)

def DoorOpen():
    print(f"""{protagonist.pronoun()} rushed towards the door and opened it swiftly, she looked up and out but no one was there.
    has she simply halucinated everything?""")

def TryHide():
    print(f"""{protagonist.name} runs towards her bedroom to hide, where does she decide to hide?
    1. The closet, no one will ever look in a closet!
    2. The minifridge!
    3. Under the blanket in the bed.""")

def IgnoreAndLook():
    print(f"""{protagonist.name} keeps looking for a respectable item to defend her next move. She fails to do so, and uses a frying pan instead.""")

main()