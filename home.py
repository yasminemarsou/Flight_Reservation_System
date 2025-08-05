
import tkinter as tk
from booking import BookingPage
import sqlite3
from tkinter import ttk

class HomePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Flight Reservation System")
        self.root.geometry("600x400")
        self.home_page()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def home_page(self):
        self.clear_frame()
        tk.Label(self.root, text="Flight Reservation System", font=("Arial", 18)).pack(pady=20)
        tk.Button(self.root, text="Book Flight", command=self.open_booking).pack(pady=10)
        tk.Button(self.root, text="View Reservations", command=self.open_reservations).pack(pady=10)

    def open_booking(self):
        BookingPage(self.root, self)

    def open_reservations(self):
        ReservationsPage(self.root, self)

       
    def view_reservations_page(self):
        tk.Label(self.root, text="Reservations", font=("Arial", 18)).pack(pady=10)
        self.tree = ttk.Treeview(self.root, columns=('ID', 'Name', 'Flight No.', 'From', 'To', 'Date', 'Seat'), show='headings')
        for col in self.tree['columns']:
            self.tree.heading(col, text=col)
        self.tree.pack()

        conn = sqlite3.connect('flights.db')
        c = conn.cursor()
        c.execute("SELECT * FROM reservations")
        for row in c.fetchall():
            self.tree.insert('', 'end', values=row)
        conn.close()

        tk.Button(self.root, text="Edit Reservation", command=self.edit_reservation).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.home_page.home_page).pack(pady=5)

    def edit_reservation(self):
        selected = self.tree.focus()
        if selected:
            values = self.tree.item(selected, 'values')
            EditReservationPage(self.root, self.home_page, values)