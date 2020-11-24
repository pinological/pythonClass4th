# Python Program to Solve Quadratic Equation
#      [Quadratic Equation  ax**2 + bx + c = 0]
import math
a = float(input("Enter a:"))
b = float(input("Enter b:"))
c = float(input("Enter c:"))
r = b**2 - 4*a*c
print(r)
x1 = float((((-b) + math.sqrt(r))/(2*a)))     
x2 = float((((-b) - math.sqrt(r))/(2*a)))
print("2 roots: %0.2f and %0.2f" % (x1, x2))

