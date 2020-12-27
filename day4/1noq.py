# WAP to take a input from user and check the value is divisible of 4 and 7.

print("num divisible by 4 and 7 ")
num = int(input("Enter number :"))
if(num%4 == 0 and num%7 == 0):
    print("yes the number "+str(num)+" is divisible by 4 and 7")
else:
    print("No the number "+str(num)+" is no divisible by 4 and 7")