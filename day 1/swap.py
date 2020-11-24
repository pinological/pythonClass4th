num1 = int(input("Enter Number :"))
num2 = int(input("Enter Another Number :"))
print("before swap")
print(num1,num2)
num1 += num2
num2 = num1 - num2
num1 = num1 - num2
print("After swap")
print(num1,num2)