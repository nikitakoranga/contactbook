import sqlite3
import os

# Database initialization
def init_db():
    conn = sqlite3.connect("contact.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Add contact
def add_contact(name, phone, email):
    conn = sqlite3.connect("contact.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
    conn.commit()
    conn.close()
    print("✅ Contact added successfully!\n")

# View all contacts
def view_contacts():
    conn = sqlite3.connect("contact.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    conn.close()

    if contacts:
        for contact in contacts:
            print(f"ID: {contact[0]} | Name: {contact[1]} | Phone: {contact[2]} | Email: {contact[3]}")
    else:
        print("⚠️ No contacts found.")
    print()

# Search contact by name
def search_contact(name):
    conn = sqlite3.connect("contact.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts WHERE name LIKE ?", ('%' + name + '%',))
    contacts = cursor.fetchall()
    conn.close()

    if contacts:
        for contact in contacts:
            print(f"ID: {contact[0]} | Name: {contact[1]} | Phone: {contact[2]} | Email: {contact[3]}")
    else:
        print("❌ No matching contact found.")
    print()

# Delete contact by ID
def delete_contact(contact_id):
    conn = sqlite3.connect("contact.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
    conn.commit()
    conn.close()
    print("🗑️ Contact deleted successfully!\n")

# Update contact by ID
def update_contact(contact_id, name, phone, email):
    conn = sqlite3.connect("contact.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE contacts SET name=?, phone=?, email=? WHERE id=?", (name, phone, email, contact_id))
    conn.commit()
    conn.close()
    print("✏️ Contact updated successfully!\n")

# Main menu
def menu():
    while True:
        print("===== Contact Book Menu =====")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email (optional): ")
            add_contact(name, phone, email)

        elif choice == '2':
            view_contacts()

        elif choice == '3':
            name = input("Enter name to search: ")
            search_contact(name)

        elif choice == '4':
            contact_id = int(input("Enter contact ID to update: "))
            name = input("Enter new name: ")
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            update_contact(contact_id, name, phone, email)

        elif choice == '5':
            contact_id = int(input("Enter contact ID to delete: "))
            delete_contact(contact_id)

        elif choice == '6':
            print("👋 Exiting Contact Book...")
            break

        else:
            print("⚠️ Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    init_db()
    menu()

