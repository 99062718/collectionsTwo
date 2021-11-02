import random
import time

players = []
playerKaarten = {}
playerPunten = {}

kleuren = ["green", "yellow", "red", "blue", "special"]
totaalKaarten = {
    "green": [],
    "yellow": [],
    "red": [],
    "blue": [],
    "special": []
}

def refreshCards(): #once cards have run out we can call this function to refresh the stack
    global totaalKaarten
    for kleur in kleuren:
        totaalKaarten[kleur] = []
    for kleur in kleuren: #fills up all colors inside totaalKaarten dict
        if kleur != "special":
            for x in range(2):
                totaalKaarten[kleur].append("skip")
                totaalKaarten[kleur].append("turn")
                totaalKaarten[kleur].append("plus 2")
            for x in range(19):
                totaalKaarten[kleur].append(str(random.randint(0, 9)))
        else:
            for x in range(4): #fills up special key inside totaalKaarten dict. The reason this is seperate from the other colors inside the dict is because this one has its own unique cards and amount
                totaalKaarten[kleur].append("plus 4")
                totaalKaarten[kleur].append("choice")

def emptyStackCheck(): #checks of the stack cards need to be grabbed from is empty. If it is it gets refreshed
    if len(totaalKaarten["blue"]) + len(totaalKaarten["green"]) + len(totaalKaarten["red"]) + len(totaalKaarten["yellow"]) + len(totaalKaarten["special"]) == 0:
        refreshCards()

def getCard(naam): #gives player a card
    global playerKaarten
    global totaalKaarten
    while 1 == 1:
        emptyStackCheck()
        kleur = kleuren[random.randint(0, len(kleuren) - 1)]
        if len(totaalKaarten[kleur]) == 0:
            continue
        numberLocal = random.randint(0, len(totaalKaarten[kleur]) - 1)
        playerKaarten[naam][kleur].append(totaalKaarten[kleur][numberLocal])
        del totaalKaarten[kleur][numberLocal]
        break

def cardFunctions(card):
    global startNumber
    global increment
    global endNumber
    global reverse
    global number
    if card == "plus 2":
        for x in range(2):
            getCard(naamNext)
        print("{} has to take 2 cards!".format(naamNext))
    elif card == "turn":
        reverse == True if reverse == False else False
        increment = 1 if reverse == False else -1
        startNumber = 0 if reverse == False else len(playerKaarten) - 1
        endNumber = len(playerKaarten) if reverse == False else -1
    elif card == "skip":
        number = number - increment if number - increment != -1 and number - increment != len(playerKaarten) else players[startNumber]

def findBiggest(naam):
    biggestColor = ["", 0]
    colors = list(playerKaarten[naam].keys())
    for numberLocal in range(0, 5):
        if len(playerKaarten[naam][colors[numberLocal]]) > biggestColor[1]:
            biggestColor[0] = colors[numberLocal]
            biggestColor[1] = len(playerKaarten[naam][colors[numberLocal]])
    return biggestColor[0]



aantalPlayers = int(input("Hoeveel spelers?\n")) #asks user for amount of players and their names
for player in range(1, aantalPlayers + 1):
    while 1 == 1:       
        naam = input("Hoe heet player " + str(player) + "\n").lower()
        if naam not in players:
            players.append(naam)
            playerKaarten[naam] = {}
            for kleur in kleuren:
                playerKaarten[naam][kleur] = []
            playerPunten[naam] = 0
            break
        print("U heeft deze naam al ingevoert!")

programEnd = "nee"
while programEnd != "ja":
    gameEnd = "nee"
    refreshCards()

    for naam in playerKaarten: #resets players cards at the start of each game
            for kleur in kleuren:
                playerKaarten[naam][kleur] = []

    for naam in playerKaarten: #gives all players 7 cards at the start of the game
            for number in range(8):
                getCard(naam)

    reverse = False
    pastCard = ["special", None]
    while gameEnd != "ja": #start of the game
        increment = 1 if reverse == False else -1
        startNumber = 0 if reverse == False else len(playerKaarten) - 1
        endNumber = len(playerKaarten) if reverse == False else -1
        for number in range(startNumber, endNumber, increment):
            print(playerKaarten)
            naam = players[number]
            naamNext = players[number - increment] if number - increment != -1 and number - increment != len(playerKaarten) else players[startNumber]
            currentCard = [findBiggest(naam)]
            if currentCard[0] == pastCard[0] or currentCard[0] == "special" or pastCard[0] == "special":
                if currentCard[0] == "special":
                    currentCard.append(playerKaarten[naam]["special"][0])
                    print("{} plays {}".format(naam, currentCard))

                    if currentCard[1] == "plus 4":
                        for x in range(4):
                            getCard(naamNext)
                        print("{} has to take 4 cards!".format(naamNext))

                    playerKaarten[naam]["special"].remove(playerKaarten[naam]["special"][0])   
                    pastCard = ["special", None] if currentCard[1] != "choice" else [findBiggest(naam), None]
                else:
                    pastCard = []
                    pastCard.append(currentCard[0])
                    pastCard.append(max(playerKaarten[naam][currentCard[0]]))
                    print("{} plays {}".format(naam, pastCard))
                    cardFunctions(pastCard[1])
                    playerKaarten[naam][currentCard[0]].remove(max(playerKaarten[naam][currentCard[0]]))
            else:
                if len(playerKaarten[naam][pastCard[0]]) > 0:
                    pastCard = [pastCard[0]]
                    pastCard.append(max(playerKaarten[naam][pastCard[0]]))
                    print("{} plays {}".format(naam, pastCard))
                    cardFunctions(pastCard[1])
                    playerKaarten[naam][currentCard[0]].remove(max(playerKaarten[naam][currentCard[0]]))
                else:
                    colorKey = []
                    for color in playerKaarten[naam]:
                        for card in color:
                            if card == pastCard[1]:
                                colorKey = list(playerKaarten[naam].keys())[list(playerKaarten[naam].values()).index(card)]
                                pastCard = [colorKey, card]
                                playerKaarten[naam][color].remove(card)
                                break
                        if colorKey != []:
                            break
                    if colorKey == []:
                        getCard(naam)
                        print("{} could not play anything and has to grab a card!".format(naam))

            if len(playerKaarten[naam]["blue"]) + len(playerKaarten[naam]["red"]) + len(playerKaarten[naam]["green"]) + len(playerKaarten[naam]["yellow"]) + len(playerKaarten[naam]["special"]) == 0:
                    print("{} has UNO!".format(naam))
                    gameEnd = "ja"
                    playerPunten[naam] += 100
                    break

            time.sleep(2)
    
    for number in range(0, len(playerPunten)):
        namen = list(playerPunten.keys())
        if playerPunten[namen[number]] >= 500:
            print("{} has won the game!".format(namen[number]))
            programEnd = "ja"
            break
                                
                        



            