from contact_manager import( add_contacts,
                             delete_contacts,
                             search_contacts,
                             show_contacts)

while True:

    print("\n===== CONTACT MANAGER =====")

    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Search Contact")
    print("4. Show Contacts")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_contacts()

    elif choice == "2":
        delete_contacts()

    elif choice == "3":
        search_contacts()

    elif choice == "4":
        show_contacts()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
