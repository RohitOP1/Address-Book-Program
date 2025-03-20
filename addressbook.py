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
        """Display all contacts."""
        if not self.contacts:
            print("\nAddress Book is empty!")
        else:
            print(f"\n--- Address Book: {self.name} ---")
            for contact in self.contacts.values():
                print(contact)

    #  Function to sort by City
    def sort_by_city(self):
        if not self.contacts:
            print("\nNo contacts to sort!")
            return
        sorted_contacts = sorted(self.contacts.values(), key=lambda c: c.city.lower())
        print(f"\n--- Contacts in '{self.name}' Sorted by City ---")
        for contact in sorted_contacts:
            print(contact)

    #  Function to sort by State
    def sort_by_state(self):
        if not self.contacts:
            print("\nNo contacts to sort!")
            return
        sorted_contacts = sorted(self.contacts.values(), key=lambda c: c.state.lower())
        print(f"\n--- Contacts in '{self.name}' Sorted by State ---")
        for contact in sorted_contacts:
            print(contact)

    # Function to sort by ZIP Code
    def sort_by_zip(self):
        if not self.contacts:
            print("\nNo contacts to sort!")
            return
        sorted_contacts = sorted(self.contacts.values(), key=lambda c: c.zip_code)
        print(f"\n--- Contacts in '{self.name}' Sorted by ZIP Code ---")
        for contact in sorted_contacts:
            print(contact)

    #   Count contacts by City
    def count_by_city(self, city):
        count = len(self.city_person_map[city])
        print(f"\nNumber of contacts in City '{city}': {count}")
        return count

    #  Count contacts by State
    def count_by_state(self, state):
        count = len(self.state_person_map[state])
        print(f"\nNumber of contacts in State '{state}': {count}")
        return count
