from addressbook import AddressBook
# from collection  import Collection

class AddressBookMain:
    def __init__(self):
        self.address_books = {}
        self.current_book = None  

    def add_address_book(self, name):
        if name in self.address_books:
            print(f"\n '{name}' Address Book already exists.")
        else:
            self.address_books[name] = AddressBook(name)
            print(f"\n '{name}' Address Book created successfully!")

    def display_address_books(self):
        if not self.address_books:
            print("\n No Address Books available.")
        else:
            print("\n Available Address Books:")
            for name in self.address_books.keys():
                print(f"- {name}")

    def select_address_book(self, name):
        if name in self.address_books:
            return self.address_books[name]
        print(f"\n '{name}' Address Book not found!")
        return None

class SearchAddressBook(AddressBookMain):
    def search_person_by_location(self, location):
        found = False
        print(f"\n Searching for contacts in '{location}' across all Address Books...\n")
        
        for address_book in self.address_books.values():
            for contact in address_book.contacts.values():
                if location.lower() in (contact.city.lower(), contact.state.lower()):
                    print(f" Found in '{address_book.name}' Address Book:\n{contact}\n{'-' * 40}")
                    # print(f"\n Found {contact.fname} {contact.lname} in '{address_book.name}' Address Book.")
                    found = True

        if not found:
            print(f"\n No contacts found for '{location}'.")
