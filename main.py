from addressbookmain import AddressBookMain
from contacts import Contacts
from validations import validate_data

def main():
    system = AddressBookMain()
    system.current_book = None

    while True:
        print("\n--- Address Book System Menu ---")
        print("1. Create New Address Book")
        print("2. Switch Address Book")
        print("3. List Address Books")
        print("4. Add Contact")
        print("5. Display Contacts")
        print("6. Edit Contact")
        print("7. View Persons by City")
        print("8. View Persons by State")
        print("9. Get Contact Count by City")
        print("10. Get Contact Count by State")
        print("11. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            book_name = input("Enter a unique name for the Address Book: ").strip()
            system.add_address_book(book_name)

        elif choice == "2":
            book_name = input("Enter the name of the Address Book to switch: ").strip()
            selected_book = system.select_address_book(book_name)
            if selected_book:
                system.current_book = selected_book
                print(f"\nSwitched to Address Book: {book_name}")

        elif choice == "3":
            system.display_address_books()

        elif choice in ["4", "5", "6", "7", "8", "9", "10"]:
            if not system.current_book:
                print("\nNo Address Book selected! Please create or switch first.")
                continue

            if choice == "4":
                try:
                    user_data = {key: input(f"Enter {key.replace('_', ' ').title()}: ").strip() for key in
                                 ["fname", "lname", "address", "city", "state", "zip_code", "phonenum", "email"]}
                    validated_data = validate_data(user_data)
                    contact = Contacts(**validated_data)
                    system.current_book.add_contact(contact)
                except ValueError as e:
                    print(f"\nValidation Error:\n{e}")

            elif choice == "5":
                system.current_book.print_address()

            elif choice == "6":
                system.current_book.edit_contact(input("Enter First Name: ").strip(), input("Enter Last Name: ").strip())

            elif choice == "7":
                system.current_book.view_by_city(input("Enter City: ").strip())

            elif choice == "8":
                system.current_book.view_by_state(input("Enter State: ").strip())

            elif choice == "9":
                system.current_book.count_by_city(input("Enter City: ").strip())

            elif choice == "10":
                system.current_book.count_by_state(input("Enter State: ").strip())

        elif choice == "11":
            print("\nExiting Address Book System...")
            break

if __name__ == "__main__":
    main()
