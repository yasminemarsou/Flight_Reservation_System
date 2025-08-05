
import tkinter as tk
from tkinter import messagebox
import sqlite3

class BookingPage:
    def __init__(self, root, home_page):
        self.root = root
        self.home_page = home_page
        self.clear_frame()
        self.booking_page()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def booking_page(self):
        tk.Label(self.root, text="Book Flight", font=("Arial", 18)).pack(pady=10)
        labels = ['Name', 'Flight Number', 'Departure', 'Destination', 'Date', 'Seat Number']
        self.entries = {}

        for label in labels:
            tk.Label(self.root, text=label).pack()
            entry = tk.Entry(self.root)
            entry.pack()
            self.entries[label] = entry

        tk.Button(self.root, text="Submit", command=self.book_flight).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.home_page.home_page).pack()

    def book_flight(self):
        data = [self.entries[label].get() for label in self.entries]
        if all(data):
            conn = sqlite3.connect('flights.db')
            c = conn.cursor()
            c.execute("INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number) VALUES (?, ?, ?, ?, ?, ?)", data)
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Flight booked successfully!")
            self.home_page.home_page()
        else:
            messagebox.showwarning("Input error", "All fields are required.")