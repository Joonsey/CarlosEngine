import random
from character import character
from dice import dice
from story import story, story_loop
story_dict = ["cave", "magic", "flying", "pirate", "undead"]


protagonist = character(name="Loba", age=17, gender="female")
antagonist = character(name="Chloe", age=22, gender="female")
antagonist.makeHostile()

def main():
    print(f"""{protagonist.name} woke up to a loud noice not too far in the distance. {protagonist.pronoun()} got up in a hurry anxiously looking for something to defend her self with,
but before she could reach anything something banged on the door
What does loba do?
1. Open the door.
2. Ignore it and keep looking for something to defend herself with.
3. Try and find a place to hide.
    """)
    story_loop(DoorOpen, IgnoreAndLook, TryHide)

def DoorOpen():
    print(f"""{protagonist.pronoun()} rushed towards the door and opened it swiftly, she looked up and out but no one was there.
has she simply halucinated everything?""")

def TryHide():
    print(f"""{protagonist.name} runs towards her bedroom to hide, where does she decide to hide?
1. The closet, no one will ever look in a closet!
2. The minifridge!
3. Under the blanket in the bed.""")
    story_loop(HidingCloset, HidingCloset, HidingCloset)

def IgnoreAndLook():
    print(f"""{protagonist.name} keeps looking for a respectable item to defend her next move. She fails to do so, and uses a frying pan instead.""")
    protagonist.inventory.append("frying pan")

def HidingCloset():
    n = protagonist.statCheck("constitution", 4)
    print(f"{protagonist.pronoun()} decides to run to the closet and attempt to hide!" + "\n" + "---[Constitution check!]---")
    print("---[Success!]---" if n else "---[Failed!]---")
    print(f"{protagonist.pronoun()} reaches the closet successfull and is filled with contentment" if n else f"{protagonist.name} falls to the floor and fucking dies.")
main()