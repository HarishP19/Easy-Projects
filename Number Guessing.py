import random

num=input('Type a Number: ')
if num.isdigit():
    num=int(num)
    if num<=0:
        print("Please enter a number which is greater than 0")     
        quit()
else:
    print("Enter a integer value")
    quit()
     
ran_num=random.randint(0,num)
guess=0

while True:
    guess+=1
    user=input("Try guessing: ")
    if user.isdigit():
     user=int(user)
    
    else:
       print("Enter a integer value")
       continue
    if ran_num==user:
       print("You got it:)")
       break
    elif user>num:
       print("You are going above the value")
    else:
       print("Keep trying")

print("You have done in",guess,"guesses")

