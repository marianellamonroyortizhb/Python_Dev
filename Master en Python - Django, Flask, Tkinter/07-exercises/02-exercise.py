"""
Exercise 2
    - Write all the pair numbers lower or equal to 100. 
"""

print("Exercise 2")

counter = 2
pair =str(0)
while counter <= 100 : 
    pair = pair + ", " + str(counter)
    counter = counter + 2 
print("The pair numbers lower than 100 are:")
print(pair)
