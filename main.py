from addressbook import AddressBook
from contacts import Contacts
from validations import validate_data

def main():
    address_book = AddressBook()

    while True:
        print("\n--- Address Book Menu ---")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Edit Contact")  
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
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
                address_book.add_contact(contact)

            except ValueError as e:
                print(f"\nValidation Error:\n{e}")

        elif choice == "2":
            print("\n--- Address Book ---")
            address_book.print_address()

        elif choice == "3":
            first_name = input("\nEnter First Name of the Contact to Edit: ").strip()
            last_name = input("Enter Last Name of the Contact to Edit: ").strip()
            address_book.edit_contact(first_name, last_name)

        elif choice == "4":
            print("\nExiting Address Book...")
            break

        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()
