# Day 7 - Hangman Game

This folder contains my solutions and practice exercises for **Day 7** of the **100 Days of Python Bootcamp**.

## Topics Covered

- Breaking a problem into smaller parts
- Using `while` loops
- Using `for` loops
- Lists and strings
- Importing modules and custom files
- Managing game state
- Building a complete Hangman game

## Project Included

### Hangman
A command-line implementation of the classic Hangman word guessing game.

The program:

1. Randomly selects a word from a predefined list.
2. Displays blanks representing each letter.
3. Allows the user to guess one letter at a time.
4. Tracks correct and incorrect guesses.
5. Reduces lives for wrong guesses.
6. Ends when the user guesses the word or runs out of lives.

## Example Output

```text
_ _ _ _ _
Guess a letter: a
Correct!

a _ _ _ a
Guess a letter: z
Wrong! You lose a life.

Lives left: 5