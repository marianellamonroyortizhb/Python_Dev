"""
Dictionary:
Collection of data in key-value format. Similar to a json object.
"""

userInfo = {
    "firstname": "Marianella",
    "lastname": "Monroy Ortiz",
    "email": "marianellamonroyortiz@gmail.com"
}

print(userInfo)
print(type(userInfo))

print(userInfo["lastname"])

# List with dictionaries
contacts = [
    {
        "firstname": "Marianella",
        "email": "marianellamonroyortiz@gmail.com"
    },
    
    {
        "firstname": "Ana Maria",
        "email": "anamaria@gmail.com"
    },
    
    {
        "firstname": "Vanessa",
        "email": "vanessa@gmail.com"
    }
]
print(contacts)
print(contacts[2]['email'])

contacts[2]['email']="vanessamonroy@gmail.com"
print(contacts)
print("\n**** Contacts List ****\n")
for contact in contacts:
    print(f"Name: {contact['firstname']}")
    print(f"Email: {contact['email']}")
    print()