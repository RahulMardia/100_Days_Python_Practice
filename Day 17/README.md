
# Day 17 - Quiz Game (Object-Oriented Programming)

This folder contains my implementation of the **Quiz Game Project**, built as part of **Day 17** of the **100 Days of Python Bootcamp**.

## Project Overview

### Quiz Game

A command-line quiz application that presents True/False questions to the user and tracks their score throughout the game.

The game:

- Displays questions one at a time
- Accepts user answers
- Checks correctness
- Tracks the user's score
- Displays the final result at the end

## Topics Covered

- Object-Oriented Programming (OOP)
- Classes and Objects
- Constructors (`__init__`)
- Attributes and Methods
- Working with Multiple Python Files
- Data Modeling
- Organizing Code Using OOP Principles

## Features

- Score tracking
- Question progression
- Answer validation
- Object-oriented design
- Multiple-file project structure

## Personal Enhancements

In addition to completing the project requirements, I made a few custom improvements:

### Expanded Question Bank

Instead of using the default set of questions, I expanded the quiz to include **100 questions**, making the game longer and more challenging.

### Lives System

I introduced a new game rule:

- The player can answer incorrectly up to **5 times**.
- After the fifth wrong answer, the game ends immediately.
- This adds an extra challenge and encourages careful thinking rather than random guessing.

These modifications were implemented by me as an additional challenge beyond the original project requirements.

## Example Output

```text
Q.1: A slug's blood is green. (True/False): True

Correct!
Score: 1/1

Q.2: The loudest animal is the African Elephant. (True/False): True

Wrong!
Mistakes: 1/5

...
```

## Learning Objectives

By completing this day, I learned how to:

- Create and use custom classes
- Pass objects between classes
- Organize code into separate modules
- Track application state using objects
- Extend existing projects with custom features
- Apply OOP concepts to real-world applications

## Files in This Folder

- `main.py` - Main Quiz Game logic
- `learning.py` - Learning about class and stuff from lessons
- `question_model.py` - Question class definition
- `quiz_brain.py` - Quiz management logic
- `data.py` - Question dataset
- `README.md` - Documentation for this day's work

## How to Run

```bash
python main.py
```

## Feedback Welcome

If you find any bugs, logic issues, or opportunities to improve the code, please feel free to let me know. I enjoy learning from feedback and continuously improving my projects.

## Course Information

This project is part of the **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu on Udemy.

## Author

**Rahul Mardia**

---

Day 17 completed successfully.