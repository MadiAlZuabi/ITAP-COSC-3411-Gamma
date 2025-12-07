#!/usr/bin/env python3
import math

print("Simple Calculator")
print("Operators: +  -  *  /  sin  cos  tan")
print("Type 'exit' to quit.\n")

while True:
    operator = input("Enter operator: ")

    if operator.lower() == "exit":

        break


    if operator in ("sin", "cos", "tan"):
        num = input("Enter number: ")

        if num.lower() == "exit":

            break

        num = float(num)

        if operator == "sin":
            print("Result:", math.sin(num))
        elif operator == "cos":
            print("Result:", math.cos(num))
        elif operator == "tan":
            print("Result:", math.tan(num))


    else:
        num1 = input("Enter first number: ")
        if num1.lower() == "exit":

            break

        num2 = input("Enter second number: ")
        if num2.lower() == "exit":

            break

        num1 = float(num1)
        num2 = float(num2)

        if operator == "+":
            print("Result:", num1 + num2)
        elif operator == "-":
            print("Result:", num1 - num2)
        elif operator == "":
            print("Result:", num1 num2)
        elif operator == "/":
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Error")
        else:
            print("Invalid operator")

    print()
