num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))
num3 = int(input("Enter number: "))

if(num1 >= num2 and num1 >= num3):
    print(str(num1)+" is the greatest of three")
elif(num2 >= num1 and num2 >= num3):
    print(str(num2)+" is the greatest of three")
else:
    print(str(num3)+ " the greatest of three")