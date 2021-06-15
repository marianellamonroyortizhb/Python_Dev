"""
Exercise 5
    - Make a program that show all the numbers between two that select the user.
"""

print("Exercise 5")
number1 = int(input("Welcome. Please write the first number: "))
number2 = int(input("Write the second number: "))
print("")

if number1 < number2:
    for number in range((number1), (number2 + 1)):
        print(number)
else:
    print("The number1 must be lower than number2.")
