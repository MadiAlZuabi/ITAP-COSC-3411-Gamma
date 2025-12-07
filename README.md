**README**

**Overview**

This is a Python command-line calculator that supports basic arithmetic operations and mathematical functions. The tool runs in a loop until the user types 'exit'. It requires only Python 3.

Setup

**1. Create a new file:**

Mousepad calculator.py



**2. Paste the following code:**

\#!/usr/bin/env python3

import math



print("Simple Calculator")

print("Operators: +  -  \*  /  sin  cos  tan")

print("Type 'exit' to quit.\\n")



while True:

&nbsp;   operator = input("Enter operator: ")



&nbsp;   if operator.lower() == "exit":



&nbsp;       break





&nbsp;   if operator in ("sin", "cos", "tan"):

&nbsp;       num = input("Enter number: ")



&nbsp;       if num.lower() == "exit":



&nbsp;           break



&nbsp;       num = float(num)



&nbsp;       if operator == "sin":

&nbsp;           print("Result:", math.sin(num))

&nbsp;       elif operator == "cos":

&nbsp;           print("Result:", math.cos(num))

&nbsp;       elif operator == "tan":

&nbsp;           print("Result:", math.tan(num))





&nbsp;   else:

&nbsp;       num1 = input("Enter first number: ")

&nbsp;       if num1.lower() == "exit":



&nbsp;           break



&nbsp;       num2 = input("Enter second number: ")

&nbsp;       if num2.lower() == "exit":



&nbsp;           break



&nbsp;       num1 = float(num1)

&nbsp;       num2 = float(num2)



&nbsp;       if operator == "+":

&nbsp;           print("Result:", num1 + num2)

&nbsp;       elif operator == "-":

&nbsp;           print("Result:", num1 - num2)

&nbsp;       elif operator == "":

&nbsp;           print("Result:", num1 num2)

&nbsp;       elif operator == "/":

&nbsp;           if num2 != 0:

&nbsp;               print("Result:", num1 / num2)

&nbsp;           else:

&nbsp;               print("Error")

&nbsp;       else:

&nbsp;           print("Invalid operator")



&nbsp;   print()



**3. Save and exit**



**4. Make the script executable:**

chmod +x calculator.py

**Running the Tool**



**Run with Python:**

python3 calculator.py



**Or run directly if executable:**

./calculator.py



**Usage Example**



**Example interaction:**



Enter operator: +

Enter first number: 10

Enter second number: 5

Result: 15.0



Enter operator: sin

Enter number: 0

Result: 0.0



Enter operator: exit

Exit



