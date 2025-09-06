import random
rock="rock"
paper="paper"
scissors="scissors"
user_input=int(input("what do you choose? Type 0 for rock, 1 for paper or 2 for scissors"))

game_list=[rock,paper,scissors]
print(fgame_list[user_input])

computer_choice=random.randint(0, 2)

print("Computer Chose:")
print(game_list[computer_choice])

if user_input ==computer_choice:
    print("you win")
elif user_input>=3 or user_input<0:
    print("you typed invalid number")
else:
    print("you lose")

