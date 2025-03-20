from contacts import Contacts
from validations import validate_data
from collections import defaultdict

class AddressBook:
    def __init__(self, name):
        self.name = name
        self.contacts = {}  # key: contact's phone number, value: Contacts object
        # Dictionaries to maintain mapping from city and state to contacts:
        self.city_person_map = defaultdict(list)
        self.state_person_map = defaultdict(list)

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
        # Update city and state maps:
        self.city_person_map[contact_obj.city].append(contact_obj)
        self.state_person_map[contact_obj.state].append(contact_obj)
        print("\nContact Added Successfully!")

    def print_address(self):
        if not self.contacts:
            print("\nAddress Book is empty!")
        else:
            print(f"\n--- Address Book: {self.name} ---")
            for contact in self.contacts.values():
                print(contact)

    def edit_contact(self, first_name, last_name):
        # Look up contact by matching first and last name (case-insensitive)
        for key, contact in list(self.contacts.items()):
            if contact.fname.lower() == first_name.lower() and contact.lname.lower() == last_name.lower():
                print(f"\nEditing Contact: {contact}")

                # Before editing, remove contact from old city/state maps.
                if contact in self.city_person_map[contact.city]:
                    self.city_person_map[contact.city].remove(contact)
                if contact in self.state_person_map[contact.state]:
                    self.state_person_map[contact.state].remove(contact)

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
                    # Remove old entry and add updated contact:
                    del self.contacts[key]
                    updated_contact = Contacts(**validated_data)
                    self.contacts[validated_data["phonenum"]] = updated_contact

                    # Update city and state maps:
                    self.city_person_map[updated_contact.city].append(updated_contact)
                    self.state_person_map[updated_contact.state].append(updated_contact)
                    print("\nContact Updated Successfully!")
                except ValueError as e:
                    print(f"\nValidation Error:\n{e}")
                return

        print("\nContact not found!")

    def view_by_city(self, city):
        if city in self.city_person_map and self.city_person_map[city]:
            print(f"\nContacts in City '{city}':")
            for contact in self.city_person_map[city]:
                print(contact)
        else:
            print(f"\nNo contacts found in City '{city}'.")

    def view_by_state(self, state):
        if state in self.state_person_map and self.state_person_map[state]:
            print(f"\nContacts in State '{state}':")
            for contact in self.state_person_map[state]:
                print(contact)
        else:
            print(f"\nNo contacts found in State '{state}'.")
