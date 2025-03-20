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
        print("5. Display Contacts (Sort & Count Options)")
        print("6. Edit Contact")
        print("7. Exit")

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

        elif choice == "4":
            if not system.current_book:
                print("\nNo Address Book selected! Please create or switch first.")
                continue
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
            if not system.current_book:
                print("\nNo Address Book selected! Please create or switch first.")
                continue

            print("\nOptions:")
            print("1. Display all contacts")
            print("2. Sort by City")
            print("3. Sort by State")
            print("4. Sort by ZIP Code")
            print("5. Count contacts by City")
            print("6. Count contacts by State")

            sort_choice = input("Enter your choice: ").strip()

            if sort_choice == "1":
                system.current_book.print_address()
            elif sort_choice == "2":
                system.current_book.sort_by_city()
            elif sort_choice == "3":
                system.current_book.sort_by_state()
            elif sort_choice == "4":
                system.current_book.sort_by_zip()
            elif sort_choice == "5":
                city = input("Enter City: ").strip()
                system.current_book.count_by_city(city)
            elif sort_choice == "6":
                state = input("Enter State: ").strip()
                system.current_book.count_by_state(state)
            else:
                print("\nInvalid choice! Please try again.")

        elif choice == "6":
            if not system.current_book:
                print("\nNo Address Book selected! Please create or switch first.")
                continue
            fname = input("Enter First Name of the Contact to Edit: ").strip()
            lname = input("Enter Last Name of the Contact to Edit: ").strip()
            system.current_book.edit_contact(fname, lname)

        elif choice == "7":
            print("\nExiting Address Book System...")
            break

        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()
