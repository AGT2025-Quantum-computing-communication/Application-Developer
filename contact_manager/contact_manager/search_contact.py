def search_contacts():
    name = input("Enter contact name: ")

    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found.")
