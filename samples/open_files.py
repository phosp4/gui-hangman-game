termsO = open("../terms.txt","r")
descrO = open("../definitions.txt","r")
cluesO = open("../clues.txt","r")

termsR = termsO.readlines()
descrR = descrO.readlines()
cluesR = cluesO.readlines()

termsL = []
descrL = []
cluesL = []

for i in range(len(termsR)):
    #t = termsR[i]
    #d = descrR[i]
    #c = cluesR[i]
    termsL.append((termsR[i])[0:-1])
    descrL.append((descrR[i])[0:-1])
    cluesL.append((cluesR[i])[0:-1])
    

print(termsL)
print(descrL)
print(cluesL)

termsO.close()
descrO.close()
cluesO.close()