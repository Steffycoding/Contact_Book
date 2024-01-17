import sqlite3
from colorama import Fore, Style

# Function to create a database and table
def create_table():
    """Create 'contacts' table if it doesn't exist."""
    connection = sqlite3.connect("contacts.db")
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            address TEXT,
            phone_number TEXT,
            email TEXT
        )
    ''')

    connection.commit()
    connection.close()

# Function to add a new contact
def add_contact(name, address, phone_number, email):
    """Add a new contact to the 'contacts' table."""
    connection = sqlite3.connect("contacts.db")
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO contacts (name, address, phone_number, email)
        VALUES (?, ?, ?, ?)
    ''', (name, address, phone_number, email))

    connection.commit()
    connection.close()

# Function to edit an existing contact
def edit_contact(contact_id, name, address, phone_number, email):
    """Edit an existing contact in the 'contacts' table."""
    connection = sqlite3.connect("contacts.db")
    cursor = connection.cursor()

    cursor.execute('''
        UPDATE contacts
        SET name=?, address=?, phone_number=?, email=?
        WHERE id=?
    ''', (name, address, phone_number, email, contact_id))

    connection.commit()
    connection.close()

# Function to delete a contact
def delete_contact(contact_id):
    """Delete a contact from the 'contacts' table."""
    connection = sqlite3.connect("contacts.db")
    cursor = connection.cursor()

    cursor.execute('''
        DELETE FROM contacts
        WHERE id=?
    ''', (contact_id,))

    connection.commit()
    connection.close()

# Function to display all contacts
def display_contacts():
    """Display all contacts from the 'contacts' table."""
    connection = sqlite3.connect("contacts.db")
    cursor = connection.cursor()

    cursor.execute('''
        SELECT * FROM contacts
    ''')

    contacts = cursor.fetchall()

    if not contacts:
        print(Fore.RED + "No contacts found." + Style.RESET_ALL)
    else:
        print(Fore.MAGENTA + "Contacts:" + Style.RESET_ALL)
        for index, contact in enumerate(contacts, start=1):
            color = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.LIGHTBLUE_EX, Fore.MAGENTA, Fore.CYAN]
            print(color[index % len(color)] +
                  f"ID: {contact[0]}, Name: {contact[1]}, Address: {contact[2]}, Phone: {contact[3]}, Email: {contact[4]}" +
                  Style.RESET_ALL)

    connection.close()

# Main function to run the Contact Book application
def main():
    """Main function to execute the Contact Book application."""
    create_table()

    while True:
        print(Fore.MAGENTA + "\nContact Book Menu:" + Style.RESET_ALL)
        print(Fore.YELLOW + "1. Add Contact")
        print("2. Edit Contact")
        print("3. Delete Contact")
        print("4. Display Contacts")
        print("5. Exit" + Style.RESET_ALL)

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter Name: ")
            address = input("Enter Address: ")
            phone_number = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            add_contact(name, address, phone_number, email)
            print(Fore.GREEN + "Contact added successfully!" + Style.RESET_ALL)

        elif choice == "2":
            contact_id = input("Enter Contact ID to edit: ")
            name = input("Enter New Name: ")
            address = input("Enter New Address: ")
            phone_number = input("Enter New Phone Number: ")
            email = input("Enter New Email: ")
            edit_contact(contact_id, name, address, phone_number, email)
            print(Fore.GREEN + "Contact edited successfully!" + Style.RESET_ALL)

        elif choice == "3":
            contact_id = input("Enter Contact ID to delete: ")
            delete_contact(contact_id)
            print(Fore.GREEN + "Contact deleted successfully!" + Style.RESET_ALL)

        elif choice == "4":
            display_contacts()

        elif choice == "5":
            print(Fore.YELLOW + "Goodbye!" + Style.RESET_ALL)
            break

        else:
            print(Fore.RED + "Invalid choice. Please enter a number between 1 and 5." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
