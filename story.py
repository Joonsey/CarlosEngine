import random
class story: # TODO VERY WORK IN PROGRESS MORE OR LESS IGNORE THIS STORY CLASS FOR NOW
    def __init__(self, *args):
        self.args = args
        self.storylist = []
    
        for n in self.args:
            if n in self.StoryDict:
                self.storylist.append(n)
            else:
                pass

    def showStory(self):
        print(self.storylist)
    

    def embedStory(self):
        def randomchoice(choices, ctx):
            return random.choice(choices.get(ctx))

        self.StoryDict = {
        "mainMotive":["neutral good", "neutral evil", "neutral neutral", "chaotic good", "chaotic evil", "chaotic neutral", "Lawfull good", "lawfull evil", "lawfull neutral"],
        "location":["oslo", "spain", "london", "narnia", "azeroth", "pandora", "mars", "the moon", "SCP"],
        "sideCharacter":["none","cat", "dog", "golem", "large rat", "SCP-529"]
        }
        
        self.storytheme = ["".join(randomchoice(self.StoryDict, "mainMotive")),
        "".join(randomchoice(self.StoryDict, "location")),
        "".join(randomchoice(self.StoryDict, "sideCharacter"))
        #", ".join(randomchoice(self.StoryDict, "4th category"))
        ]
        print(self.storytheme)
        
    def storyTheme(self):
        return self.storytheme

class story_loop: # this basically functions as the main component in the game.
    # where it will run one of 3 functions in the game based on input.
    # TODO add ability to check inventory at any given time and maybe a rare or custom option? 
    # TODO also add the ability to see stats
    def __init__(self, outcome1, o2, o3):
        self.ANSWER_A = ["1","A","a"]
        self.ANSWER_B = ["b","2","B"]
        self.ANSWER_C = ["C","c","3"]
        self.INVENTORYKEY = ["i","inv","inventory","items"]
        self.FirstOutcome = outcome1
        self.SecondOutcome = o2
        self.ThirdOutcome = o3
        self.run()
    
    def run(self):
        n = input(">>>").lower()
        if n in self.ANSWER_A:
            self.FirstOutcome()
        elif n in self.ANSWER_B:
            self.SecondOutcome()
        elif n in self.ANSWER_C:
            self.ThirdOutcome()
        elif n in self.INVENTORYKEY:
            # protagonist.showInventory()
            pass
        else:
            print("please enter valid input, A, B or C")
            self.run()

if __name__ == "__main__":
    s = story()
    s.embedStory()