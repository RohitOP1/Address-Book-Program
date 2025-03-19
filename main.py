from addressbookmain import SearchAddressBook
from contacts import Contacts
from validations import validate_data

def main():
    system = SearchAddressBook()  
    system.current_book = None  

    while True:
        print("\n--- Address Book System Menu ---")
        print("1. Create New Address Book")
        print("2. Switch Address Book")
        print("3. List Address Books")
        print("4. Add Contact")
        print("5. Display Contacts")
        print("6. Edit Contact")
        print("7. Search Contact by City/State")
        print("8. Exit")

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

        elif choice in ["4", "5", "6"]:
            if not system.current_book:
                print("\n No Address Book selected! Please create or switch first.")
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
                    print(f"\n Validation Error:\n{e}")

            elif choice == "5":
                system.current_book.print_address()

            elif choice == "6":
                first_name = input("\nEnter First Name of the Contact to Edit: ").strip()
                last_name = input("Enter Last Name of the Contact to Edit: ").strip()
                system.current_book.edit_contact(first_name, last_name)

        elif choice == "7":
            location = input("\nEnter City or State to search: ").strip()
            system.search_person_by_location(location)

        elif choice == "8":
            print("\n Exiting Address Book System...")
            break

        else:
            print("\n Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
