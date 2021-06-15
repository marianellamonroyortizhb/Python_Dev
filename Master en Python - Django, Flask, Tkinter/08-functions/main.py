"""""
Function: 
A block of instructions than can be used many times.

def fuctionName(parameters):
    Instructions
"""""
# Example 1 - Define and call a fuction
print(" *** Example 1 *** ")

def printDay():
    print("Monday")
    print("Tuesday")
    print("Wednesday")
    print("Thursday")
    print("Friday")
    print("Saturday")
    print("Sunday")

printDay()
print("")

# Example 2 - Call a function many times
print(" *** Example 2 *** ")

def showDay(day):
    print(f"Today is: {day}")

showDay("Monday")
showDay("Tuesday")
showDay("Wednesday")
showDay("Thursday")
showDay("Friday")
showDay("Saturday")
showDay("Sunday")
print("")

# Example 3 - Print user's data
print(" *** Example 3 *** ")

def showName(name, age):
    print(f"Welcome {name}")

    if age >= 18:
        print("You are of legal age.\n")
    else: 
        print("You are young.\n")

name = input("What is your name?: ")
age = int(input("How old are you?: "))
showName(name, age)
print("")

# Example 4 - Multiplication Tables using functions.
print(" *** Example 4 *** \n")

def table(number):
    print(f"Multiplication Table of {number}\n")

    for count in range (0,11):
        mult = number * count
        print (f"{number} X {count} = {mult}")

number = int(input("Write a number: "))
print("")
table(number)
print("")

# Example 5 - For of a function
print(" *** Example 5 *** \n")

for number_count in range (1,11):
    table(number_count)
    print("")

# Example 6 - Default parameters
print(" *** Example 6 *** \n")

def getPersonalData(name_user, id_user = None):
    print("Personal Info")
    print(f"Name: {name_user}")

    if id_user != None:
        print(f"ID: {id_user}")

getPersonalData("Marianella Monroy", 12345678)
print("")

# Example 7 - Return
print(" *** Example 7 *** \n")

def gretting(your_name):
    grett = f"Welcome {your_name}"
    return(grett)

print(gretting("Marianella"))
print("")

# Example 8 - Calculator
print(" *** Example 8 *** \n")

def calculator (numb1, numb2, operator = None):
    operation =  numb1 + operator + numb2
    result = eval(operation)
    print(f"Result: {numb1} {operator} {numb2} = {result}")

numb1 = input("Write the first number: ")
numb2 = input("Write the second number: ")
operator = input("Write the operator: ")

calculator(numb1, numb2, operator)
print("")

# Example 9 - Function inside another one.
print(" *** Example 9 *** \n")

def getname(firstname):
    user_name = f"Your firstname: {firstname}"
    return user_name

def getlastname(lastname):
    user_lastname = f"Your lastname: {lastname}"
    return user_lastname

def getallname(firstname, lastname):
    all_name = f"Your name: {firstname} {lastname}"
    return all_name
firstname = input("What is your firstname?: ")
lastname = input("What is your lastname?: ")

print(getname(firstname))
print(getlastname(lastname))
print(getallname(firstname, lastname))
print("")

# Example 10 - Lambda Function
print(" *** Example 10 *** \n")

this_year = lambda year: f"The year is {year}" 

print(this_year(2021))
