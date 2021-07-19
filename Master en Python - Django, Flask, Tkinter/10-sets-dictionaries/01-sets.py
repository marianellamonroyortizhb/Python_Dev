"""
Set:
Collection of values, without order or index.
"""

people = {
    "Juan David",
    "Samuel",
    "Daniela"
}
print(people)
print(type(people))

people.add("Alejandra")
people.remove("Samuel")
print(people)
