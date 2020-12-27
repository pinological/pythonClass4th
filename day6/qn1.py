numrang = int(input("Enter range :"))
start,final = 1,0
fordis = ''
while start <=numrang:
    tmp = start
    start = start+1
    fordis = fordis +"+"+str(tmp)
    final = final+tmp
    print(fordis)

print("the sum of "+fordis+" is "+str(final))
    