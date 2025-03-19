from addressbook import AddressBook
from contacts import Contacts
from validations import validate_data

class AddressBookSystem:
    def __init__(self):
        self.address_books = {}  # Stores multiple address books
        self.current_book = None

    def create_address_book(self, name):
        if name in self.address_books:
            print("\nAn Address Book with this name already exists!")
        else:
            self.address_books[name] = AddressBook(name)
            self.current_book = self.address_books[name]  # Set as active
            print(f"\nAddress Book '{name}' created and selected.")

    def switch_address_book(self, name):
        if name in self.address_books:
            self.current_book = self.address_books[name]
            print(f"\nSwitched to Address Book '{name}'.")
        else:
            print("\nAddress Book not found!")

    def list_address_books(self):
        if not self.address_books:
            print("\nNo Address Books available.")
        else:
            print("\nAvailable Address Books:")
            for name in self.address_books.keys():
                print(f"- {name}")

def main():
    system = AddressBookSystem()

    while True:
        print("\n--- Address Book System Menu ---")
        print("1. Create New Address Book")
        print("2. Switch Address Book")
        print("3. List Address Books")
        print("4. Add Contact")
        print("5. Display Contacts")
        print("6. Edit Contact")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            book_name = input("Enter a unique name for the Address Book: ").strip()
            system.create_address_book(book_name)

        elif choice == "2":
            book_name = input("Enter the name of the Address Book to switch: ").strip()
            system.switch_address_book(book_name)

        elif choice == "3":
            system.list_address_books()

        elif choice in ["4", "5", "6"]:
            if system.current_book is None:
                print("\nNo Address Book selected! Create or switch first.")
                continue

            if choice == "4":
                try:
                    user_data = {
                        "fname": input("Enter First Name: ").strip(),
                        "lname": input("Enter Last Name: ").strip(),
                        "address": input("Enter Address: ").strip(),
                        "city": input("Enter City: ").strip(),
                        "state": input("Enter State: ").strip(),
                        "zip_code": input("Enter ZIP Code: ").strip(),
                        "phonenum": input("Enter Phone Number: ").strip(),
                        "email": input("Enter Email: ").strip()
                    }

                    validated_data = validate_data(user_data)
                    contact = Contacts(**validated_data)
                    system.current_book.add_contact(contact)

                except ValueError as e:
                    print(f"\nValidation Error:\n{e}")

            elif choice == "5":
                system.current_book.print_address()

            elif choice == "6":
                first_name = input("\nEnter First Name of the Contact to Edit: ").strip()
                last_name = input("Enter Last Name of the Contact to Edit: ").strip()
                system.current_book.edit_contact(first_name, last_name)

        elif choice == "7":
            print("\nExiting Address Book System...")
            break

        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()
