# None type
nothing = None
print(nothing)
print(type(nothing))

# String type
text="Hello everyone"
print(text)
print(type(text))

# Integer type
number = 1992
print(number)
print(type(number))

# Float type
decimal = 3.1415
print(decimal)
print(type(decimal))

# Complex type
compx = 2j
print(compx)
print(type(compx))

# Boolean type
boolean = True
print(boolean)
print(type(boolean))

# List type
list_num = [10, 20, 30, 40]
list_mix = ["January", 1, "February", 2]
print(list_num)
print(type(list_num))
print(list_mix)
print(type(list_mix))

# Tuple type (Is like a list, but data can't be changed)
tuple = ("Marianella", "Monroy", "Ortiz", 29)
print(tuple)
print(type(tuple))

# Dictionary type (Associated data collection in Key : Value)
dict = {
    "name" : "Marianella",
    "lastname" : "Monroy", 
    "birthday": "29"
}
print(dict)
print(type(dict))

# Range type
ran = range(9)
print(ran)
print(type(ran))

# Set type (Is like a tuple, but data can be changed)
set = {"Marianella", "Monroy", "Ortiz", 29}
print(set)
print(type(set))

# Frozenset type (Is like a set, but data can't be changed)
frozen = frozenset({"Monday", "Tuesday", "Friday"})
print(frozen)
print(type(frozen))

# Bytes type
byte_data = b"example"
print(byte_data)
print(type(byte_data))

# Bytearray type
byte_array = bytearray(4)
print(byte_array)
print(type(byte_array))

# Memoryview type
memo = memoryview(bytes(8))
print(memo)
print(type(memo))





