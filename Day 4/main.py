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

game_images = [rock,paper,scissors]



user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 0 and user_choice <= 2:
    print(f"You chose{game_images[user_choice]}")

computer_choice = random.randint(0,2)

if user_choice >= 0 and user_choice <= 2:
    print(f"Compute chose{game_images[computer_choice]}")
    print(computer_choice)

if user_choice >= 3 or user_choice < 0:
    print("You entered invalid input. You lose!")

elif user_choice == 0 and computer_choice == 2:
    print("You Win!")

elif user_choice == 2 and computer_choice == 0:
    print("Computer Wins!")

elif user_choice < computer_choice:
    print("Computer Wins!")

elif user_choice > computer_choice:
    print("You Win!")
    
elif user_choice == computer_choice:
    print("It's a Draw!")

