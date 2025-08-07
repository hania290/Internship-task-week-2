import json
import os

filename = "phonebook.json"

def load_contacts():
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    with open(filename, "w") as file:
        json.dump(contacts, file, indent=4)

def create_contact(contacts):
    name = input("Enter contact name: ")
    number = input("Enter contact number: ")
    contacts[name] = number
    print("Contact added.")

def read_contacts(contacts):
    if contacts:
        for name, number in contacts.items():
            print(f"{name}: {number}")
    else:
        print("Phonebook is empty.")

def update_contact(contacts):
    name = input("Enter the name to update: ")
    if name in contacts:
        number = input("Enter new number: ")
        contacts[name] = number
        print("Contact updated.")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter the name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

def main():
    contacts = load_contacts()

    while True:
        print("\n--- Phonebook Menu ---")
        print("1. Create Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            create_contact(contacts)
        elif choice == "2":
            read_contacts(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            save_contacts(contacts)
            print("Contacts saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()