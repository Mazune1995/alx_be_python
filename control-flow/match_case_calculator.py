#!/usr/bin/python3
    num1 = float(input("Enter the num1: "))
    num2 = float(input("Enter the num2: "))
except ValueError:
    print("Invalid input. Please enter numeric values.")
    exit()
# Ask the user to choose an operation
operation = input("Choose the operation (+, -, *, /): ").strip()
# Perform calculation using match-case
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    case _:
        print("Invalid operation. Please choose one of +, -, *, /.")
#
