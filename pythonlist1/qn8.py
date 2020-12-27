import array
number = input("Enter the number :")
temp = number[::-1]
if(number == temp):
    print("The number "+number+" is a palindrome")
else:
    print("The number "+number+" is not a palindrome")
