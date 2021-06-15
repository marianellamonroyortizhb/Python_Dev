
"""
IF Conditional

if condition:
    instructions

else:
    other instructions
"""

# Example 1
print(" *** Example 1 *** ")

color = input("Which one is my favorite color? ")

if color == "orange":
    print("It's correct, it's the orange.")

else:
    print("The color isn't " + color)

print("\n")

# Example 2
print(" *** Example 2 *** ")

year = 2022

if year >= 2021:

    print("The year is greater than 2021")

else:
    print("The year is lower than 2021")

# Example 3
print(" *** Example 3 *** ")

name = "Marianella Monroy"
city = "Bogotá"
continent = "America"
age = 28
age_adult = 18

if age >= 18:
    print(name + " is an adult.")
    if continent == "America":
        print(name + " is American.")
    
    else:
        print(name + "is from another continent")

else:
    print(name + "is young")

"""
if condition1:
    instructions1
elif condition2:
    instructions2
else:
    instructions3
"""

# Example 4
print(" *** Example 4 *** ")

day = 3

if day == 1:
    print("Today is Monday")
elif day == 2:
    print("Today is Tuesday")
elif day == 3:
    print("Today is Wednesday")
elif day == 4:
    print("Today is Thursday")
elif day == 5:
    print("Today is Friday")
elif day == 6:
    print("Today is Saturday")
else:
    print("Today is Sunday")

# Example 5
print(" *** Example 5 *** ")
min_age = 18
max_age = 65
actual_age = 24

if actual_age >= 18 and actual_age <= 65:

    print("Person is allowed to work")

else:
    print("Person isn't allowed to work")

# Example 6
print(" *** Example 6 *** ")

country = "Germany"

if country =="Colombia" or country=="España" or country=="México":
    print(f"In {country} the spanish is the main language")
else:
    print(f"In {country} the spanish isn't the main language.")