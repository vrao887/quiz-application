""" make a quiz that has 4 options and add 1 point if ans is correct 
    and add -1 point if ans is incorrect 
    also it has option to skip and quit the quiz """

Q1= """ What is the maximum possible length of an identifier?
    a)    16
    b)    32
    c)    64
    d)    None of these above """

Q2=""" Who developed the Python language?
    a)   Zim Den
    b)    Guido van Rossum
    c)    Niene Stom
    d)    Wick van Rossum """

Q3=""" In which year was the Python language developed?
    a)    1989
    b)    1996
    c)    1964
    d)    None of these above """

Q4="""In which language is Python written?
    a)    Java
    b)    PHP
    c)    c
    d)    None of these above """

    # we are making a dic for quetion and its correct ans 

question= {Q1:"d" , Q2:"b" , Q3:"a" , Q4:"c"}
score= 0
for i in question:
    print(i)
    skip=input("do you want to skip this question (y/n) : ")
    if skip == "y" :
        continue

    ans=input("Enter the answere (a/b/c/d) : ")
    if ans == question[i] :
        print("CORRECT ANS , you got 1 point")
        score = score +1
        print("TOTAL SCORE = ",score)
    
    else:
        print("WRONG ANS , you got -1 point")
        score = score -1
        print("TOTAL SCORE = ",score)
    quit= input("do you want to quit this quiz (y/n) : ")
    if quit == "y":
        break

if score <=2:
    print("Sorry!! score is", score, "you are fail in this quiz")

else :
    print("Congratulation!! score is", score, "you have cleared")

