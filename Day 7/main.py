import random
from hangman_words import word_list
from hangman_art import stages,logo

lives = 6

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"****************************<???>/{lives} LIVES LEFT****************************")
    while True:
        char = input("Guess a letter: ").lower()
        if len(char) == 1:
            guess = char
            break
        print("Invalid input. Please try again.")



    if guess in correct_letters:
        print(f"You've already guessed: {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter

        else:
            display += "_"

    print("Word to guess: " + display)

   

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")




    if "_" not in display or lives <= 0:
        game_over = True
        if lives <=0 :
            print(f"***********************IT WAS {chosen_word}. YOU LOSE**********************")
        elif ("_" not in display):

            print("****************************YOU WIN****************************")

    print(stages[lives])
