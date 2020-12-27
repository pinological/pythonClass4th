import datetime
#login
today = datetime.datetime.now()
print("\t\t\t Inland Revenue Department")
print("\t\t    Welcome to Integrated Tax System")
userName = input("Enter your name :")
userAdd = input("Address : ")
usersta = input("Enter 'Y' for Married and 'N' for Unmarried : ")
userPan = int(input("Enter your PAN No :"))
userMoney = float(input("Enter your per month income [Rs] :"))
userMoney = userMoney*12


marY = 450000
marN = 400000
finaltaxMoney = 0
if(usersta == 'Y'):
    if(userMoney <= marY):
        tax = 1
        finaltaxMoney = finaltaxMoney + 4500
    elif(userMoney >= (marY+100000) and userMoney <= (marY+199999)):
        tax = 10
        extrataxmoney = userMoney - marY
        finaltaxMoney = ((tax*extrataxmoney)/100)
        finaltaxMoney = finaltaxMoney + 4500
    elif(userMoney >= (marY+200000) and userMoney <= ((marY+1299999))):
        tax = 20
        extrataxmoney = userMoney - marY
        finaltaxMoney = ((tax*extrataxmoney)/100)
        finaltaxMoney = finaltaxMoney + 4500
    elif(userMoney >= (marY+1300000) and userMoney <= (marY+199999)):
        tax = 30
        extrataxmoney = userMoney - marY
        finaltaxMoney = ((tax*extrataxmoney)/100)
        finaltaxMoney = finaltaxMoney + 4500
    elif(userMoney >= (marY+2000000)):
        tax = 36
        extrataxmoney = userMoney - marY
        finaltaxMoney = ((tax*extrataxmoney)/100)
        finaltaxMoney = finaltaxMoney + 4500
elif(usersta == 'N'):
    if(userMoney <= marN):
        tax = 1
        finaltaxMoney = finaltaxMoney + 4000
    elif(userMoney >= (marN+100000) and userMoney <= (marN+199999)):
        tax = 10
        extrataxmoney = userMoney - marN
        finaltaxMoney = ((tax*extrataxmoney)/100)
        finaltaxMoney = finaltaxMoney + 4000
    elif(userMoney >= (marN+200000) and userMoney <= (marN+1299999)):
        tax = 20
        extrataxmoney = userMoney - marN
        finaltaxMoney = ((tax*extrataxmoney)/100)
        finaltaxMoney = finaltaxMoney + 4000
    elif(userMoney >= (marN+1300000) and userMoney <= (marN+1999999)):
        tax = 30
        extrataxmoney = userMoney - marN
        finaltaxMoney = ((tax*extrataxmoney)/100)
        finaltaxMoney = finaltaxMoney + 4000
    elif(userMoney >= (marN+2000000)):
        tax = 36
        extrataxmoney = userMoney - marN
        finaltaxMoney = ((tax*extrataxmoney)/100)
        finaltaxMoney = finaltaxMoney + 4000
if(tax == 1):
    finaltax = "1"
else:
    finaltax = "1 + "+str(tax)
# print(tax)
# print(finaltaxMoney)
# print(extrataxmoney)
#output
print("\t\tLand Revenue Department")
print("\t\t Lazimpart, Kathmandu")
print("\t\t\tWelcome to")
print("\t\tIntegrated Tax System(ITS)")
print("Tax Payee : "+userName+"\t\t\t\t Address : "+userAdd)
print("PAN : "+str(userPan)+"\t\t FY: "+str(today.year)+"/"+str(int(today.year)+1)+"\t\tMarried Status = "+usersta)
print("Tax Payee "+userName +" with PAN "+str(userPan) +" fall under "+finaltax+" % Tax salb.")
print(userName + "("+str(userPan)+")"+" to pay tax to governement is [Rs] = "+str(finaltaxMoney))

