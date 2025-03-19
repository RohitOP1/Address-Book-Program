from addressbook import AddressBook

class AddressBookMain:
    """This class is used to create and manage multiple address books."""
    
    def __init__(self):
        self.address_books = {}  # Dictionary to store multiple address books

    def add_address_book(self, name):
        """Creates a new address book."""
        if name in self.address_books:
            print(f"\n'{name}' Address Book already exists.")
        else:
            self.address_books[name] = AddressBook(name)
            print(f"\n'{name}' Address Book created successfully!")

    def display_address_books(self):
        """Displays all the available address books."""
        if not self.address_books:
            print("\nNo Address Books available.")
        else:
            print("\nAvailable Address Books:")
            for name in self.address_books.keys():
                print(f"- {name}")

    def select_address_book(self, name):
        """Selects an address book to work with."""
        if name in self.address_books:
            return self.address_books[name]
        print(f"\n'{name}' Address Book not found!")
        return None

    def delete_address_book(self, name):
        """Deletes an address book."""
        if name in self.address_books:
            del self.address_books[name]
            print(f"\n'{name}' Address Book deleted successfully!")
        else:
            print(f"\n'{name}' Address Book not found!")