# Rock, Paper, Scissors Game
import random

rock = '''
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

print("Welcome to Rock, Paper, Scissors!\n")
user_choice = int(input("What will be your choice? Type 0 for Rock, 1 for Paper, or 2 for Scissors:\n"))
if 0 <= user_choice <= 2:
    print("Your Choice: " + options[user_choice])
computer_choice = random.randint(0,2)
print("Computer Choice: " + options[computer_choice])

if user_choice == computer_choice:
    print("Draw")
elif (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1) or (user_choice == 0 and computer_choice == 2):
    print("You Win!")
elif (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 1):
    print("Computer Wins!")
else:
    print("The value you typed is invalid")

