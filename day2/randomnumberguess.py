import random
rannum = random.randint(0,101)
print("Guess the randon number")

#print(rannum)
def rangegiver(x):
    range = ""
    if (x <= 20 and x >= 0):
        range = "0 to 20"
    elif (x <= 40 and x >=21):
        range = "21 to 40"
    elif (x <= 60 and x >=41):
        range = "41 to 60"
    elif (x <= 80 and x >=61):
        range = "61 to 80"
    elif (x <= 100 and x >=81):
        range = "81 to 100"
    return range

def rangegivermore(x):
    if (x <= 10 and x>=0):
        range = "0 to 10"
    elif (x <= 20 and x >=11):
        range = "11 to 20"
    elif (x <= 30 and x >=21):
        range = "21 to 30"
    elif (x <= 40 and x >=31):
        range = "31 to 40"
    elif (x <= 50 and x >=41):
        range = "41 to 50"
    elif (x <= 60 and x >=51):
        range = "51 to 60"
    elif (x <= 70 and x >=61):
        range = "61 to 70"
    elif (x <= 80 and x >=71):
        range = "71 to 80"
    elif (x <= 90 and x >=81):
        range = "81 to 90"
    elif (x <= 100 and x >=91):
        range = "91 to 100"
    return range
    

life = 3
temp = life
print("You will get 3 chances !")
for x in range(life):
    guess = int(input("Enter Your guess: "))
    if(guess == rannum):
        print("You are right")
        break
    else:
        temp -=1
        if(temp >0):
            print("sorry You are wrong but still you got :"+str(temp))
            if(temp == 2):   
                print("the number lies between "+str(rangegiver(rannum)))
            else:
                print("the number lies between "+str(rangegivermore(rannum)))
        else:
            print("sorry you lose \n the right number was "+str(rannum))



        

