import random
print("Gussing Game")
rannum = random.randint(1,9)
mainnum = int(input("Guess number between 1 - 9 :"))
flag = True
while flag == True:
    if mainnum == rannum:
        print("Well guess the number was "+str(rannum))
        break
    else:
        rannum = int(input("Try again :"))
        flag = True
