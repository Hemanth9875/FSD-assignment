import sqlite3
# Connect to SQLite database (or create it if it doesn't exist)
connect= sqlite3.connect('contact_book.db')
cursor= connect.cursor()

# Create table
cursor.execute('''
    CREATE TABLE contacts
    (ID INTEGER PRIMARY KEY,
    Name TEXT,
    Cell TEXT,
    Email TEXT)
''')
# Insert 5 rows of data
data= [
    (1, 'hamenth C', '1234567890', 'GIRI@example.com'),
    (2, 'charan C', '0987654321', 'LOHITH@example.com'),
    (3, 'abhishek C', '1112223333', 'CHANDRA@example.com'),
    (4, 'VR Verma', '4445556666', 'VERRAMMA@example.com'),
    (5, 'Suretkal', '7778889999', 'VEMGAL@example.com'),
]
cursor.executemany('INSERT INTO contacts VALUES (?,?,?,?)', data)
# Commit the changes
connect.commit()
# Fetch all data
cursor.execute('SELECT * FROM contacts')
# Display all data
rows = cursor.fetchall()

print("ID\tName\t\tCell#\t\t\tEmail")
print("-" * 50)
for row in rows:
    print(f"{row[0]}\t{row[1]}\t\t{row[2]}\t\t{row[3]}")

# Close the connection
connect.close()