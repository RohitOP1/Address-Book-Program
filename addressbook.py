from contacts import Contacts
from validations import validate_data

class AddressBook:
    def __init__(self, name):
        self.name = name
        self.contacts = {}

    def add_contact(self, contact_obj):
        if contact_obj.phonenum in self.contacts:
            print("\n Contact with this phone number already exists!")
            return

        for existing_contact in self.contacts.values():
            if existing_contact.fname.lower() == contact_obj.fname.lower() and existing_contact.lname.lower() == contact_obj.lname.lower():
                print(f"\n {contact_obj.fname} {contact_obj.lname} is already in '{self.name}' Address Book.")
                return

        self.contacts[contact_obj.phonenum] = contact_obj
        print("\n Contact Added Successfully!")

    def print_address(self):
        if not self.contacts:
            print("\nℹ Address Book is empty!")
        else:
            print(f"\n---  Address Book: {self.name} ---")
            for contact in self.contacts.values():
                print(contact)

    def edit_contact(self, first_name, last_name):
        for key, contact in list(self.contacts.items()):
            if contact.fname.lower() == first_name.lower() and contact.lname.lower() == last_name.lower():
                print(f"\n Editing Contact: {contact}")

                new_data = {
                    "fname": input("Enter new First Name: ").strip() or contact.fname,
                    "lname": input("Enter new Last Name: ").strip() or contact.lname,
                    "address": input("Enter new Address: ").strip() or contact.address,
                    "city": input("Enter new City: ").strip() or contact.city,
                    "state": input("Enter new State: ").strip() or contact.state,
                    "zip_code": input("Enter new ZIP Code: ").strip() or contact.zip_code,
                    "phonenum": input("Enter new Phone Number: ").strip() or contact.phonenum,
                    "email": input("Enter new Email: ").strip() or contact.email
                }

                try:
                    validated_data = validate_data(new_data)
                    del self.contacts[key]  # Remove old
                    self.contacts[validated_data["phonenum"]] = Contacts(**validated_data)  
                    print("\n Contact Updated Successfully!")
                except ValueError as e:
                    print(f"\n Validation Error:\n{e}")
                return  

        print("\n Contact not found!")
