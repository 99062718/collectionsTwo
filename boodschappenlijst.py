boodschappenlijst = {}
antwoord = "ja"

while antwoord == "ja":
    boodschap = input("Wat voor boodschap wilt u halen?\n")
    hoeveelheid = int(input("Hoeveel wilt u hiervan halen?\n"))
    try:
        if boodschappenlijst[boodschap] >= 0:
            boodschappenlijst[boodschap] += hoeveelheid
    except:
        boodschappenlijst[boodschap] = hoeveelheid
    antwoord = input("Wilt u nog een boodschap doen (ja of nee)?\n").lower()

print(boodschappenlijst)