from PIL import Image,ImageDraw,ImageFont
from datetime import date
today = date.today()
img = Image.open("C:/Users/Pinological/Desktop/python classwork/Result making/main.png")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("arial.ttf",20)
def main():
    inputfromuser()
    basicMarketing()
    commerce()
    computerg()
    mobile()
    img.show()
    img.save("final.png")


def inputfromuser():
    print("Basic info")
    name = input("Enter Your name :")
    issudate = today
    classs = input("Enter Semester :")
    section = input("Enter Section :")
    reenum = input("Enter REGD NO :")
    draw.text((143,220),name,"Black",font=font)
    draw.text((682,220),classs,"Black",font=font)
    draw.text((1056,220),section,"Black",font=font)
    draw.text((1315,220),reenum,"Black",font=font)
    draw.text((1172,161),str(issudate),"Red",font=font)
    

def basicMarketing():
    print("Basic marketing :")
    firstass = int(input("1st Assignment mark [10] :"))
    internal = int(input("Internal Examination [10] :"))
    attendance = int(input("Student Attendance [10] :"))
    quizz = int(input("Quizzes or lab [10] :"))
    group = int(input("Group project [10] :"))
    total = firstass+internal+attendance+quizz+group
    height = 383
    draw.text((401,height),str(firstass),"Black",font=font)
    draw.text((587,height),str(internal),"Black",font=font)
    draw.text((823,height),str(attendance),"Black",font=font)
    draw.text((1123,height),str(quizz),"Black",font=font)
    draw.text((1287,height),str(group),"Black",font=font)
    draw.text((1387,height),str(total),"Red",font=font)
    

def commerce():
    print("Introduction To E-Commerce :")
    firstass = int(input("1st Assignment mark [10] :"))
    internal = int(input("Internal Examination [10] :"))
    attendance = int(input("Student Attendance [10] :"))
    quizz = int(input("Quizzes or lab [10] :"))
    group = int(input("Group project [10] :"))
    total = firstass+internal+attendance+quizz+group
    height = 499
    draw.text((401,height),str(firstass),"Black",font=font)
    draw.text((587,height),str(internal),"Black",font=font)
    draw.text((823,height),str(attendance),"Black",font=font)
    draw.text((1123,height),str(quizz),"Black",font=font)
    draw.text((1287,height),str(group),"Black",font=font)
    draw.text((1387,height),str(total),"Red",font=font)
    

def computerg():
    print("Computer Graphics :")
    firstass = int(input("1st Assignment mark [10] :"))
    internal = int(input("Internal Examination [10] :"))
    attendance = int(input("Student Attendance [10] :"))
    quizz = int(input("Quizzes or lab [10] :"))
    group = int(input("Group project [10] :"))
    total = firstass+internal+attendance+quizz+group
    height = 595
    draw.text((401,height),str(firstass),"Black",font=font)
    draw.text((587,height),str(internal),"Black",font=font)
    draw.text((823,height),str(attendance),"Black",font=font)
    draw.text((1123,height),str(quizz),"Black",font=font)
    draw.text((1287,height),str(group),"Black",font=font)
    draw.text((1387,height),str(total),"Red",font=font)
    

def mobile():
    print("Mobile Programming :")
    firstass = int(input("1st Assignment mark [10] :"))
    internal = int(input("Internal Examination [10] :"))
    attendance = int(input("Student Attendance [10] :"))
    quizz = int(input("Quizzes or lab [10] :"))
    group = int(input("Group project [10] :"))
    total = firstass+internal+attendance+quizz+group
    height = 671
    draw.text((401,height),str(firstass),"Black",font=font)
    draw.text((587,height),str(internal),"Black",font=font)
    draw.text((823,height),str(attendance),"Black",font=font)
    draw.text((1123,height),str(quizz),"Black",font=font)
    draw.text((1287,height),str(group),"Black",font=font)
    draw.text((1387,height),str(total),"Red",font=font)
    




main()




