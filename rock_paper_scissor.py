import random
user_win=0
com_win=0
option= ["rock","paper","scissor"]
while True:
    user=input("Type Rock/Paper/Scissor or Q to Quit: ").lower()
    if user=='q':
        break
    if user not in option:
        continue

    random_num=random.randint(0,2)
    computer_pick=option[random_num]
    print("Computer Picked:",computer_pick)

    if user=="rock"and computer_pick=="scissor":
        print("You won")
        user_win+=1
        continue
    if user=="scissor"and computer_pick=="paper":
        print("You won")
        user_win+=1
        continue
    if user=="paper"and computer_pick=="rock":
        print("You won")
        user_win+=1
        continue
    if user==computer_pick:
        print("Draw")
        continue
    else:
        print("You Loose")
        com_win+=1
        continue

print("Computer win",com_win,"times")
print("You won",user_win,"times")
print("BYE! SEE YOU SOON")
