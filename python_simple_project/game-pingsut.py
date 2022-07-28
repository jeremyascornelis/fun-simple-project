# Rock, Paper, Scissors Game
# In Indonesia this called pingsut (suit or batu, gunting, kertas)
import random

'''
3 Simple Rules:
=> Rock wins against scissors
=> Scissors win against paper
=> Paper wins against rock
'''

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

games_item = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
if (player_choice >= 3 or player_choice < 0): 
    print("You typed an invalid number, you lose!")
else:
    print(games_item[player_choice])

    computer_choice = random.randint(0, len(games_item) - 1)

    print("Computer choice:")
    print(games_item[computer_choice])


    if (player_choice == 0 and computer_choice == 2):
        print("You win!")
    elif (player_choice == 2 and computer_choice == 0):
        print("You lose")
    elif (player_choice == computer_choice):
        print("It's a draw")
    elif (player_choice > computer_choice):
        print("You win!")
    elif (computer_choice > player_choice):
        print("You lose")