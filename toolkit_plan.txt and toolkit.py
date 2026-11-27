# POWER LEARN PROJECT (PLP)
# WEEK 8 FINAL PROJECT — PERSONAL MINI-TOOLKIT

**Student Name:** Mahamud Abdi  
**Project Title:** Personal Mini-Toolkit  
**Programming Language:** Python  
**GitHub Repository:** plp-python-week8

---

# PART A — TOOLKIT PLAN

## 1. Selected Tools

I have selected three useful tools for my Personal Mini-Toolkit.

### Tool 1: Simple Calculator
This tool allows users to perform basic mathematical operations, including addition, subtraction, multiplication and division.

### Tool 2: To-Do List
This tool allows users to add tasks, view their tasks and manage a simple list of activities.

### Tool 3: Number Guessing Game
This tool generates a random number, and the user tries to guess the correct number.

## 2. Exact Menu Text

```text
=================================
       PERSONAL MINI-TOOLKIT
=================================
1. Simple Calculator
2. To-Do List
3. Number Guessing Game
4. Quit
=================================
Enter your choice (1-4):
```

## 3. Programming Concepts Used

| Tool | Programming Concepts |
|---|---|
| Simple Calculator | Variables, input, conditionals, arithmetic operators |
| To-Do List | Lists, loops, input and conditionals |
| Number Guessing Game | Random numbers, loops, conditionals |
| Main Menu | While loop, if/elif/else, input and output |

---

# PART B — BUILD THE MENU LOOP

## File: toolkit.py

```python
import random

# Store tasks in a list
tasks = []


# TOOL 1: SIMPLE CALCULATOR
def calculator():
    print("\n--- SIMPLE CALCULATOR ---")

    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                return
            result = num1 / num2
        else:
            print("Invalid operator.")
            return

        print(f"Result: {result}")

    except ValueError:
        print("Please enter valid numbers.")


# TOOL 2: TO-DO LIST
def todo_list():
    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Return to main menu")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            task = input("Enter your task: ")

            if task.strip():
                tasks.append(task)
                print("Task added successfully!")
            else:
                print("Task cannot be empty.")

        elif choice == "2":
            if len(tasks) == 0:
                print("Your task list is empty.")
            else:
                print("\nYour Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")


# TOOL 3: NUMBER GUESSING GAME
def guessing_game():
    print("\n--- NUMBER GUESSING GAME ---")
    print("Guess a number between 1 and 10.")

    secret_number = random.randint(1, 10)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 10:
                print("Choose a number between 1 and 10.")

            elif guess < secret_number:
                print("Too low! Try again.")

            elif guess > secret_number:
                print("Too high! Try again.")

            else:
                print(f"Congratulations! You guessed correctly.")
                print(f"Number of attempts: {attempts}")
                break

        except ValueError:
            print("Please enter a valid whole number.")


# MAIN PROGRAM: MENU LOOP
while True:
    print("\n=================================")
    print("       PERSONAL MINI-TOOLKIT")
    print("=================================")
    print("1. Simple Calculator")
    print("2. To-Do List")
    print("3. Number Guessing Game")
    print("4. Quit")
    print("=================================")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        calculator()

    elif choice == "2":
        todo_list()

    elif choice == "3":
        guessing_game()

    elif choice == "4":
        print("\nThank you for using Personal Mini-Toolkit!")
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select between 1 and 4.")
```

---

# PART C — EXPECTED PROGRAM BEHAVIOUR

When you run `toolkit.py`, the program displays:

```text
=================================
       PERSONAL MINI-TOOLKIT
=================================
1. Simple Calculator
2. To-Do List
3. Number Guessing Game
4. Quit
=================================
Enter your choice (1-4):
```

### Example 1: Calculator

```text
--- SIMPLE CALCULATOR ---
Enter the first number: 20
Enter operator (+, -, *, /): +
Enter the second number: 10
Result: 30.0
```

### Example 2: To-Do List

```text
--- TO-DO LIST ---
1. Add a task
2. View tasks
3. Return to main menu

Enter your choice (1-3): 1
Enter your task: Complete my Python assignment
Task added successfully!
```

### Example 3: Number Guessing Game

```text
--- NUMBER GUESSING GAME ---
Guess a number between 1 and 10.
Enter your guess: 3
Too low! Try again.
```

*The secret number is generated randomly, so the result changes each time.*

### Example 4: Quit

```text
Thank you for using Personal Mini-Toolkit!
Goodbye!
```

---

# PART D — PROJECT CONCLUSION

The Personal Mini-Toolkit combines important Python programming concepts into one menu-driven application.

The project demonstrates:
- Variables and user input.
- Conditional statements.
- While and for loops.
- Lists and list operations.
- Functions.
- Error handling using try and except.
- Random number generation.
- Formatted output using f-strings.

The application allows users to select different tools and return to the main menu without restarting the program.

---

# GITHUB SUBMISSION DETAILS

**Exact repository name:** `plp-python-week8`

**Visibility:** Public

**GitHub username:** `thesonofbillionairemom-netizen`

**Repository link:**

https://github.com/thesonofbillionairemom-netizen/plp-python-week8

## Required repository structure

```text
plp-python-week8/
│
├── toolkit_plan.txt
│
└── toolkit.py
```

## Final Submission Checklist

- [ ] Create a public GitHub repository named `plp-python-week8`.
- [ ] Create `toolkit_plan.txt` and paste Part A into it.
- [ ] Create `toolkit.py` and paste the complete Python program into it.
- [ ] Run the program and test all three tools.
- [ ] Test the Quit option.
- [ ] Take a screenshot showing the program running.
- [ ] Add both files to GitHub.
- [ ] Open your repository in an incognito browser to confirm it is public.
- [ ] Submit your GitHub repository link on the LMS.

**End of Week 8 Final Project.**
