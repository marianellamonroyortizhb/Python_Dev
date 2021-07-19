"""
Exercise 3
Program that check if a varible is empty and in that case, fill it with text in lowercase and print it in uppercase.
"""
print("Exercise 3")
test = input("Write something: ")

if len(test.strip()) <= 0:
    test="i used to be a text in lowercase"
    print(test.upper())
else:
    print("You wrote: " + test)