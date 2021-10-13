import random

choice = "ja"
namen = []
namen2 = []

while choice != "nee":
    naam = input("Vul hier een unieke naam in:\n").lower()
    if naam not in namen:
        namen.append(naam)
        namen2.append(naam)
    else:
        print("Deze naam heeft u al gebruikt!")

    if len(namen) > 2:
        choice = input("Wilt u nog een naam invullen (ja/nee)?\n").lower()

while namen:
    naam1 = namen[random.randint(0, len(namen) - 1)]
    naam2 = namen2[random.randint(0, len(namen2) - 1)]

    if naam1 == naam2:
        if len(namen) == 1:
            print(naam1 + " is alleen :(")
            exit()
    else:
        print(naam1 + " heeft " + naam2 + " als lootje!")
        namen.remove(naam1)
        namen2.remove(naam2)