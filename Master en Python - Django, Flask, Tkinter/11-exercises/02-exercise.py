"""
Exercise 2
Write a program that add values to a list, if their lenght is lower than 12. Show the list ath the end.
"""
print("Exercise 2")

numbersList = list()
newNumber=""

# Create a list with input in for
for count in range (0,12):
    newNumber= input("Add a number ")
    numbersList.append(int(newNumber))

print("**** List 1 - For****")
print(numbersList)
print()

# Create a list with input in while

numbersList2 = list()
newNumber2=""
counter = 0
while counter <= 12:
    newNumber= input("Add a number ")
    numbersList2.append(int(newNumber))
    counter = counter + 1

print("**** List 2 - While ****")
print(numbersList2)