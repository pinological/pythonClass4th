import random
rannum = random.randint(0,101)
print("Guess the randon number")

#print(rannum)

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
        else:
            print("sorry you lose")


