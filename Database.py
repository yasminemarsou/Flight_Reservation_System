
import sqlite3

conn = sqlite3.connect('Flights.db')
cur = conn.cursor()

# Corrected CREATE TABLE statement
cur.execute("""CREATE TABLE flight_reservation (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            passenger_name TEXT,
            flight_number INTEGER,
            departure TEXT,
            destination TEXT,
            date TEXT,  -- Changed to TEXT as dates are typically stored as text in SQLite
            seat_number INTEGER
            )""")

conn.commit()  # Save the changes
conn.close()


