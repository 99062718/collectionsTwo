import random

kleineLetter = "abcdefghijklmnopqrstuvwxyz"
groteLetter = kleineLetter.upper()
cijfers = "0123456789"
speciale = "@#$%&_?"
aantalGrote = random.randint(2, 6)
aantalCijfer = random.randint(4, 7)
characters = [[], [], [], []]
wachtwoord = ""

for x in range(0, 22 - (aantalCijfer + aantalGrote)):
    characters[0].append(kleineLetter[random.randint(0, len(kleineLetter) - 1)])

for x in range(0, 3):
    characters[1].append(speciale[random.randint(0, len(speciale) - 1)])

for x in range(0, aantalCijfer + 1):
    characters[2].append(cijfers[random.randint(0, len(cijfers) - 1)])

for x in range(0, aantalGrote + 1):
    characters[3].append(groteLetter[random.randint(0, len(groteLetter) - 1)])

def wachtwoordMaker():
    global wachtwoord
    global characters
    randomNum = random.randint(0, len(characters) - 1)
    if randomNum == 2 and len(wachtwoord) < 3 or randomNum == 1 and len(wachtwoord) == 0 or randomNum == 1 and len(wachtwoord) == 23:
        wachtwoordMaker()
    else:
        wachtwoord += characters[randomNum][0]
        del characters[randomNum][0]
        if len(characters[randomNum]) == 0:
            del characters[randomNum]

for x in range(24):
    wachtwoordMaker()

print(wachtwoord)