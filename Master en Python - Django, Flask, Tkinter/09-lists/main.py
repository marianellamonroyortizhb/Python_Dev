"""
Lists (arrays):
They are data collections. Their values can be accessed by indexes.
"""

# Define a list - Two ways.
movies = ["Batman", "Spiderman", "Superman"]
singers = list(("Shakira", "Dualipa", "Beyonce"))
years = list(range(2020, 2030))
mix = [2.2, True, 'Name']

# Print a list
print(movies)
print(singers)
print(years)
print(mix)

# Print an element
print(movies[1])
print(singers[2])
print(mix[0])
print(years[8])

# Negative index: Start from the last one.
print(movies[-2])

# Print a range
print(years[2:5])

# Print the list from 3
print(years[3:]) 

# Modify a value
movies[2] = "Iron Man"
print(movies)

# Add an element
movies.append("X-Men")
print(movies)

# Print an element per line.
print("**** Superhero Movies ****")

for count in movies:
    print(count)

for count in movies:
    print(f"{movies.index(count) + 1}. {count}")

# Ask movies to append

new_movie = ""
while new_movie != 'stop':
    new_movie = input("Write a new movie: ")

    if new_movie != 'stop':
        movies.append(new_movie)

for counter in movies:
    print(f"{movies.index(counter) + 1}. {counter}")

# Multidimensional list
print("**** Contacts List ****")
contacts = [
    [
        'Ana Maria',
        'anamaria@gmail.com'
    ],

    [
        'Vanessa',
        'vanessa@gmail.com'
    ],
    [
        'Juanita',
        'juanita@gmail.com'
    ],
]
# Print all contact list
print(contacts)
print()

# Print a contact
print(contacts[1])
print()

# Print an email
print(contacts[0][1])
print()

# Print list 
print("**** Contacts List ****")
for contact in contacts:
    for element in contact:
        if contact.index(element) == 0:
            print("Name: " + element)
        else:
            print("Email: " + element)
    print()