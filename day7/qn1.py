def max(num1,num2):
    if(num1 > num2):
        result = num1
    else:
        result = num2
    return result

def main():
    num1 = int(input("enter number :"))
    num2 = int(input("enter number :"))
    bigger = max(num1,num2)
    print("The biggest number between "+str(num1)+" and "+str(num2)+" is "+str(bigger))
main()