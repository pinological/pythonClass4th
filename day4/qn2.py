# to take a input value from user and check the value is odd or even if even then add the 5 multiple until its sum being 100.
num = float(input("Enter number : "))
if(num%2 == 0):
    print("number even")
else:
    num = num + 5*1
    if(num >= 100):
        print(str(num) + " is greater or equals to 100")
    else:
        num = num + 5*2
        if(num >= 100):
             print(str(num) + " is greater or equals to 100")
        else:
            num = num + 5*3
            if(num >= 100):
                print(str(num) + " is greater or equals to 100")
            else:
                num = num + 5*4
                if(num >= 100):
                    print(str(num) + " is greater or equals to 100")
                else:
                    num = num + 5*5
                    if(num >= 100):
                        print()



           

