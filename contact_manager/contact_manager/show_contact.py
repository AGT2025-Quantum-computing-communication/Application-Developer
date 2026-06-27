
import json
import os


def load_contacts():
    if os.path.exists("contacts.json"):
        with open("contacts.json", "r") as file:
            return json.load(file)
    return {}

contacts = load_contacts()

def show_contacts():

    if not contacts:
        print("No contacts available.")
        return

    print("\nContacts")

    for name, phone in contacts.items():
        print(f"{name} : {phone}")
