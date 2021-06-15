"""
Exercise 9
    - Guess the number between 0 and 100.
"""

print("Exercise 9")

correct_n = 29

number = int(input("Welcome. Please write a number between 0 and 100: "))

while (number != correct_n):
    print("Try again!")
    number = int(input("Write a number between 0 and 100: "))
print("Bingo! The number is correct")
