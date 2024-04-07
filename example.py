import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('entroPass.db')
cursor = conn.cursor()

# Fetch all rows from a table (replace 'your_table' with the actual table name)
cursor.execute('SELECT * FROM Authenticate')
rows = cursor.fetchall()

# Print the rows
for row in rows:
    print(row)

# Close the connection
conn.close()
