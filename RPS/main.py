import random
user_score=0
comp_score=0

print("""Winning rules are ----
      rock vs scissors ==> rock wins
      paper vs rock ==> paper wins
      paper vs scissors ==> scissors wins
      
      Now let's start the game """)
print()
while True:
  print("Choose one between rock,paper and scissors")
  user=input("Enter choice :").lower()
  while user not in["rock", "paper","scissors"]:
    print("Invalid Input")
    user=input("Enter valid choice:")
  print("User's choice is :", user)
  game=["rock","paper","scissors"]
  comp=random.choice(game)
  print("Computer's choice is:", comp)
  if user=="rock" and comp=="paper":
     print("Computer Wins")
     comp_score+=1
  elif user=="paper" and comp=="rock":
     print("User Wins")
     user_score +=1
  elif user=="rock" and comp=="scissors":
     print("User Wins")
     user_score +=1
  elif user=="scissors" and comp=="rock":
     print("Computer Wins")
     comp_score+=1
  elif user=="paper" and comp=="scissors":
     print("Computer Wins")
     comp_score+=1
  elif user=="scissors" and comp=="paper":
     print("User Wins")
     user_score +=1
  else:
     print("It's a Tie")
  print("User's score is : ", user_score)
  print("Computer's score is : ", comp_score)
  repeat=input("Do you want to play again ?").lower()
  if repeat=="no":
     break

