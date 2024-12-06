print("Welcome to My Computer QUIZZ")
playing=input("Do you want to PLAY? Type Yes or No: ")
if playing.lower() !='yes':
    print("See You Byee:(")
    quit()
print("Okay! Let's GOOOO ----->")
print("Well, There is total 10 Question and Take your time to Finish it")
score=0
q=10
q1=input("1. What does CPU stands for? ")
if q1.lower()=='central processing unit':
    print("You are right:)")
    score+=1
else:
    print("Incorrect!")
q2=input("2. What does GPU stands for? ")
if q2.lower()=='graphics processing unit':
    print("You are right:)")
    score+=1
else:
    print("Incorrect!")
q3=input("3. What does RAM stands for? ")
if q3.lower()=='random access memory':
    print("You are right:)")
    score+=1
else:
    print("Incorrect!")
q4=input("4. What does ROM stands for? ")
if q4.lower()=='read only memory':
    print("You are right:)")
    score+=1
else:
    print("Incorrect!")
q5=input("5. What is the contol for save? Ctrl+ ")
if q5.lower()=='s':
    print("You are right:)")
    score+=1
else:
    print("Incorrect!")
q6=input("6. What is the contol for copy? Ctrl+ ")
if q6.lower()=='c':
    print("You are right:)")
    score+=1
else:
    print("Incorrect!")
q7=input("7. What is the contol for paste? Ctrl+ ")
if q7.lower()=='v':
    print("You are right:)")
    score+=1
else:
    print("Incorrect!")
q8=input("8. What is the contol for undo? Ctrl+ ")
if q8.lower()=='z':
    print("You are right:)")
    score+=1
else:
    print("Incorrect!")
q9=input("9. What is the contol for redo? Ctrl+ ")
if q9.lower()=='y':
    print("You are right:)")
    score+=1
else:
    print("Incorrect!")
q10=input("10. What is the keyword for shutdown? ")
if q10.lower()=='alt+f4':
    print("You are right:)")
    score+=1
else:
    print("Incorrect!")
print("Your Total Score:",score,'/',q)
print("Your Percentage:",(score/10)*100,'%')