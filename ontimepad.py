import random
num,alf = [None]*26,[None]*26
for i in range(26):
    num[i] = i
    alf[i] = chr(i+65)

maintext = input("Enter Word :")
finalword = ""
for x in maintext:
    if(x.islower()):
      finalword = finalword + x.upper()

print(finalword)

counter = 0
for x in maintext:
    counter+=1

forkey = ""
for i in range(counter):
    forkey = forkey+chr(random.randint(65,91))

print(forkey)

