singers = list(("Shakira", "Dualipa", "Beyonce"))
numbers=[1,2,4,6,3,8]

# Sort
print(numbers)
numbers.sort()
print(numbers)

# Add elements at the end
singers.append('Britney Spears')

# Add elements at a specific position

singers.insert(2,'Madonna')
print(singers)

# Delete an element
singers.pop(2)
print(singers)

# Delete by name
singers.remove('Shakira')
print(singers)

# Reverse list
numbers.reverse()
print(numbers)

# Search
print('Britney Spears' in singers)

# Count elements
print(len(numbers))

# Count repetitions
numbers.append(8)
numbers.append(8)
print(numbers.count(8))

# Find index
print(singers.index('Beyonce'))

# Join to elements
singers.extend(numbers)
print(singers)
