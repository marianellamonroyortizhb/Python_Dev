name = "Marianella Monroy"

# print()
print(name)

# type()
print(type(name))

# isinstance(): Returns True if the object is of the specified type.
print(isinstance(name, int))

# strip(): It's a method that removes spaces
quote = "   Erase the spaces  "
print(quote)
print(quote.strip())

# del : Deletes a variable
year = 2021
print(year)
del year
# print(year)

# len(): Lenght of item in and object
print(f"Lenght of quote: {len(quote)}")

# find(): Search.
print(quote.find("spaces"))

# replace(): Changes the occurences.
print(quote.replace("the","all the"))

# lower() and upper()
print(name)
print(name.lower())
print(name.upper())