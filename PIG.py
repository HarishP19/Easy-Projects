import random
def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value,max_value)

    return roll

while True:
   players=input("Enter the number of players(1-4): ")
   if players.isdigit():
       players=int(players)
       if 2<= players <=4:
           break
       else: 
           print("Must be between 2 - 4 players.")
   else:
       print("Invalid,Try again")
       
       

max_score=50
player_score=[0 for i in range(players)]

while max(player_score)<max_score:
    for pla_idx in range(players):
      print("\n Player number",pla_idx+1,"turn has just started\n")  
      curr=0

      while True:

         rol=input("Would you like to roll (y)? ")
         if rol.lower()!="y":
           break
    
    
         value=roll()
         if value==1:
           print("You rolled a",value)
           curr=0
           break
         else: 
          curr+=value
          print("You rolled a",value)
          print("Your current score is",curr)

      player_score[pla_idx]+=curr
      print("your total score is : ",player_score[pla_idx])