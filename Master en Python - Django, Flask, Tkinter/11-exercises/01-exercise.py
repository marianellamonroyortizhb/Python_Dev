"""
Exercise 1
Make a program with a list of 8 integer numbers:
- Show
- Function that show the list and return a string.
- Sort
- Lenght
- Search an element 
"""
print("Exercise 1")
print()

# Create the list
integers = [0, 9, 12, 8, 4, 6, 5, 8]

print("The list is:")
print(integers)
print()

# Define the function
def showList(numberList):
    result = ""
    for element in numberList:
        result += "Element: " + str(element)
        result += "\n"
    return result

# Print the list using the fuction
print("Show the list using the fuction")
print(showList(integers))

# Show the list
print("Show the list using a for loop")
for count in integers:
    print(count)
print()
# Short the list
integers.sort()
print("List sorted:")
print(integers)
print()

# Lenght of the list
print("The lenght of the list is: ")
print(len(integers))
print()

# Search a number
searchNumber = int(input("Which number? "))
checking = isinstance(searchNumber, int)

while not checking:
    searchNumber = input("Which number? ")
else:
    print(f"You wrote: {searchNumber}")

print(f"**** Search the number {searchNumber} ****")

search = integers.index(searchNumber)

print(f"The number is in the index {search}")