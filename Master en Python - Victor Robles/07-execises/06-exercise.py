"""
Exercise 5
    - Show the multiplication tables from 1 to 10.
"""
print("Exercise 5 - Multiplication Tables")
result = 0

for table_number in range (1,11):
    print("Table of number " + str(table_number))
    print("--------------------")
    for mult in range (1,11):
        result = table_number * mult
        print(str(table_number) + " X " + str(mult) + " = " + str(result))
        mult = mult + 1
    print("")