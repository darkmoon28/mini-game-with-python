import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

game_image = [rock, paper, scissors]

i = 0
my_score = 0
coms_score = 0

while i < 3:

    i += 1
    user_choice = int(input("What do you choose ? Type 0 for Rock, 1 for Paper, 2 for Scissors ?\n"))

    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number, you lose")
    else:
        print(game_image[user_choice])

        computer_choice = random.randint(0, 2)

        print("Computer chose: ")
        print(game_image[computer_choice])

        if user_choice == 0 and computer_choice == 2:
            print("You win")
            my_score += 1
        elif computer_choice == 0 and user_choice == 2:
            print("You lose")
            coms_score += 1
        elif computer_choice > user_choice:
            print("You lose")
            coms_score += 1
        elif user_choice > computer_choice:
            print("You win")
            my_score += 1
        elif computer_choice == user_choice:
            print("it's a draw")
            my_score += 0
            coms_score += 0

        print(f"user {my_score} & computer {coms_score}")

print(f"your score {my_score}")

if my_score > coms_score:
    print("Your win!")
elif my_score == coms_score:
    print("Draw!")
else:
    print("Your lose")