# ☕ Day 15 - Coffee Machine Project

## Overview

This project is a command-line Coffee Machine simulation built in Python as part of my **100 Days of Code Python Challenge**.

The coffee machine can prepare different types of coffee, manage available resources, process coin-based payments, return change, and generate reports of remaining resources.

## Features

### ☕ Coffee Selection

Users can order:

* Espresso
* Latte
* Cappuccino

### 📦 Resource Management

The machine tracks:

* Water (ml)
* Milk (ml)
* Coffee (g)
* Money ($)

Before preparing a drink, the machine verifies that sufficient resources are available.

### 💰 Payment Processing

The machine accepts:

* Quarters ($0.25)
* Dimes ($0.10)
* Nickels ($0.05)
* Pennies ($0.01)

It:

* Calculates the total amount inserted.
* Checks whether the payment is sufficient.
* Returns change when applicable.
* Rejects orders when insufficient funds are provided.

### 📊 Reporting

Using the `report` command, users can view:

* Remaining water
* Remaining milk
* Remaining coffee
* Total money collected

### 🔌 Machine Control

Using the `off` command, the machine can be turned off.

---

## Sample Output

```text
What would you like? (espresso/latte/cappuccino): espresso

Please insert coins.
How many quarters?: 12
How many dimes?: 1
How many nickles?: 1
How many pennies?: 1

Here's your change: $1.66
Here's your espresso. Enjoy your coffee!!.

What would you like? (espresso/latte/cappuccino): latte

Please insert coins.
How many quarters?: 12
How many dimes?: 0
How many nickles?: 0
How many pennies?: 0

Here's your change: $0.5
Here's your latte. Enjoy your coffee!!.

What would you like? (espresso/latte/cappuccino): report

Water: 50ml
Milk: 50ml
Coffee: 58g
Money: $4.0

What would you like? (espresso/latte/cappuccino): off
```

---

## Concepts Practiced

* Python Dictionaries
* Nested Dictionaries
* Loops (`while`, `for`)
* Conditional Statements
* User Input Handling
* Resource Validation
* Payment Calculations
* Change Calculations
* Dynamic Dictionary Access
* String Formatting (f-strings)

---

## Learning Journey

This project was developed independently as part of my Python learning journey.

Key challenges I worked through on my own:

* Dynamically checking ingredient availability.
* Accessing nested dictionary values.
* Managing coffee machine resources.
* Processing coin-based payments.
* Calculating and returning change.
* Updating resources only after successful transactions.

The focus of this project was understanding the logic and problem-solving process rather than simply reaching the final solution.

---

## Future Improvements

Potential enhancements:

* Refactor the code into reusable functions.
* Add more drink options.
* Improve user input validation.
* Support exact payment handling more elegantly.
* Add transaction history.
* Create a GUI version using Tkinter.

---

## Author

**Rahul Mardia**

Learning Python through the **100 Days of Code: The Complete Python Pro Bootcamp** and building projects from scratch to strengthen problem-solving skills and programming fundamentals.

---

### Feedback Welcome

If you find any bugs, edge cases, or opportunities for improvement, feel free to open an issue or share your suggestions. Feedback helps me learn and improve.
