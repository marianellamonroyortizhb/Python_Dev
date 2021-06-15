"""
WHILE LOOP

while condition:
    instructions
    counter update

"""
# Example 1 - While 
print(" *** Example 1 *** ")

count = 1
numbers= str(0)
while count <= 40:
    numbers = numbers + ", " + str(count)
    count = count + 1
print(numbers)
print("\n")

# Example 2 -
print(" *** Example 2 *** ")
number_select = (input("Write a number lower than 10: "))
int_number_select = int(number_select)

if int_number_select < 1:
    print("Please write a positive number")
    number_select = (input("Write a number lower than 10: "))
int_number_select = int(number_select)
print("\n")


print("Multiplication table of " + number_select)
print("-------------------------------")

number_counter = 0

if int_number_select < 10:
    while number_counter <= 10:
        print(f"{number_select} x {number_counter} = {int_number_select * number_counter}")
        number_counter = number_counter + 1 
else:
    print("The number is greater than 10. Sorry, I can't resolve it.")
print("\n")

