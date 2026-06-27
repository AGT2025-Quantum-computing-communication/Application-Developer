
import logging
import json
import os

logging.basicConfig(
    filename="contacts.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# begin####################
'''This print out the error message in the file created above called contact.log'''
logging.basicConfig(level=logging.ERROR)



#contacts = {"Alain": "683925986","Kams": "696404836"}
# end#########################


def load_contacts():
    if os.path.exists("contacts.json"):
        with open("contacts.json", "r") as file:
            return json.load(file)

    return {}

contacts = load_contacts()

def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)


def add_contacts():
    try:
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        city = input("City: ")

        contacts[name] = {
        "phone": phone,
        "email": email,
        "city": city
        }
        save_contacts()
        print(f"Added {name} succesfully")
    except Exception:
        logging.exception("An error occurred")

    logging.info(f"Contact added: {name}")
