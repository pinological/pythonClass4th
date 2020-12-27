"))
    group = int(input("Group project [10] :"))
    total = firstass+internal+attendance+quizz+group
    height = 671
    draw.text((401,height),str(firstass),"Black",font=font)
    draw.text((587,height),str(internal),"Black",font=font)
    draw.text((823,height),str(attendance),"Black",font=font)
    draw.text((1123,height),str(quizz),"Black",font=font)
    draw.text((1287,height),str(group),"Black",font=font)
    draw.text((1387,height),str(total),"Red",font=font)
    

def main():
   inputfromuser()
   basicMarketing()
   commerce()
   computerg()
   mobile()
   img.show()
   img.save("final.png")


main()
