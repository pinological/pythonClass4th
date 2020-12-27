import random
total = 0
numList = [None]*7
for i in range(len(numList)):
    numList[i] = random.randint(1,10)
    total = total+numList[i]
mean = total/len(numList)
print("list of number : "+str(numList))
#
print("The mean : {:.2f}".format(mean))
print("The number geater then mean value are :")
for i in numList:
    if(i > mean):
        print(i,end=", ")
        


