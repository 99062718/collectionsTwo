import random

dobbelstenen = [0, 0, 0, 0, 0]
keuzes = ("aces", "twos", "threes", "fours", "fives", "sixes", "three of a kind", "four of a kind", "full house", "small straight", "large straight", "yahtzee", "chance")
possibleScores = {
    "full house": 25,
    "small straight": 30,
    "large straight": 40,
    "yahtzee": 50,
    "extra bonus": 35
}

def roll(stenen=[0,1,2,3,4]):
    global dobbelstenen
    for x in stenen:
        dobbelstenen[x] = random.randint(1, 6)

def reRoll():
    global dobbelstenen
    list = []
    opnieuw = input("Welke dobbelstenen wilt u opnieuw gooien (schrijf als '12345')?\n")
    for x in range(0, len(opnieuw)):
        list.append(int(opnieuw[x]) - 1)
    roll(list)

def straight(message, number, beurt):
    begin = int(input("Welke dobbelsteen begint de straight?\n"))
    oldDobbelsteen = 0
    lowestDobbelsteen = dobbelstenen[begin - 1]
    highestDobbelsteen = 0
    for x in range(0, len(dobbelstenen)):
        if oldDobbelsteen == 0:
            oldDobbelsteen = lowestDobbelsteen
            highestDobbelsteen = lowestDobbelsteen
        if dobbelstenen[x] - oldDobbelsteen == 1:
            highestDobbelsteen = dobbelstenen[x]
        oldDobbelsteen = dobbelstenen[x]
    if highestDobbelsteen - lowestDobbelsteen <= number:
        return
    else:
        print(message)
        keuze(beurt)

def keuze(beurt):
    global totaalTop
    global totaal
    global dobbelstenen
    while keuzes == keuzes:
        try:
            choice = input("Waar wilt u deze dobbelstenen in zetten?\n").lower()
            if "aces" == choice or "twos" == choice or "threes" == choice or "fours" == choice or "fives" == choice or "sixes" == choice:
                dictionary = {
                    "aces": 1,
                    "twos": 2,
                    "threes": 3,
                    "fours": 4,
                    "fives": 5,
                    "sixes": 6
                }
                currentKeuzes[beurt].remove(choice)
                for x in range(0, len(dobbelstenen)):
                    if dictionary[choice] == dobbelstenen[x]:
                        totaalTop[beurt] += dobbelstenen[x]
                return
            elif "three of a kind" == choice or "four of a kind" == choice or "chance" == choice:
                currentKeuzes[beurt].remove(choice)
                for x in range(0, len(dobbelstenen)):
                    totaal[beurt] += dobbelstenen[x]
                return
            elif "small straight" == choice:
                straight("Dit is geen small straight!", 3, beurt)
                currentKeuzes[beurt].remove(choice)
                totaal[beurt] += possibleScores["small straight"]
                return
            elif "large straight" == choice:
                straight("Dit is geen large straight!", 2, beurt)
                currentKeuzes[beurt].remove(choice)
                totaal[beurt] += possibleScores["large straight"]
                return
            elif "full house" == choice:
                num1 = 0
                num2 = 0
                numberTotals = [0, 0]
                for x in dobbelstenen:
                    if num1 == 0:
                        num1 = x
                        numberTotals[0] = 1
                    elif num2 == 0 and x != num1:
                        num2 = x
                        numberTotals[1] = 1
                    elif num1 == x:
                        numberTotals[0] += 1
                    elif num2 == x:
                        numberTotals[1] += 1
                    else:
                        print("Dit is geen full house!")
                        keuze(beurt)
                if numberTotals[0] == 2 and numberTotals[1] == 3 or numberTotals[0] == 3 and numberTotals[1] == 2:
                    currentKeuzes[beurt].remove(choice)
                    totaal[beurt] += possibleScores["full house"]
                    return
                else:
                    print("Dit is geen full house!")
                    keuze(beurt)
            elif "yahtzee" == choice:
                num = dobbelstenen[0]
                for x in dobbelstenen:
                    if num != x:
                        print("Dit is geen yahtzee!")
                        keuze(beurt)
                currentKeuzes[beurt].remove(choice)
                totaal[beurt] += possibleScores["yahtzee"]
                return
            elif "no possible" == choice:
                return
            else:
                triggerException() #this is not a real function i just wanted to create an error here
        except:
            print("Dit is geen geldige optie!")
            keuze(beurt)

def beurt(beurt):
    roll()
    print("Uw dobbelstenen zijn: " + str(dobbelstenen))
    choice = "y"
    retries = 0
    while choice != "n" and retries < 3:  
        choice = input("Wilt u overnieuw gooien? (y/n)\n").lower()
        if choice == "y":
            retries += 1
            reRoll()
            print("Uw dobbelstenen zijn: " + str(dobbelstenen))
    keuze(beurt)

def tussenstand(message):
    tussenstand = []
    for y in range(0, len(totaal)):
        tussenstandTop = totaalTop[y] if totaalTop[y] < 63 else totaalTop[y] + 35
        tussenstand = totaal[y] + totaalTop[y]
    print(message + str(tussenstand))

aantalPlayers = int(input("Met hoeveel spelers wilt u het spel spelen?\n"))
game = 0
while keuzes == keuzes:
    game += 1
    print("Game ", game)
    gameEnd = "nee"
    currentKeuzes = []
    totaalTop = []
    totaal = []
    for x in range(0, aantalPlayers):
        currentKeuzes.append([])
        totaalTop.append(0)
        totaal.append(0)
        for y in range(0, len(keuzes)):
            currentKeuzes[x].append(keuzes[y])
    
    while gameEnd == "nee":
        for x in range(0, len(currentKeuzes)):
            print("beurt ", str(x + 1))
            beurt(x)

            if len(currentKeuzes[x]) == 0:
                gameEnd = "ja"
                tussenstand("En de uitslag is....: ")

        tussenstand("De tussenstand is: ")
    
    choice = input("Wilt u nog een keer spelen (y/n)").lower()
    if choice == "n":
        exit()