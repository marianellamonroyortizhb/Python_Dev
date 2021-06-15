"""
Local Variables:
They are defined inside the fuction and just work inside it

Global Variables:
The are are defined outside the function and can be use inside or outside.
"""
# Example 1 - Global and Local Variables.
print(" *** Example 1 *** \n")

greeting_global = "Hello Global"
print(greeting_global)

def helloLocal():
    greeting_local = "Hello Local"
    print(greeting_local)

    # Define a global variable inside the fuction.
    global month
    month = "June"
    print(f"Inside: {month}")

    year = 2021
    # Lets use the value of a fuction outside.
    return year

helloLocal()
print(helloLocal())
print(f"Outside: {month}")