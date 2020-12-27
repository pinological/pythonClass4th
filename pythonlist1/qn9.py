num = int(input("Enter range : "))
for x in range(1,num+1):
    temp=str(x)
    temp2 = temp[::-1]
    if(temp == temp2):
        print(x)
