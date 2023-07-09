import random
user_life=3
comp_life=3
options = ["Rock", "Paper", "Scissors"]
while user_life!=0 and comp_life!=0:
    user_choice = input("Choose Rock, Paper, or Scissors: ")
    computer_choice = random.choice(options)
    print("You chose: ", user_choice)
    print("Computer chose: ", computer_choice)
    if user_choice == computer_choice:
        pass
    elif user_choice == "Rock" and computer_choice == "Scissors":
        comp_life-=1
    elif user_choice == "Paper" and computer_choice == "Rock":
        comp_life-=1
    elif user_choice == "Scissors" and computer_choice == "Paper":
        comp_life-=1
    else:
        user_life-=1
    print(comp_life)
    print(user_life)
if comp_life==0:
    print("User Wins")
else:
    print("comp_wins")