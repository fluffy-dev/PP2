import psycopg2
import csv

conn = psycopg2.connect(
    database="pp2",
    user="postgres",
    password="rauan2530",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    phone VARCHAR(20) UNIQUE
)
""")
conn.commit()

def insert_from_csv(file_path):
    file_path = input("Enter path to CSV file: ")
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                try:
                    cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", row)
                except psycopg2.Error as e:
                    print(f"⚠️ Failed to insert {row}: {e.pgerror.strip()}")
        conn.commit()
        print("✅ CSV import complete.")
    except FileNotFoundError:
        print("❌ CSV file not found.")

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    try:
        cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (name, phone))
        conn.commit()
        print("✅ Contact added.")
    except psycopg2.Error as e:
        print("❌ Error inserting data:", e.pgerror.strip())

def update_contact():
    phone = input("Enter phone of contact to update: ")
    print("1. Change name\n2. Change phone")
    choice = input("Choose option: ")
    if choice == '1':
        new_name = input("Enter new name: ")
        cur.execute("UPDATE phonebook SET first_name = %s WHERE phone = %s", (new_name, phone))
    elif choice == '2':
        new_phone = input("Enter new phone: ")
        cur.execute("UPDATE phonebook SET phone = %s WHERE phone = %s", (new_phone, phone))
    else:
        print("❌ Invalid option.")
        return
    conn.commit()
    print("✅ Contact updated.")

def delete_contact():
    identifier = input("Enter name or phone to delete: ")
    cur.execute("DELETE FROM phonebook WHERE first_name = %s OR phone = %s", (identifier, identifier))
    conn.commit()
    print("✅ Contact deleted (if existed).")

def view_all_contacts():
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    if not rows:
        print("📭 PhoneBook is empty.")
    else:
        print("\n📱 PhoneBook Entries:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")

def filter_contacts():
    value = input("Enter name or phone to search: ")
    cur.execute("SELECT * FROM phonebook WHERE first_name = %s OR phone = %s", (value, value))
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(f"🔍 ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")
    else:
        print("❌ No matching contacts found.")

def menu():
    while True:
        print("\n📖 PhoneBook Menu:")
        print("1. Upload from CSV")
        print("2. Add contact manually")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. View all contacts")
        print("6. Filter contacts")
        print("0. Exit")

        choice = input("Choose option: ")

        if choice == '1':
            insert_from_csv("contacts.csv")
        elif choice == '2':
            insert_from_console()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            view_all_contacts()
        elif choice == '6':
            filter_contacts()
        elif choice == '0':
            print("👋 Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")

menu()

cur.close()
conn.close()

''' 
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    phone VARCHAR(20) UNIQUE
);

INSERT INTO phonebook (first_name, phone)
VALUES 
('Beks', '87472253209'),
('Ali', '870098765544'),
('Nurik', '87077777777');

SELECT * FROM phonebook;
'''