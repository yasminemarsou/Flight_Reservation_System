
import tkinter as tk
import sqlite3
from home import HomePage

conn = sqlite3.connect('Flights.db')

if __name__ == "__main__":
    cur = conn.cursor()
    root = tk.Tk()
    app = HomePage(root)
    root.mainloop()