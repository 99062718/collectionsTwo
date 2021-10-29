import random

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
                totaalKaarten[kleur].append(random.randint(0, 9))
        else:
            for x in range(4): #fills up special key inside totaalKaarten dict. The reason this is seperate from the other colors inside the dict is because this one has its own unique cards and amount
                totaalKaarten[kleur].append("plus 4")
                totaalKaarten[kleur].append("choice")

def emptyStackCheck(): #checks of the stack cards need to be grabbed from is empty. If it is it gets refreshed
    totaal = len(totaalKaarten["blue"]) + len(totaalKaarten["green"]) + len(totaalKaarten["red"]) + len(totaalKaarten["yellow"]) + len(totaalKaarten["special"])
    if totaal == 0:
        refreshCards()

def getCard(naam): #gives player a card
    global playerKaarten
    global totaalKaarten
    while 1 == 1:
        emptyStackCheck()
        kleur = kleuren[random.randint(0, len(kleuren) - 1)]
        if len(totaalKaarten[kleur]) == 0:
            continue
        number = random.randint(0, len(totaalKaarten[kleur]) - 1)
        playerKaarten[naam][kleur].append(totaalKaarten[kleur][number])
        del totaalKaarten[kleur][number]
        break

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
        endNumber = len(playerKaarten) - 1 if reverse == False else -1
        for number in range(startNumber, endNumber, increment):
            naam = players[number]
            naamNext = players[number - increment]

            card = [max(playerKaarten[naam])]
            if card[0] == "special":
                card.append(playerKaarten[naam]["special"][random.rantint(0, len(playerKaarten[naam]["special"]))])
                playerKaarten[naam]["special"].remove(card[1])
                if card[1] == "plus 4":
                    for x in range(4):
                        getCard(naamNext)
                elif card[1] == "choice":
                    pastCard = [max(playerKaarten[naam]), None] if max(playerKaarten[naam]) != "special" else [kleuren[random.randint(0,3)], None]
            else: #continue working here
                card.append
                if pastCard[0] == "special" or pastCard[0] == card[0]:                   
                    if card[1] == "plus 2":
                        for x in range(2):
                            getCard(naamNext)
                    elif card[1] == "skip":
                        number += increment
                        number = startNumber if number == -1 or number == len(playerKaarten) else number
                    elif card[1] == "reverse":
                        reverse = True if reverse == False else False
                        increment = 1 if reverse == False else -1
                        endNumber = len(playerKaarten) - 1 if reverse == False else -1
