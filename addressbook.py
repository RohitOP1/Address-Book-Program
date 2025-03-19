from contacts import Contacts
from validations import validate_data

class AddressBook:
    def __init__(self, name):
        self.name = name  # Unique name for each address book
        self.contacts = {}  

    def add_contact(self, contact_obj):
        if contact_obj.phonenum in self.contacts:
            print("\nContact with this phone number already exists!")
        else:
            self.contacts[contact_obj.phonenum] = contact_obj
            print("\nContact Added Successfully!")
            for existing_contact  in self.contacts.values():
             if existing_contact  ==  contact.full_name:
                 print(f"\n{contact.full_name} is already in '{self.name}' Address Book.")
                 break

    def print_address(self):
        if not self.contacts:
            print("\nAddress Book is empty!")
        else:
            print(f"\n--- Address Book: {self.name} ---")
            for contact in self.contacts.values():
                print(contact)

    def edit_contact(self, first_name, last_name):
        for key, contact in list(self.contacts.items()):
            if contact.fname.lower() == first_name.lower() and contact.lname.lower() == last_name.lower():
                print(f"\nEditing Contact: {contact}")

                new_data = {
                    "fname": input("Enter new First Name (Leave empty to keep current): ").strip() or contact.fname,
                    "lname": input("Enter new Last Name (Leave empty to keep current): ").strip() or contact.lname,
                    "address": input("Enter new Address (Leave empty to keep current): ").strip() or contact.address,
                    "city": input("Enter new City (Leave empty to keep current): ").strip() or contact.city,
                    "state": input("Enter new State (Leave empty to keep current): ").strip() or contact.state,
                    "zip_code": input("Enter new ZIP Code (Leave empty to keep current): ").strip() or contact.zip_code,
                    "phonenum": input("Enter new Phone Number (Leave empty to keep current): ").strip() or contact.phonenum,
                    "email": input("Enter new Email (Leave empty to keep current): ").strip() or contact.email
                }

                try:
                    validated_data = validate_data(new_data) 
                    
                    # If phone number changes
                    if validated_data["phonenum"] != contact.phonenum:
                        del self.contacts[key]  # Remove old entry
                        self.contacts[validated_data["phonenum"]] = Contacts(**validated_data)  # Add new entry
                    else:
                        self.contacts[key] = Contacts(**validated_data) 

                    print("\nContact Updated Successfully!")

                except ValueError as e:
                    print(f"\nValidation Error:\n{e}")
                return  

        print("\nContact not found!")
