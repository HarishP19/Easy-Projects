name=input("Enter your name:")
print("Welcome",name.upper(),"to this adventure!")
answer=input("You come to an END and you can go left or right. Which would you like to do? ").lower()
if answer=="left":
        a1=input("You reached to a river, you can go around or wanna swim across? Type walk across or swim: ").lower()
        if a1=="walk":
               print("You walked far miles and You see a DARK HOUSE")
               a2=input("You want to enter house or leave? Type enter or leave: ").lower()
               if a2=="enter":
                      print("You have entered into the Knull house it is the wrong decision you have done ")
               elif a2=="leave":
                      print("Its the right decision you made and You reached your home safely! ")
               else:
                     print("You entered invalid value so YOU LOSE") 
        elif a1=="swim":
               print("You got killed by crocodile")
        else:
               print("You entered invalid value so YOU LOSE")
elif answer=="right":
        print("You came across and you saw the theif and they are trying to steal the house You want to call the Police or fight yourself?  ")
        a5=input("Type Police or Fight: ")
        if a5=="police":
               print("Police came and they arreseted the theif")
        elif a5=="fight":
               a3=input("You want to enter the house in front door or back door? Type front or back: ").lower()
               if a3=="front":
                      print("Theif saw you and They shoot in the head, YOU DIED and You lose")
               elif a3=="back":
                      print("You went through the back door")
                      a4=input("You seacrhing for weapon and you got gun and knife,Do you want to threaten them or kill them? Type threaten or kill: ").lower()
                      if a4=="kill":
                             print("You shoot them all,You got an award for bravery")
                      elif a4=="threaten":
                             print("They shoot you and YOU DIED!")
                      else:
                             print("You entered invalid value so YOU LOSE")
               else:
                      print("You entered invalid value so YOU LOSE")
                             
                      
else:
    print("You entered invalid value so YOU LOSE")
