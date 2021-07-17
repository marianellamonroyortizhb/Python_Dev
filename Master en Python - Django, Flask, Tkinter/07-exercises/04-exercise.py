"""
Exercise 4
    - Make a calculator using the number that select the user.
"""

print("Exercise 4 - Calculator")
number1 = input("Welcome. Please write the first number: ")
number2 = input("Write the second number: ")

operator = input ("Write the operator (+, -, *, /): " )

result = number1 + " " +  operator +  " " + number2
print (str(result) + " = " + str(eval(result)))
