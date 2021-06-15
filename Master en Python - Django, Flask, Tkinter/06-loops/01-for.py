"""
FOR LOOP

for item in iteration:
    Instructions

"""
# Example 1
print(" *** Example 1 *** ")

count = 0
result = 0
for count in range(0,4):
    print("This is the iteration " + str(count))
    result += count

print(result)
print("\n")

# Example 2
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

if int_number_select < 10:
    for number_count in range(0,11):
        print(f"{number_select} x {number_count} = {int_number_select * number_count}")
else:
    print("The number is greater than 10. Sorry, I can't resolve it.")
print("\n")
