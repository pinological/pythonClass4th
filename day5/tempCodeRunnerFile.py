print("\t\tDepartment of Transport Management")
print("\t\t\tBaneswor, Kathmandu")
print("\t\tWelcome to DOTM Bike Renewal System")
print("\t\t\tFiscal Year 2020/21")

custName = input("Customer Name : ")
custAdd = input("Customer Address : ")
custCC = int(input("Customer Bike in cc : "))
custPhone = input("Phone No : ")

if(custCC <=125):
    finalmoeny = 2800
elif(custCC >= 126 and custCC <=160):
    finalmoeny = (2800+4500)
elif(custCC >= 161 and custCC <=250):
    finalmoeny = (2800+4500+5500)
elif(custCC >= 251 and custCC <=400):
    finalmoeny = (2800+4500+5500+9000)
elif(custCC >= 401 and custCC <=650):
    finalmoeny = (2800+4500+5500+9000+20000)
elif(custCC >= 651):
    finalmoeny = (2800+4500+5500+9000+20000+30000)



print("\t\tDepartment of Transport Management")
print("\t\t\tBaneswor, Kathmandu")
print("\t\tWelcome to DOTM Bike Renewal System")
print("\t\t\tFiscal Year 2020/21")
print("Customer Name: "+custName+"\t\t\t\tAddress:"+custAdd)
print("Customer Bike[cc]: "+str(custCC)+"\t\t\t\tPhone No:"+custPhone)
print(custName+" with "+str(custCC)+" Bike have to pay Tax to [Rs] = "+str(finalmoeny))
