import json
import os


def load_contacts():
    if os.path.exists("contacts.json"):
        with open("contacts.json", "r") as file:
            return json.load(file)
    return {}

contacts = load_contacts()
def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)
def delete_contacts():
    name = input("Enter contact to delete: ")

    if name in contacts:
        del contacts[name]
        save_contacts()
        print("Contact deleted.")
    else:
        print("Contact not found.")
