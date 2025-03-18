class AddressBook:
    def __init__(self):
        self.contacts = {}  # Dictionary to store contacts by phone number

    def add_contact(self, contact_obj):
        if contact_obj.phonenum in self.contacts:
            print("\nContact with this phone number already exists!")
        else:
            self.contacts[contact_obj.phonenum] = contact_obj
            print("\nContact Added Successfully!")

    def print_address(self):
        if not self.contacts:
            print("\nAddress Book is empty!")
        else:
            for key, value in self.contacts.items():
                print(value)
