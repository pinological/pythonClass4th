word = input("Write something : ")
vo,co = 0,0
for x in word:
    if(x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'):
        print("The alphabet "+x+" is vowel")
        vo = vo+1
    else:
        print("The alphabet "+x+" is  consonant")
        co = co +1
print("total number of vowel : "+str(vo)+" and total number of consonant : "+str(co))