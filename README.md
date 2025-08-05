# Flight_Reservation_System
A simple desktop-based Flight Reservation System built with Python, Tkinter for GUI, and SQLite for data storage.

# Features
Book Flight Tickets
View Reservations
Edit & Delete Reservations
# Technologies Used
Python 3.x
Tkinter
SQLite3
# Installation
# Clone the Repository:
git clone [https://github.com/yourusername/flight-reservation-app.git]
cd flight-reservation-app
# Install Requirements:
pip install -r requirements.txt
# Run the Application:
python main.py
Create Executable (Windows)
pyinstaller --onefile --windowed main.py
The .exe file will be in the /dist directory.

# Project Structure
/flight_reservation_app
│
├── main.py               # Main entry
├── database.py           # DB setup
├── home.py               # Home page
├── booking.py            # Booking form
├── reservations.py       # Reservations listing
├── edit_reservation.py   # Edit/Delete functions
├── flights.db            # SQLite database
├── requirements.txt      # Required libraries
├── README.md             # Documentation
