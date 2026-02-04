
contacts = {
    "Mosab": "01090097506",
    "Omar": "01234567891",
    "Ricky": "01121159011"
}
print(contacts.keys())
while 1 :
    search = input("Enter name to search: ")

    if search in contacts:
        print(f"Phone number of {search}: {contacts[search]}")
    else:
        print("Contact not found.")
        break
