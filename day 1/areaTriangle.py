#3.Python Program to Calculate the Area of a Triangle

#[Area of a triangle = (s*(s-a)*(s-b)*(s-c))-1/2]
import math
print("Enter 3 Side")
a = float(input("Enter Side :"))
b = float(input("Enter Side :"))
c = float(input("Enter Side :"))
s = (a+b+c)/2
print(s)
total = math.sqrt((s*(s-a)*(s-b)*(s-c)))
print(s*(s-a)*(s-b)*(s-c))
print("area of triangle is %0.2f" %total)

