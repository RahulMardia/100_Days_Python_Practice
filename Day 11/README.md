# Day 11 - The Blackjack Capstone Project

This folder contains my complete implementation of the **Blackjack** game, built as part of **Day 11** of the **100 Days of Python Bootcamp**.

## Project Overview

### Blackjack
A command-line version of the classic Blackjack card game where the player competes against the computer (dealer).

The game includes:

- Random card dealing
- Score calculation
- Automatic Ace value adjustment (11 → 1 when needed)
- Dealer logic to draw cards until reaching 17
- Win, lose, and draw conditions
- Option to play multiple rounds

## Topics Covered

- Breaking large problems into smaller functions
- Functions with return values
- Recursive function calls to restart the game
- Complex conditional logic
- Lists and random selection
- Game development in Python

## Personal Learning Notes

This project was a major milestone in my Python journey.

While building this project, I wanted to fully understand how recursive functions and `return` statements work. To strengthen my understanding, I researched these concepts independently using online resources and documentation.

**Important Note:**

- The entire Blackjack code was written completely by me.
- I did not copy or compare my implementation with the course solution.
- Every function and logic flow was developed based on my own understanding and experimentation.
- The external research was only used to understand concepts such as recursion and return values—not to obtain the final solution.

This project gave me a much deeper understanding of how real programs are structured and how functions communicate with each other.

## Example Output

```text
Welcome to Blackjack!
Your cards: [10, 7], current score: 17
Computer's first card: 9

Type 'y' to get another card, type 'n' to pass:
y

Your final hand: [10, 7, 4], final score: 21
Computer's final hand: [9, 7, 5], final score: 21
Draw 🙃