class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, contact_obj):
        self.contacts[contact_obj.phonenum] = contact_obj
        
    def print_address(self):
        for key, value in self.contacts.items():
            print(f"{key}: {value}")

    def edit_contact(self, phonenum):
        if phonenum in self.contacts:
            contact = self.contacts[phonenum]
            print(f"Editing contact: {contact}")
            
            #user for updated details
            contact.fname = input("Enter First Name: ") or contact.fname
            contact.lname = input("Enter Last Name: ") or contact.lname
            contact.address = input("Enter Address: ") or contact.address
            contact.city = input("Enter City: ") or contact.city
            contact.state = input("Enter State: ") or contact.state
            contact.zip_code = input("Enter ZIP Code: ") or contact.zip_code
            contact.email = input("Enter Email: ") or contact.email
            
            print("\nContact updated successfully!")
        else:
            print("Contact not found.")
