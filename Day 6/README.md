# Day 6 - Python Functions and Karel

This folder contains my solutions for **Day 6** of the **100 Days of Python Bootcamp**.

## Topics Covered

- Defining functions using `def`
- Calling functions
- Function parameters
- Indentation in Python
- Code blocks and scope
- Solving problems using Karel (Reeborg's World)

## Project Included

### Escaping the Maze
A problem-solving challenge in Reeborg's World where a robot must navigate through a maze and find the exit using Python functions and control logic.

The program uses custom functions such as:

- `turn_left()`
- `turn_right()`
- `move()`
- `front_is_clear()`
- `right_is_clear()`
- `at_goal()`

## Example Solution Logic

```python id="8bligf"
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()