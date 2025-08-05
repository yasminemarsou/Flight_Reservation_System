
import tkinter as tk
from tkinter import ttk
import sqlite3


class ReservationsPage:
    def __init__(self, root, home_page):
        self.root = root
        self.home_page = home_page
        self.clear_frame()
        self.view_reservations_page()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

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