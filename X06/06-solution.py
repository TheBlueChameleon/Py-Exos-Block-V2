import random

# ============================================================================ #

class Player :
    backpackLimit = 3                # may not be bigger than the number of items in game
    stepsToWin    = 4                      
    
    baseHealth       = 10
    baseStrength     =  5
    baseIntelligence =  5
    baseSpeed        =  5
    baseCharisma     =  5
    
    fluctuationHealth       = 5
    fluctuationStrength     = 2
    fluctuationIntelligence = 2
    fluctuationSpeed        = 2
    fluctuationCharisma     = 2
    
    # ........................................................................ #
    
    def __init__(self, name) :
        self.name = name
        self.steps = 0
        self.skipTurn = False
        
        self.health       = Player.baseHealth       + random.randint(-Player.baseHealth, +Player.baseHealth)
        self.strength     = Player.baseStrength     + random.randint(-Player.baseHealth, +Player.baseHealth)
        self.intelligence = Player.baseIntelligence + random.randint(-Player.baseHealth, +Player.baseHealth)
        self.speed        = Player.baseSpeed        + random.randint(-Player.baseHealth, +Player.baseHealth)
        self.charisma     = Player.baseCharisma     + random.randint(-Player.baseHealth, +Player.baseHealth)
        
        self.backpack = []
        
        self.lookup = {"strength"     : self.strength,
                       "intelligence" : self.intelligence,
                       "speed"        : self.speed,
                       "charisma"     : self.charisma
            }
        
    
    # ........................................................................ #
    
    def __str__ (self) :
        reVal = "PLAYER:\n"
        reVal += "\tname                : " + self.name                 + "\n"
        reVal += "\tsteps toward success: " + str(self.steps)           + "\n"
        reVal += "\thealth              : " + str(self.health)          + "\n"
        reVal += "\tstrenght            : " + str(self.strength)        + "\n"
        reVal += "\tintelligence        : " + str(self.intelligence)    + "\n"
        reVal += "\tspeed               : " + str(self.speed)           + "\n"
        reVal += "\tcharisma            : " + str(self.charisma)        + "\n"
        
        reVal += "\tin their backpack:\n"
        for item in self.backpack :
            reVal += "\t* " + str(item) + "\n"
        
        return reVal
    
    # ........................................................................ #
    
    def equipNewItiem(self) :
        # finds a random item that wasn't in the backpack before and puts it
        # in the backpack if there is still space left; asks which item to
        # discard, otherwise.
        
        while True :
            candidate = random.choice(items)
            if candidate in self.backpack : continue
            break
        
        print("you found:", candidate)
        
        # if item fits in backpack: pack it and be done.
        if len(self.backpack) < self.backpackLimit :
            self.backpack.append(candidate)
            print(candidate.name, "packed into your backpack")
        
        # otherwise: offer a choice what to discard
        else :
            while True :
                # users will always enter BS. Loop the discard choice until
                # a valid choice was made
                
                print("Your backpack is full! Which item do you want to discard?")
                for i, item in enumerate(self.backpack) :
                    print(i, item, sep=") ")
                print(i+1, candidate, sep=") ")
            
                slot = int(input("please enter the number of the item to discard: "))
                
                if slot in range(self.backpackLimit + 1) : break
                
                print("Invalid choice.")
            
            if slot == self.backpackLimit :
                print(candidate.name, "was not taken")
                
            else :
                print(candidate.name, "replaces", self.backpack[slot].name)
                self.backpack[slot] = candidate
    
    # ........................................................................ #
    
    def getDiceCount(self, category) :
        result = self.lookup[category]
        for item in self.backpack :
            if item.category == category :
                result += item.bonus
        
        return result
    
    # ........................................................................ #
    
    def performTest(self, test) :
        print(test.textDecision)
        print("You need...")
        print(f"   either (yes): {test.yesCategory} : {test.yesCost}")
        print(f"   or     (no) : {test.noCategory} : {test.noCost}")
        
        # ask user for a yes or no. Again, repeat until an understandable answer
        # was given
        
        while True :
            decision = input("yes or no? ").lstrip().rstrip().upper()
            # lstrip: remove leading white spaces and tabs
            # rstrip: remove trailing white spaces and tabs
            # upper: make all letters upper case
            
            if decision in ("YES", "NO") : break
        
            print("I don't understand. Please repeat your answer.")
            
        if decision == "YES" :
            self.performTask(test.yesText, test.yesCategory, test.yesCost)
        else :
            self.performTask(test.noText, test.noCategory, test.noCost)
    
    # ........................................................................ #
    
    def performTask(self, text, category, cost) :
        print(text)
        
        if category == "skip turn" :
            print("skip a turn!")
            self.skipTurn = True
            return
        
        print("your roll:")
        dice  = [random.randint(1, 6) for i in range( self.getDiceCount(category) )]
        total = sum(dice)
        print(dice, "for a total of", total)
        
        if total > cost :
            print("You made it!")
            self.equipNewItiem()
            self.steps += 1
        else :
            print("That didn't suffice. You loose health points.")
            self.health -= 1
    
    # ........................................................................ #
    
    def isAlive(self) :
        return self.health > 0
    
    def isWinner(self) :
        return self.steps >= self.stepsToWin
    
# ============================================================================ #

class Test :
    def __init__(self,
                 textDecision,
                 yesText, yesCategory, yesCost,
                 noText ,  noCategory, noCost) :
        
        self.textDecision = textDecision
        
        self.yesText     = yesText
        self.yesCategory = yesCategory
        self.yesCost     = yesCost
        
        self.noText     = noText
        self.noCategory = noCategory
        self.noCost     = noCost
        
    # ........................................................................ #
    
    def __str__ (self) :
        # this is a very compact way of showing all attributes in an instance
        # __dict__ is, well, a dict, that has all instance attributes as keys
        # and their respective values as values.
        
        result = ""
        for key, value in self.__dict__.items() :
            result += f"{key:10}: {value:30}\n"
        
        return result
    
# ============================================================================ #

class Item :
    def __init__ (self, name, category, bonus) :
        self.name     = name
        self.category = category
        self.bonus    = bonus
    
    # ........................................................................ #
    
    def __str__(self) :
        return self.name + " (" + self.category + f" {self.bonus:+2}" + ")"

# ============================================================================ #
# global variables

players = [Player(name) for name in ["Victoria", "Chris", "Simon"]]

items = [
    Item("Berret"                         , "charisma"    , 2),
    Item("Holy Hand Grenade of Antioch"   , "strength"    , 3),
    Item("Bullwhip"                       , "strength"    , 1),
    Item("Dune - The Desert Planet (book)", "intelligence", 3)
]

tests = [
    Test("The deep jungle suddenly ends on a cliff. In front of you, a chasm opens up and a deep gorge stands between you and the temple. There is a narrow and shaky suspension bridge over the gorge.\n"
         "Do you step on the bridge?",
         "Half way over the bridge, you hear the hissing sound of ropes disintegrating: one of the ropes holding the bridge is about to snap!\nRun for your life!", "speed", 16,
         "You try to find another way across the gorge, which takes a lot of time.\nSkip one turn.", "skip turn", 0
         ),
    Test("A tribe of natives discovered you on their sacred cerimonial grounds.\n"
         "Do you try to appease them (yes) or run away (no)?",
         "The natives appear to be rather upset by your sacrilege. Can your charisma win them over?", "charisma", 25,
         "Run for your life!", "speed", 10),
    Test("An avalanche of pebbles has gone down, and now a boulder blocks your way. Will you try to thrust away the boulder (yes) or can you think of something more sophisticated (no)?",
         "You roll up the sleeves of your shirt and push against the boulder. Are you strong enough?", "strength", 20,
         "You try to remember all the episodes of MacGyver you've ever seen. Can you remember a good trick?", "intelligence", 20)
]

# ============================================================================ #
# Debug / Tests

print("ITEMS IN GAME:")
for item in items :
    print("*", item)
print()

print("TESTS IN GAME:")
for test in tests :
    print(test)

print("PLAYERS IN GAME:")
for player in players :
    print(player)

# ============================================================================ #
# The game (you lost again) (me too)

gameActive = True
while gameActive :
    for player in players :
        
        # skip players who are already deceased
        if not player.isAlive() : continue
        
        print("#", "=" * 78, "#")
        print(player)
        
        if player.skipTurn :
            player.skipTurn = False
            print(f"{player.name} skips a turn.")
            continue
        
        test = random.choice(tests)
        
        player.performTest(test)
        
        if player.isWinner() :
            print(player.name, "wins the game!")
            gameActive = False
            break
    
