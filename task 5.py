import json
import os

CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

# Add new contact
def add_contact(contacts):
    name = input("Enter name: ").strip()
    if name in contacts:
        print("⚠️ Contact with this name already exists!")
        return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()

    contacts[name] = {"phone": phone, "email": email, "address": address}
    save_contacts(contacts)
    print("✅ Contact added successfully!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("📭 No contacts found.")
        return
    print("\n=== Contact List ===")
    for name, details in contacts.items():
        print(f"\nName: {name}")
        print(f"📞 Phone: {details['phone']}")
        print(f"📧 Email: {details['email']}")
        print(f"🏠 Address: {details['address']}")

# Search contact by name or phone
def search_contact(contacts):
    query = input("Enter name or phone number to search: ").strip().lower()
    found = False
    for name, details in contacts.items():
        if query in name.lower() or query in details["phone"]:
            print(f"\nName: {name}")
            print(f"📞 Phone: {details['phone']}")
            print(f"📧 Email: {details['email']}")
            print(f"🏠 Address: {details['address']}")
            found = True
    if not found:
        print("⚠️ Contact not found.")

# Update existing contact
def update_contact(contacts):
    name = input("Enter the contact name to update: ").strip()
    if name in contacts:
        phone = input(f"Enter new phone (leave blank to keep {contacts[name]['phone']}): ").strip()
        email = input(f"Enter new email (leave blank to keep {contacts[name]['email']}): ").strip()
        address = input(f"Enter new address (leave blank to keep {contacts[name]['address']}): ").strip()

        if phone: contacts[name]['phone'] = phone
        if email: contacts[name]['email'] = email
        if address: contacts[name]['address'] = address

        save_contacts(contacts)
        print("✏️ Contact updated successfully!")
    else:
        print("⚠️ Contact not found.")

# Delete contact
def delete_contact(contacts):
    name = input("Enter the contact name to delete: ").strip()
    if name in contacts:
        confirm = input(f"Are you sure you want to delete {name}? (y/n): ").lower()
        if confirm == "y":
            del contacts[name]
            save_contacts(contacts)
            print("🗑️ Contact deleted successfully!")
    else:
        print("⚠️ Contact not found.")

# Main program
def main():
    contacts = load_contacts()

    while True:
        print("\n=== Contact Book Menu ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

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
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
