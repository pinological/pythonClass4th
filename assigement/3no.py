# Write a Python program to guess a number between 1 to 9.
# [ Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears
# again until the guess is correct, on successful guess, user will get a "Well guessed!" message,
# and the program will exit.]
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
        mainnum = int(input("Try again :"))
        flag = True

