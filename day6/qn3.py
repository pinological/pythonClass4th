import random
num1 = 0
randomlist = [None]*5
for i in range(5):
    randomlist[i] = random.randint(1,100)

num = int(input("Enter a number :"))
for i in randomlist:
    if(i > num):
        num1 = num1 + 1
        print("This are the number grater then "+str(num)+" :"+ str(i))

print("There are "+str(num1)+" greater then "+str(num))
