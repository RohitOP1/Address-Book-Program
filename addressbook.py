import csv
import os
import json
from collections import defaultdict
from contacts import Contacts  

class AddressBook:
    def __init__(self, name):
        """Initialize Address Book and ensure corresponding CSV and JSON folders exist."""
        self.name = name
        self.contacts = {}  # key: phone number, value: Contacts object
        self.city_person_map = defaultdict(list)
        self.state_person_map = defaultdict(list)

        # Ensure 'data/csv' and 'data/json' folders exist
        os.makedirs("data/csv", exist_ok=True)
        os.makedirs("data/json", exist_ok=True)

        # File paths for CSV and JSON storage
        self.csv_filename = f"data/csv/{self.name}.csv"
        self.json_filename = f"data/json/{self.name}.json"

        # Ensure the CSV file exists
        if not os.path.exists(self.csv_filename):
            self.create_csv()

        self.load_from_csv()

    def create_csv(self):
        """Creates a new CSV file for the Address Book."""
        with open(self.csv_filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["First Name", "Last Name", "Address", "City", "State", "ZIP", "Phone", "Email"])
        print(f"\n New Address Book '{self.name}' created: {self.csv_filename}")

    def add_contact(self, contact_obj):
        """Add a contact to the address book and save it automatically."""
        if contact_obj.phonenum in self.contacts:
            print("\n⚠ Contact with this phone number already exists!")
            return

        for existing_contact in self.contacts.values():
            if (existing_contact.fname.lower() == contact_obj.fname.lower() and
                existing_contact.lname.lower() == contact_obj.lname.lower()):
                print(f"\n⚠ {contact_obj.fname} {contact_obj.lname} is already in '{self.name}' Address Book.")
                return

        # Add contact to dictionaries
        self.contacts[contact_obj.phonenum] = contact_obj
        self.city_person_map[contact_obj.city].append(contact_obj)
        self.state_person_map[contact_obj.state].append(contact_obj)

        # Save to CSV and JSON after adding
        self.save_to_csv()
        self.save_to_json()
        print("\n Contact Added Successfully!")

    def remove_contact(self, phone_number):
        """Remove a contact from the address book."""
        if phone_number in self.contacts:
            contact = self.contacts.pop(phone_number)
            self.city_person_map[contact.city].remove(contact)
            self.state_person_map[contact.state].remove(contact)

            # Save changes after removing
            self.save_to_csv()
            self.save_to_json()
            print(f"\n Contact '{contact.fname} {contact.lname}' removed successfully!")
        else:
            print("\n⚠ Contact not found!")

    def print_address(self):
        """Display all contacts."""
        if not self.contacts:
            print("\n⚠ Address Book is empty!")
        else:
            print(f"\n --- Address Book: {self.name} ---")
            for contact in self.contacts.values():
                print(contact)

    def save_to_csv(self):
        """Save contacts to a CSV file."""
        if not self.contacts:
            print("No contacts to save!")
            return

        try:
            with open(self.csv_filename, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["First Name", "Last Name", "Address", "City", "State", "ZIP", "Phone", "Email"])

                for contact in self.contacts.values():
                    writer.writerow([contact.fname, contact.lname, contact.address, contact.city,
                                     contact.state, contact.zip_code, contact.phonenum, contact.email])

            print(f"\n Contacts saved to CSV: {self.csv_filename}")

        except Exception as e:
            print(f"\n Error saving to CSV: {e}")

    def save_to_json(self):
        """Save contacts to a JSON file."""
        contacts_list = [
            {
                "First Name": contact.fname, "Last Name": contact.lname, "Address": contact.address,
                "City": contact.city, "State": contact.state, "ZIP": contact.zip_code,
                "Phone": contact.phonenum, "Email": contact.email
            }
            for contact in self.contacts.values()
        ]

        try:
            with open(self.json_filename, "w") as file:
                json.dump(contacts_list, file, indent=4)

            print(f"\n Contacts saved to JSON: {self.json_filename}")

        except Exception as e:
            print(f"\n Error saving to JSON: {e}")

    def load_from_csv(self):
        """Load contacts from a CSV file."""
        if not os.path.exists(self.csv_filename):
            return

        try:
            with open(self.csv_filename, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    contact = Contacts(
                        fname=row["First Name"], lname=row["Last Name"], address=row["Address"],
                        city=row["City"], state=row["State"], zip_code=row["ZIP"],
                        phonenum=row["Phone"], email=row["Email"]
                    )
                    self.contacts[contact.phonenum] = contact
                    self.city_person_map[contact.city].append(contact)
                    self.state_person_map[contact.state].append(contact)

            print(f"\n Contacts loaded from CSV: {self.csv_filename}")

        except Exception as e:
            print(f"\n Error loading contacts: {e}")

    def sort_by_city(self):
        """Sort contacts by city name."""
        if not self.contacts:
            print("\n⚠ No contacts to sort!")
            return
        sorted_contacts = sorted(self.contacts.values(), key=lambda c: c.city.lower())
        print(f"\n --- Contacts Sorted by City ---")
        for contact in sorted_contacts:
            print(contact)

    def sort_by_state(self):
        """Sort contacts by state name."""
        if not self.contacts:
            print("\n⚠ No contacts to sort!")
            return
        sorted_contacts = sorted(self.contacts.values(), key=lambda c: c.state.lower())
        print(f"\n --- Contacts Sorted by State ---")
        for contact in sorted_contacts:
            print(contact)

    def sort_by_zip(self):
        """Sort contacts by ZIP Code."""
        if not self.contacts:
            print("\n⚠ No contacts to sort!")
            return
        sorted_contacts = sorted(self.contacts.values(), key=lambda c: c.zip_code)
        print(f"\n --- Contacts Sorted by ZIP Code ---")
        for contact in sorted_contacts:
            print(contact)

    def count_by_city(self, city):
        """Count contacts by city."""
        count = len(self.city_person_map[city])
        print(f"\n Number of contacts in City '{city}': {count}")
        return count

    def count_by_state(self, state):
        """Count contacts by state."""
        count = len(self.state_person_map[state])
        print(f"\n Number of contacts in State '{state}': {count}")
        return count
