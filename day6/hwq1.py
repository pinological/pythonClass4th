string = input("Enter string: ")
vowels = 0
for i in string:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels+1
print("Number of vowels are: "+str(vowels))
if vowels > 1:
    for i in range(2, vowels):
        if (vowels % i) == 0:
            print(str(vowels)+" is not a prime number")
            for j in range(1, 11):
                temp = vowels*j
                print(str(vowels)+ " X "+str(j)+ " = "+str(temp))
            break
    else:
        print(vowels, "is a prime number")
