"""
Exercise 4
Write a script with 4 variables (list, string, int, boolean), and print a text depending of the type.
"""
print("Exercise 4")
mylist = ['Monday','Tuesday','Wednesday','Thursday','Friday']

mystring = "It's July"

myint = 29

myboolean = True

def typefunction(element):
    typeElement = type(element)
    if typeElement == list:
        result = print("It's a list:")
    elif typeElement == str:
        result = print("It's a string:")
    elif typeElement == int:
        result = print("It's an integer:")
    else:
        result = print("It's a boolean:")
    print(element)
    return result

typefunction(mylist)
typefunction(myboolean)
typefunction(mystring)
typefunction(myint)
