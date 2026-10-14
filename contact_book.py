import json
import os

FILE_NAME = "contacts.json"


def load_contacts():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return []
    return []


def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()

    if not name or not phone or not email:
        print("All fields are required!")
        return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })

    save_contacts(contacts)
    print("Contact added successfully!")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    print("\n===== ALL CONTACTS =====")

    for index, contact in enumerate(contacts, start=1):
        print(f"\nContact {index}")
        print(f"Name : {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")


def search_contact(contacts):
    name = input("Enter name to search: ").strip().lower()

    found = False

    for contact in contacts:
        if name in contact["name"].lower():
            print("\nContact Found!")
            print(f"Name : {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            found = True

    if not found:
        print("Contact not found.")


def update_contact(contacts):
    name = input("Enter name to update: ").strip().lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            new_name = input("Enter new name (press Enter to skip): ").strip()
            new_phone = input("Enter new phone (press Enter to skip): ").strip()
            new_email = input("Enter new email (press Enter to skip): ").strip()

            if new_name:
                contact["name"] = new_name

            if new_phone:
                contact["phone"] = new_phone

            if new_email:
                contact["email"] = new_email

            save_contacts(contacts)
            print("Contact updated successfully!")
            return

    print("Contact not found.")


def delete_contact(contacts):
    name = input("Enter name to delete: ").strip().lower()

    for index, contact in enumerate(contacts):
        if contact["name"].lower() == name:
            removed = contacts.pop(index)
            save_contacts(contacts)
            print(f"Contact '{removed['name']}' deleted successfully!")
            return

    print("Contact not found.")


def main():
    contacts = load_contacts()

    while True:
        print("\n===== CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            view_contacts(contacts)

        elif choice == "3":
            search_contact(contacts)

        elif choice == "4":
            update_contact(contacts)

        elif choice == "5":
            delete_contact(contacts)

        elif choice == "6":
            print("Thank you for using Contact Book!")
            break

        else:
            print("Invalid choice! Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
