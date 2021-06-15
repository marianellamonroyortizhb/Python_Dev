"""
Exercise 3
    - Write the square of the first 40 natural numbers. 
    - Use while and for loop
"""

# While Loop
count = 1
squares = str(0)

print("Exercise 3, using while loop")
while count <= 40:
    squares = squares + "\n" + str(count * count)
    count = count + 1 
print("The square of the first 40 natural numbers are:")
print(squares + "\n")



# For loop

print("Exercise 3, using for loop")
counter = 1
sq = str(0)

for counter in range(0, 40):
    sq = sq + "\n" + str(counter * counter)
print("The square of the first 40 natural numbers are:")
print(squares + "\n")
