import sqlite3

from config import (DATABASE_1)

# Connect to SQLite database
conn = sqlite3.connect(r'Resources\fart.db')
cursor = conn.cursor()

# Open and read the .sql file
with open(DATABASE_1, 'r', encoding='utf-8') as sql_file:
    sql_script = sql_file.read()

# Execute the SQL script
cursor.executescript(sql_script)

# Commit changes and close the connection
conn.commit()
conn.close()
