from contacts import Contacts
from validations import validate_data
from collections import defaultdict

class AddressBook:
    def __init__(self, name):
        self.name = name
        self.contacts = {}  # key: phone number, value: Contacts object
        self.city_person_map = defaultdict(list)
        self.state_person_map = defaultdict(list)

    def add_contact(self, contact_obj):
        if contact_obj.phonenum in self.contacts:
            print("\nContact with this phone number already exists!")
            return

        for existing_contact in self.contacts.values():
            if (existing_contact.fname.lower() == contact_obj.fname.lower() and
                existing_contact.lname.lower() == contact_obj.lname.lower()):
                print(f"\n{contact_obj.fname} {contact_obj.lname} is already in '{self.name}' Address Book.")
                return

        self.contacts[contact_obj.phonenum] = contact_obj
        self.city_person_map[contact_obj.city].append(contact_obj)
        self.state_person_map[contact_obj.state].append(contact_obj)
        print("\nContact Added Successfully!")

    def print_address(self):
        if not self.contacts:
            print("\nAddress Book is empty!")
        else:
            sorted_contacts = sorted(self.contacts.values(), key=lambda c: (c.fname.lower(), c.lname.lower())) #sort Alphabetically
            print(f"\n--- Address Book: {self.name} (Sorted Alphabetically) ---")
            for contact in sorted_contacts:
                print(contact)

    def edit_contact(self, first_name, last_name):
        for key, contact in list(self.contacts.items()):
            if contact.fname.lower() == first_name.lower() and contact.lname.lower() == last_name.lower():
                print(f"\nEditing Contact: {contact}")

                if contact in self.city_person_map[contact.city]:
                    self.city_person_map[contact.city].remove(contact)
                if contact in self.state_person_map[contact.state]:
                    self.state_person_map[contact.state].remove(contact)

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
                    del self.contacts[key]
                    updated_contact = Contacts(**validated_data)
                    self.contacts[validated_data["phonenum"]] = updated_contact

                    self.city_person_map[updated_contact.city].append(updated_contact)
                    self.state_person_map[updated_contact.state].append(updated_contact)
                    print("\nContact Updated Successfully!")
                except ValueError as e:
                    print(f"\nValidation Error:\n{e}")
                return

        print("\nContact not found!")
