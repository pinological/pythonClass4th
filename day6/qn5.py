import random
dupcounter = 0
numlist = [None]*7
while(dupcounter != 7):
    dupcounter = 0
    for i in range(len(numlist)):
        numlist[i] = random.randint(0,20)
        # print(numlist[i])

    for i in range(len(numlist)):
        for y in range(len(numlist)):
            if(numlist[i] == numlist[y]):
                # print(str(numlist[i])+" : "+str(numlist[y]))
                dupcounter = dupcounter+1
                # print(dupcounter)
print(numlist)



