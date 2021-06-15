"""
 The variables allow to save information.
"""

# Print a text
text = "Python is cool"
print(text)

# Print a number
num = 2021
print(num)

# Print a decimal
decimal = 3.1415
print(decimal)

# Reassing the value of a variable
decimal = 4.8
print(decimal) 

# Concatenation - Four ways
name = "Marianella"
lastname = "Monroy"
twitter = "@nelimonroyortiz"

print(name + " " + lastname + " - " + twitter)

print(f"{name} {lastname} - {twitter}")

print("Hello, my name is {} {} and my Twitter is {}".format(name, lastname, twitter))

print(name, lastname, "-", twitter)