import random

choice = "ja"
namen = []
namen2 = []

while choice != "nee":
    try:
        naam = input("Vul hier een unieke naam in:\n").lower()
        isNaamInList = []
        if len(namen) == 0:
            namen.append(naam)
            namen2.append(naam)    
            triggerError() #this is not a real function. It exists purely to trigger an error
        else:
            for x in namen:
                if naam != x:
                    isNaamInList.append("nee")
                else:
                    isNaamInList.append("ja")
        
        for x in isNaamInList:
            if x == "ja":
                print("Deze naam zit al in de lijst!")
                triggerError() #this is not a real function. It exists purely to trigger an error
        
        namen.append(naam)
        namen2.append(naam)

        if len(namen) > 2:
            choice = input("Wilt u nog een naam invullen (ja/nee)?\n").lower()
    except:
        pass

while len(namen) > 0:
    naam1 = namen[random.randint(0, len(namen) - 1)]
    naam2 = namen2[random.randint(0, len(namen2) - 1)]

    if naam1 == naam2:
        if len(namen) == 1:
            print(naam1 + " is alleen :(")
    else:
        print(naam1 + " heeft " + naam2 + " als lootje!")
        namen.remove(naam1)
        namen2.remove(naam2)