from contacts import Contacts
from validations import validate_data

class AddressBook:
    def __init__(self, name):
        self.name = name  
        self.contacts = {}  

    def add_contact(self, contact_obj):
        # Check if contact with the same phone number exists
        if contact_obj.phonenum in self.contacts:
            print("\nContact with this phone number already exists!")
            return
        
        # Check if contact with the same name exists
        for existing_contact in self.contacts.values():
            if (existing_contact.fname.lower() == contact_obj.fname.lower() and
                existing_contact.lname.lower() == contact_obj.lname.lower()):
                print(f"\n{contact_obj.fname} {contact_obj.lname} is already in '{self.name}' Address Book.")
                return

        # Add contact if it doesn't exist
        self.contacts[contact_obj.phonenum] = contact_obj
        print("\nContact Added Successfully!")

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

                    
                    if validated_data["phonenum"] != contact.phonenum:
                        del self.contacts[key]  #old
                        self.contacts[validated_data["phonenum"]] = Contacts(**validated_data)  # Add new entry
                    else:
                        self.contacts[key] = Contacts(**validated_data) 

                    print("\nContact Updated Successfully!")

                except ValueError as e:
                    print(f"\nValidation Error:\n{e}")
                return  

        print("\nContact not found!")
