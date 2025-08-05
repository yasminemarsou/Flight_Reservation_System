
import tkinter as tk
from tkinter import messagebox
import sqlite3

class EditReservationPage:
    def __init__(self, root, home_page, reservation):
        self.root = root
        self.home_page = home_page
        self.reservation = reservation
        self.clear_frame()
        self.edit_reservation_page()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def edit_reservation_page(self):
        tk.Label(self.root, text="Edit Reservation", font=("Arial", 18)).pack(pady=10)
        labels = ['ID', 'Name', 'Flight Number', 'Departure', 'Destination', 'Date', 'Seat Number']
        self.entries = {}

        for i, label in enumerate(labels):
            tk.Label(self.root, text=label).pack()
            entry = tk.Entry(self.root)
            entry.pack()
            entry.insert(0, self.reservation[i])
            if label == 'ID':
                entry.config(state='readonly')
            self.entries[label] = entry

        tk.Button(self.root, text="Update", command=self.update_reservation).pack(pady=10)
        tk.Button(self.root, text="Delete", command=self.delete_reservation).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.home_page.home_page).pack()

    def update_reservation(self):
        data = [self.entries[label].get() for label in ['Name', 'Flight Number', 'Departure', 'Destination', 'Date', 'Seat Number']]
        res_id = self.entries['ID'].get()
        conn = sqlite3.connect('flights.db')
        c = conn.cursor()
        c.execute("UPDATE reservations SET name=?, flight_number=?, departure=?, destination=?, date=?, seat_number=? WHERE id=?", data + [res_id])
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Reservation updated!")
        self.home_page.home_page()

    def delete_reservation(self):
        res_id = self.entries['ID'].get()
        conn = sqlite3.connect('flights.db')
        c = conn.cursor()
        c.execute("DELETE FROM reservations WHERE id=?", (res_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Reservation deleted!")
        self.home_page.home_page()