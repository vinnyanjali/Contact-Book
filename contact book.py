class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address,
        }
        self.contacts.append(contact)
        print(f"Contact {name} added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        print("Contact List:")
        for index, contact in enumerate(self.contacts, start=1):
            print(f"{index}. {contact['name']} - {contact['phone']}")

    def search_contact(self, keyword):
        found_contacts = []
        for contact in self.contacts:
            if keyword.lower() in contact["name"].lower() or keyword in contact["phone"]:
                found_contacts.append(contact)
        return found_contacts

    def update_contact(self, index, name, phone, email, address):
        if 0 < index <= len(self.contacts):
            contact = self.contacts[index - 1]
            contact["name"] = name
            contact["phone"] = phone
            contact["email"] = email
            contact["address"] = address
            print("Contact updated successfully!")
        else:
            print("Invalid index. Contact not updated.")

    def delete_contact(self, index):
        if 0 < index <= len(self.contacts):
            deleted_contact = self.contacts.pop(index - 1)
            print(f"Contact {deleted_contact['name']} deleted successfully!")
        else:
            print("Invalid index. Contact not deleted.")


def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_manager.add_contact(name, phone, email, address)

        elif choice == "2":
            contact_manager.view_contacts()

        elif choice == "3":
            keyword = input("Enter name or phone number to search: ")
            found_contacts = contact_manager.search_contact(keyword)
            if found_contacts:
                print("Matching Contacts:")
                for contact in found_contacts:
                    print(contact)
            else:
                print("No matching contacts found.")

        elif choice == "4":
            index = int(input("Enter the index of the contact to update: "))
            name = input("Enter updated name: ")
            phone = input("Enter updated phone number: ")
            email = input("Enter updated email: ")
            address = input("Enter updated address: ")
            contact_manager.update_contact(index, name, phone, email, address)

        elif choice == "5":
            index = int(input("Enter the index of the contact to delete: "))
            contact_manager.delete_contact(index)

        elif choice == "6":
            print("Exiting Contact Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
