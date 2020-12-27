print("Factorial")

num = int(input("Enter a number :"))
anonum = 1
for i in range(1,num+1):
    anonum = anonum * i
    
print("The factorial of "+str(num)+" is "+str(anonum))