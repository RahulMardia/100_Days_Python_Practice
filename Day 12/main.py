from art import logo
import random
def guess_number():

    print(logo)

    print("Welcome to the Number Guessing Game!\n I'm thinking of a number between 1 and 100.")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()

    attempts = 0

    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
    else:
        print("Invalid Input!")
        guess_number()

    number =  random.randint(1,100)


    while(attempts > 0):

            print(f"You have {attempts} attempts remaining to guess the number.")
            guess = int(input("Make a guess:"))
            if guess == number:
                print(f"You got it! The answer was {guess}.")
            elif guess < number:
                print("Too low.\nGuess again.")
                attempts-= 1
            elif guess > number:
                print("Too High.\nGuess again.")
                attempts -= 1

    print("All attempts failed. You Lose!")
    print(f"The number was {number}.")
guess_number()

