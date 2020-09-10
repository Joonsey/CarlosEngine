import random
class story:
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
        "location":["oslo", "spain", "london", "narnia", "azeroth", "pandora", "mars", "the moon"],
        "sideCharacter":["none","cat", "dog", "golem", "large rat"]
        }
        
        self.storytheme = ["".join(randomchoice(self.StoryDict, "mainMotive")),
        "".join(randomchoice(self.StoryDict, "location")),
        "".join(randomchoice(self.StoryDict, "sideCharacter"))
        #", ".join(randomchoice(self.StoryDict, "4th category"))
        ]
        s = open("Storydictionairy.txt","w")
        s.write(self.StoryDict)
        s.close()
        print(self.storytheme)
        
    def storyTheme(self):
        return self.storytheme
s = story()
s.embedStory()
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