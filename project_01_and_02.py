#(Project 1) : Simple Calculator
print('''Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Modulus''')

Operator = int(input("Enter choice (1/2/3/4/5):"))
n1 = float(input("Enter first number:"))
n2 = float(input("Enter second number:"))

if Operator == 1:
    print(n1,"+",n2,"=",n1+n2)
elif Operator == 2:
    print(n1,"-",n2,"=",n1-n2)
elif Operator == 3:
    print(n1,"x",n2,"=",n1*n2)
elif Operator== 4:
    print(n1,"÷",n2,"=",n1/n2)
elif Operator == 5:
    print(n1,"%",n2,"=",n1%n2)
else:
    print("Invalid choice!")
  
print("Thanks for using")




#(Project 2): Number Guessing Game

import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("Try to guess the number between 1 and 100.")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break

number_guessing_game()