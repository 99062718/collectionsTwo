import random
kleuren = [["harten", "klaveren", "schoppen", "ruiten" , "joker"], ["2", "3", "4", "5", "6", "7", "8", "9", "10", "boer", "vrouw", "heer", "aas"]]
kaarten = []
jokerNum = 0
for x in range(54):
    part1 = kleuren[0][random.randint(0, len(kleuren[0]) - 1)]
    if part1 == "joker":
        jokerNum += 1
        kaarten.append(part1)
        if jokerNum == 2:
            del kleuren[0][4]
    else:
        kaarten.append(part1 + " " + kleuren[1][random.randint(0, len(kleuren[1]) - 1)])
for x in range(1, 8):
    print("kaart " + str(x) + ": " + kaarten[0])
    del kaarten[0]
print("deck (" + str(len(kaarten)) + " kaarten): " + str(kaarten))