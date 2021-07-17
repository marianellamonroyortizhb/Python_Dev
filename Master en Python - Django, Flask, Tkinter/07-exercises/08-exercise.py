"""
Exercise 8
    - Percent of a number.
"""

print("Exercise 8")
number1 = int(input("Welcome. Please write a number: "))
number2 = int(input("Write the percent that you want to know: "))
print("")

percent = int(number1) * (float(0.01) * int(number2))
print(f"The {number2}% of {number1} is: {percent}")
