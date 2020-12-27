word = input("Enter word : ")
finalword = ""
for x in word:
    if(x.isupper()):
      finalword = finalword + x.lower()
    else:
      finalword = finalword + x.upper()

print(finalword)