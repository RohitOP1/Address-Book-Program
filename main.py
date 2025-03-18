from contacts import Contacts
from validations import validate_data

def main():
    try:
        # User input
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

        # Validate user input
        validated_data = validate_data(user_data)

        # Create a contact object
        contact = Contacts(**validated_data)  # Unpack dictionary as arguments
        print("\n Contact Added Successfully!\n")
        print(contact)

    except ValueError as e:
        print(f"\n Validation Error:\n{e}")

if __name__ == "__main__":
    main()
